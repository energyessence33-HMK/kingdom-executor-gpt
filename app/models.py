from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Status(str, Enum):
    REQUESTED = "REQUESTED"
    PLANNED = "PLANNED"
    AWAITING_APPROVAL = "AWAITING_APPROVAL"
    EXECUTING = "EXECUTING"
    VERIFYING = "VERIFYING"
    VERIFIED = "VERIFIED"
    FAILED = "FAILED"
    BLOCKED = "BLOCKED"


class Risk(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass
class Task:
    task_id: str
    objective: str
    scope: str = ""
    risk_level: Risk = Risk.LOW
    approval_required: bool = False
    status: Status = Status.REQUESTED
    plan: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)
    verification_checks: list[str] = field(default_factory=list)
    rollback_plan: str = ""
    evidence: list[dict[str, Any]] = field(default_factory=list)
    audit_log: list[dict[str, Any]] = field(default_factory=list)

    def transition(self, status: Status) -> None:
        self.status = status
