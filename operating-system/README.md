# Kingdom Executor Studio Synchronization Surface

`studio-sync.json` is the versioned, canonical exchange surface between the Kingdom Executor GPT and Kingdom Executor Studio.

The GPT remains the **brain** and canonical intelligence source. The Studio remains the **body**: it stores operational workflow state, presents execution interfaces, and carries out approved actions. This file shares only structured priority tasks and AI-workflow metadata. It never contains prompt bodies, hidden reasoning, user conversations, credentials, or executable integration code.

## Item Types

| Type | Purpose | Canonical authority |
| :--- | :--- | :--- |
| `priority_task` | A high-priority operating task that can be reconciled with a Studio workflow. | The reviewed upstream document. |
| `ai_workflow` | Structured metadata describing an approved worker/workflow capability. | The reviewed upstream document. |

Each item requires a stable `externalId`, title, description, priority, status, dependency list, origin, and ISO-8601 `updatedAt` timestamp. The supported `schemaVersion` is `1`.

Studio reads this file through a server-side boundary. Studio-to-GPT changes are staged as an L3 governed request and need a recorded human approval before the server makes a GitHub write. Concurrent source and Studio changes are treated as conflicts, not silent overwrites.
