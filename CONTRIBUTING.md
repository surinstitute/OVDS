# Contributing to OVDS

## Scope

This repository contains the OVDS specification only.

Accepted contributions include:

- Schema improvements
- Clarifications to semantic rules
- Additional examples
- Additive, backward-compatible extensions to published models

This repository should not include:

- Backend implementations
- Framework-specific integrations
- Application-specific business logic

## Compatibility Rules

OVDS versions must evolve without breaking consumers.

- Do add new optional properties.
- Do add new examples and documentation.
- Do add new extension namespaces.
- Do not remove existing properties from a published version.
- Do not change the semantic meaning of an existing property.
- Do not rename existing properties.

If a change is incompatible, publish it as a new version instead of modifying an
existing version in place.

## Versioning Workflow

OVDS versions are maintained by directory within the repository, such as `spec/v0.1/`.

Contributors should follow these rules:

- Add backward-compatible changes to the active development version only.
- Do not make incompatible changes in an already published version directory.
- When a change is incompatible, create a new version directory instead of rewriting a published one.
- Keep matching explanatory version pages under `docs/versions/`.
- Use Git tags for published releases; do not use long-lived version branches as the primary release mechanism.

## Style Rules

- Follow the field naming convention used by the published schema version.
- Use JSON Schema draft 2020-12 for the current v0.1 schemas.
- Add a clear `description` for each schema property.
- Keep the core schema minimal and portable.
- Prefer extensibility through `extensions` for domain-specific data.
- Use human-readable, deterministic uppercase IDs.
- For lineage entities, derive IDs from the commercial hierarchy, for example `OVDS-MD-AETHRA-LYNX` or `OVDS-VR-AETHRA-LYNX-2026-ECLIPSE-LONG-RANGE`.
- For reusable technical entities, prefer stable technical codes or published family names, for example `OVDS-EG-2ZR-FXE` or `OVDS-BP-AURORA-84`.
- Keep ID tokens stable over time and avoid opaque random identifiers in published examples.
- Do not overload `variantId` with technical configuration details when the same commercial variant is sold with multiple motors, batteries, drivetrains, or transmissions.
- Use `vehicle.id` for the unique published configuration record when technical differentiation is required.

## Examples

Every new field or extension proposal should include at least one example under
`examples/` when practical.

## Documentation

Semantic rules belong in the versioned `readme.md` file alongside the schema.
The schema defines structure. The standard document defines meaning and usage.

Explanatory, navigable documentation should live under `docs/` so it can later be published with a documentation generator without restructuring the repository.

## Validation Workflow

Use uv for local validation work:

```bash
uv sync
uv run python scripts/validate_schemas.py
```

When adding examples or sample payloads, validate them explicitly against the target schema:

```bash
uv run python scripts/validate_schemas.py \
  --schema-id https://ovds.xyz/spec/v0.1/vehicle.schema.json \
  --instance path/to/example.json
```
