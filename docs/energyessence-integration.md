# EnergyEssence Integration Contract

## Role

Kingdom Executor provides governance, planning, verification, and auditability. EnergyEssence remains the commerce domain. Integration must preserve separation of concerns.

## Read path

The executor may inspect authorized Shopify/product/catalog/marketing state and normalize it into an internal audit model.

## Write path

Writes must be explicit, scoped, logged, and verified. Customer-facing publication is a separate state from drafting.

## Product branding pipeline

`INGEST → NORMALIZE → CLASSIFY → EVIDENCE CHECK → BRAND MAP → GENERATE SPEC → HUMAN REVIEW (when required) → PUBLISH → VERIFY`

### Required normalized product fields

- source product ID
- supplier/source
- product category
- EnergyEssence ritual/category
- canonical display name
- ingredients/key actives where verified
- serving/usage data where verified
- certifications where verified
- approved claims
- prohibited/unsupported claims
- price/currency
- media inventory
- alt text
- SEO metadata
- status

## Image specification pipeline

The system should generate a structured image brief before generating or requesting an image:

- product identity
- package type
- label hierarchy
- verified product facts
- brand palette
- typography rules
- composition
- lighting
- props/natural elements
- background
- watermark rule
- output dimensions
- accessibility/alt-text requirements

Never put unverified ingredient quantities, certifications, health outcomes, or supplier claims onto a label or marketing image.

## Verification

After any product update, verify the storefront state and compare it with the intended normalized record. Report discrepancies rather than assuming synchronization.

## Failure handling

If Shopify/CJ/other integration is unavailable, do not fabricate data. Preserve the draft/specification and mark the task BLOCKED with the missing dependency.
