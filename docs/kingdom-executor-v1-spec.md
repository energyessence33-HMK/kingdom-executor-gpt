# Kingdom Executor GPT — V1 Build Specification

## Purpose

Turn the existing Kingdom Executor repository into a governed execution layer for the user's business systems, beginning with EnergyEssence, without claiming that work is complete until it has been verified.

## Source of truth

This specification extends the repository's existing architecture: frontend, backend API, database, task executor, message queue, and monitoring/logging. The repository documentation explicitly calls for secured APIs, environment-variable configuration, containerization, CI/CD, and dependency maintenance.

## Operating principles

1. **Truth before completion:** Never report an action as completed without observable evidence.
2. **Plan → execute → verify → report:** Every material task follows this lifecycle.
3. **Least privilege:** Credentials and integrations receive only the access required for a task.
4. **No secret commits:** Secrets belong in environment/secret management, never source control.
5. **Human approval gates:** Financial transactions, irreversible production changes, legal/compliance changes, credential changes, and destructive data operations require explicit approval unless an independently verified policy grants execution authority.
6. **Auditability:** Every execution records task, actor, timestamp, inputs, actions, outputs, verification result, and failure reason when applicable.
7. **Idempotency:** Re-running a task must not create unintended duplicates or corrupt state.
8. **Rollback:** Production changes must have a documented rollback path where technically possible.
9. **Scope control:** The executor must distinguish what it can access, what it can modify, and what it can only recommend.
10. **No invented evidence:** Screenshots, API responses, test results, sales, approvals, and deployment status must never be fabricated.

## Execution state machine

`REQUESTED → PLANNED → AWAITING_APPROVAL (when required) → EXECUTING → VERIFYING → VERIFIED | FAILED | BLOCKED`

A task is only called **done** when it reaches `VERIFIED` with evidence.

## Task contract

Each task should have:

- `task_id`
- `objective`
- `scope`
- `risk_level`
- `required_integrations`
- `approval_required`
- `plan`
- `actions`
- `verification_checks`
- `rollback_plan`
- `status`
- `evidence`
- `audit_log`

## Risk levels

- **LOW:** read-only inspection, reporting, non-production drafting.
- **MEDIUM:** reversible configuration/content changes with limited blast radius.
- **HIGH:** production changes affecting checkout, customer data, integrations, pricing, automation, or public-facing behavior.
- **CRITICAL:** credentials, financial movement, destructive data operations, legal/compliance state, or irreversible infrastructure changes.

HIGH and CRITICAL operations require explicit approval unless a documented automation policy specifically authorizes them.

## EnergyEssence integration boundary

EnergyEssence is the first commerce execution domain. The executor should treat Shopify as the system of record for storefront/product state and use connected services only through authenticated, least-privilege interfaces.

Initial capabilities:

- Store/product audit
- Product metadata and branding consistency checks
- SEO/alt-text audits
- Collection/category consistency checks
- Draft product copy
- Draft image-generation specifications
- Conversion-system audits
- Legal/compliance checklist generation
- Marketing workflow planning
- Change verification and evidence reporting

Do not automatically publish health claims, pricing, payment configuration, legal text, or customer-facing changes without the appropriate approval gate.

## Branding intelligence

EnergyEssence brand rules supplied to the system should be represented as structured policy rather than repeated ad hoc instructions. The system should maintain:

- visual identity
- typography
- color palette
- product-category rules
- naming conventions
- image composition rules
- label-data requirements
- approved claims
- prohibited/unsupported claims
- SEO/alt-text formula
- ritual taxonomy

The executor should compare each proposed product asset against the brand policy and return PASS, WARN, or BLOCK with reasons.

## Evidence standard

For every execution report:

- State what was inspected.
- State what was changed.
- State what could not be changed.
- Provide concrete evidence identifiers where available.
- Separate verified facts from recommendations.
- Never infer successful execution from an instruction being issued.

## V1 deliverables

1. Governed task schema.
2. Risk/approval policy.
3. Audit-log model.
4. Verification framework.
5. Integration boundary for EnergyEssence.
6. Prompt/policy library structure.
7. Test fixtures for success, failure, blocked, and rollback scenarios.
8. Documentation describing local setup, environment variables, testing, and deployment.
9. CI checks for formatting, linting, tests, secret scanning, and security-sensitive configuration.

## Definition of done

V1 is not complete until:

- tests exist and pass;
- security checks are documented and run;
- no secrets are committed;
- the task lifecycle is demonstrable end-to-end;
- blocked/approval-required tasks behave correctly;
- verification evidence is captured;
- EnergyEssence integration boundaries are documented;
- a human can reproduce the setup from the repository documentation.
