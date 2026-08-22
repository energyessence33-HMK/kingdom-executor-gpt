from __future__ import annotations

from datetime import datetime, timezone

from .models import Status, Task
from .policy import authorize


def _event(task: Task, event: str, **data: object) -> None:
    task.audit_log.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event,
        **data,
    })


def execute(task: Task, approved: bool = False) -> Task:
    """Run the V1 lifecycle for a task whose external actions are supplied by callers.

    This first runtime intentionally does not pretend to have Shopify/OpenAI/GitHub
    write access. It provides the governed state machine and evidence contract.
    """
    try:
        task.transition(Status.PLANNED)
        _event(task, "planned", objective=task.objective)

        if task.approval_required or task.risk_level.value in {"HIGH", "CRITICAL"}:
            task.transition(Status.AWAITING_APPROVAL)
            _event(task, "approval_required", risk=task.risk_level.value)
            authorize(task, approved=approved)

        task.transition(Status.EXECUTING)
        _event(task, "executing")

        # External connector actions are deliberately not invented here.
        # A connector adapter must append concrete evidence after performing work.
        task.transition(Status.VERIFYING)
        _event(task, "verifying")

        if not task.evidence:
            task.transition(Status.BLOCKED)
            _event(task, "blocked", reason="No execution evidence was supplied by an external adapter.")
            return task

        task.transition(Status.VERIFIED)
        _event(task, "verified", evidence_count=len(task.evidence))
        return task
    except PermissionError as exc:
        task.transition(Status.AWAITING_APPROVAL)
        _event(task, "approval_denied", reason=str(exc))
        return task
    except Exception as exc:
        task.transition(Status.FAILED)
        _event(task, "failed", error=str(exc))
        return task
