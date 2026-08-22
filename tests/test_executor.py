from app.executor import execute
from app.models import Risk, Status, Task


def test_low_risk_without_connector_evidence_is_blocked_not_verified():
    task = Task(task_id="t-1", objective="inspect store")
    result = execute(task)
    assert result.status == Status.BLOCKED
    assert any(e["event"] == "blocked" for e in result.audit_log)


def test_high_risk_requires_approval():
    task = Task(task_id="t-2", objective="change payment settings", risk_level=Risk.HIGH)
    result = execute(task)
    assert result.status == Status.AWAITING_APPROVAL


def test_verified_requires_evidence():
    task = Task(task_id="t-3", objective="perform verified action")
    task.evidence.append({"source": "test", "result": "confirmed"})
    result = execute(task)
    assert result.status == Status.VERIFIED
