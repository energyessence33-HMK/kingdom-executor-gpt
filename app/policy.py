from __future__ import annotations

from .models import Risk, Task


APPROVAL_RISKS = {Risk.HIGH, Risk.CRITICAL}


def requires_approval(task: Task) -> bool:
    """Apply the V1 policy gate before execution."""
    return task.approval_required or task.risk_level in APPROVAL_RISKS


def authorize(task: Task, approved: bool = False) -> None:
    if requires_approval(task) and not approved:
        raise PermissionError("Explicit approval is required for this task.")
