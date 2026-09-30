# Kingdom Executor GPT — V2 Orchestration Specification

## Purpose

Evolve Kingdom Executor from a prompt collection into a governed intelligence/orchestration layer that can coordinate the user's connected engineering, knowledge, data, design, creative, deployment, AI, automation, file, and research systems without fabricating access or completion.

## Canonical architecture

VISION → INTELLIGENCE → ARCHITECTURE → CONNECTOR ROUTING → EXECUTION → VERIFICATION → EVIDENCE → DOCUMENTATION → OPTIMIZATION

### Source-of-truth boundaries

- Kingdom Executor GPT: canonical intelligence, operating policy, approved workflow metadata, strategic orchestration.
- Kingdom Executor Studio: operational UI, workflow state, execution surfaces, audit evidence.
- GitHub: canonical software source for repositories that explicitly designate GitHub as authoritative.
- Notion: canonical knowledge/decision source where a workspace page is explicitly authoritative.
- Airtable: canonical structured operational source where a base/table is explicitly authoritative.
- Figma/Canva/Adobe: canonical creative/design source only for artifacts explicitly maintained there.
- Shopify and other external platforms: canonical commerce/service state within their respective domains.
- No system automatically becomes authoritative merely because it is connected.

## Universal connector layer

The executor maintains a versioned connector registry describing capability, domain, authority, read/write level, approval level, and fallback behavior.

The registry is routing metadata, not a credential store.

Required connector classes:
1. GitHub — engineering/source control.
2. Notion — knowledge and operating documentation.
3. Slack — team communication and operational alerts.
4. Airtable — structured data and operations.
5. Figma — interface/design systems.
6. Canva — marketing and brand production.
7. Adobe — advanced creative/document workflows.
8. Lovable — application generation.
9. AppDeploy — deployment/QA/monitoring.
10. OpenAI Platform — AI/API infrastructure.
11. Automations — scheduled/conditional execution.
12. Files — persistent source artifacts.
13. Web research — current external intelligence.
14. Other authenticated connectors discovered at runtime.

## Connector routing algorithm

For each request:
1. Identify the required capability.
2. Check the connector registry.
3. Check actual runtime availability and permissions.
4. Select the smallest sufficient connector set.
5. Order calls by dependency.
6. Execute reads before writes when possible.
7. Verify each material write.
8. Persist evidence to the correct system of record.
9. Reconcile cross-system state.
10. Escalate conflicts or approval-gated actions.

Do not perform an integration merely because it exists. Relevance, permission, ownership, and risk determine routing.

## Execution state machine

REQUESTED → INSPECTING → PLANNED → AWAITING_APPROVAL → EXECUTING → VERIFYING → VERIFIED

Alternative terminal states:
BLOCKED | CONFLICT | FAILED | PARTIAL

A task is not DONE unless it reaches VERIFIED with evidence.

## Task contract

Each material task should carry:
- task_id
- objective
- scope
- risk_level
- required_integrations
- approval_required
- plan
- actions
- verification_checks
- rollback_plan
- status
- evidence
- audit_log

## Risk model

- LOW: read-only inspection, reporting, drafting.
- MEDIUM: reversible content/configuration changes.
- HIGH: production-facing changes, pricing, integrations, customer data, public automation.
- CRITICAL: credentials, financial movement, destructive data operations, legal/compliance state, irreversible infrastructure.

HIGH and CRITICAL operations require explicit approval unless a documented policy independently authorizes them.

## Cross-system integrity

- Never silently overwrite a conflicting source.
- Never duplicate an existing system when an authoritative implementation exists.
- Never copy secrets into sync surfaces.
- Never expose private credentials to mobile/client code.
- Use current object/blob versions for updates where supported.
- Keep audit trails for material mutations.
- Prefer idempotent actions and documented rollback.
- Verify after every consequential mutation.

## GitHub engineering standard

The canonical GPT repository should contain:
- core orchestration prompt/policy;
- versioned operating-system sync contract;
- connector registry;
- architecture/specification;
- test and CI conventions;
- integration documentation.

The Studio repository should consume structured metadata through its existing server-side synchronization boundary rather than copying the GPT's reasoning into the app.

## Definition of done for V2 foundation

- Canonical orchestration rules exist.
- Connector routing metadata exists.
- Studio sync remains schema-compatible.
- Secrets remain outside source control.
- Cross-system ownership and approval rules are documented.
- Existing code is reused instead of duplicated.
- Tests and CI remain part of the release path.
- Verification evidence is required for completion claims.
