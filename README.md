# OVDS

Open Vehicle Data Standard.

OVDS is an open, portable standard for representing vehicle data using JSON Schema.

This repository contains the specification only. It does not contain backend code, framework bindings, or application logic.

## Documentation

- Overview: [docs/index.md](docs/index.md)
- Normative spec: [spec/v0.2.0/readme.md](spec/v0.2.0/readme.md)

## Data Model

OVDS v0.2.0 is organized around a concrete vehicle record with separate reusable technical entities.

- Group: reusable automotive group definition above makes
- Make: reusable brand or marque definition
- Platform: reusable architecture shared across makes or groups
- Vehicle: published vehicle configuration with lineage, technical configuration, and canonical specs
- Safety: normalized safety feature set intended for cross-brand comparison
- Engine: reusable internal combustion engine definition
- Electric motor: reusable traction motor definition
- Battery pack: reusable battery pack definition
- Transmission: reusable transmission definition

This keeps commercial lineage separate from technical composition while reducing duplication across generations, model years, and variants.

## Goals

- JSON-first
- Framework-independent
- Extensible without breaking the core model
- Explicitly versioned specification releases
- Safe evolution through additive changes

## Core Vehicle Model

The current v0.2.0 schemas are defined in:

- `spec/v0.2.0/vehicle.schema.json`
- `spec/v0.2.0/group.schema.json`
- `spec/v0.2.0/make.schema.json`
- `spec/v0.2.0/platform.schema.json`
- `spec/v0.2.0/safety.schema.json`
- `spec/v0.2.0/engine.schema.json`
- `spec/v0.2.0/electric-motor.schema.json`
- `spec/v0.2.0/battery-pack.schema.json`
- `spec/v0.2.0/transmission.schema.json`

The vehicle schema is structured around these top-level blocks:

- `id`
- `lineage`
- `configuration`
- `origin`
- `specs`
- `performance`
- `costOfOwnership`
- `safety`
- `compliance`
- `attributes`

Within `specs`, OVDS can capture both physical measurements and published capacities such as passenger, payload, towing capacity, cargo capacity, ground clearance, and footprint.

Within `configuration`, powertrain data references reusable engine, electric motor, and battery pack entities instead of redefining them inline.

`configuration` can also include a published `bodyStyle` classification for the vehicle.

`configuration` may also include a dedicated `charging` block for published charging ports, AC/DC charging capability, and charging-time scenarios such as `10-80` or `0-100` under specific connector, power, and supply-context conditions.

`configuration` may also include `emissionsControls` for published catalytic-converter fitment, oxygen sensors, EGR, secondary air injection, onboard diagnostics, durability standard, and particulate filters.

`origin` captures the published assembly location for the concrete vehicle configuration, such as country, region, or plant when known.

The current powertrain model is role-based and separates:

- energy sources
- energy storage
- energy converters
- traction motors

This allows OVDS to represent vehicles such as series hybrids and range-extended EVs without treating every propulsion component as an `engine`.

Fuel capacity is modeled inside energy storage, while longer-horizon ownership estimates are modeled separately in `costOfOwnership`.

Published efficiency, range, emissions, acceleration, top speed, torque, and system power results are modeled separately from compliance data so test-cycle values and regulatory classifications can coexist without being conflated.

In v0.2.0, `compliance.approvals` adds a portable way to represent official approvals and certifications across markets. Each approval can capture the authority, jurisdiction, scheme, domain, identifier, status, and one or more official `sourceDocs` without duplicating vehicle lineage fields such as `modelYear`.

Reusable engine and electric-motor schemas can also store component-level power values without duplicating vehicle-level combined output.

Safety features are modeled separately from both compliance and commercial packaging so they can be compared across brands using a common taxonomy.

## Versioning

OVDS versions are published by directory within the repository, for example `spec/v0.2.0/`.

This repository does not use long-lived branches as the primary versioning mechanism for the standard.

The intended release strategy is:

- versioned specification directories in `spec/`
- matching explanatory documentation under `docs/versions/`
- Git tags for official published releases such as `v0.1.0`, `v0.1.1`, `v0.1.2`, and `v0.2.0`

This keeps multiple specification versions visible in one repository while making published releases easy to reference and later expose in generated documentation sites.

## Conventions

- Field names currently use `camelCase`.
- Schemas use JSON Schema draft 2020-12.
- Every property should include a clear description.
- Entity identifiers use human-readable, deterministic uppercase slugs in the form `OVDS-<TYPE>-<TOKEN>-<TOKEN>...`.
- Lineage IDs follow the commercial hierarchy: `OVDS-MK-AETHRA`, `OVDS-MD-AETHRA-LYNX`, `OVDS-GN-AETHRA-LYNX-1`, `OVDS-VR-AETHRA-LYNX-2026-ECLIPSE-LONG-RANGE`.
- Vehicle IDs identify a concrete published configuration, for example `OVDS-V-AETHRA-LYNX-2026-ECLIPSE-LONG-RANGE-RWD-84KWH`.
- Reusable technical IDs should use stable technical names or codes, for example `OVDS-EG-2ZR-FXE`, `OVDS-EM-APP550`, `OVDS-BP-AURORA-84`.
- A single `variantId` may map to multiple `vehicle.id` values when one commercial trim is offered with multiple technical configurations.

## Usage

Other systems, such as APIs or internal services, can consume OVDS schemas to
validate payloads and declare compliance. Those implementations do not belong in
this repository.

## Validation

Use uv to install the locked dependencies and validate the published schemas:

```bash
uv sync
uv run python scripts/validate_schemas.py
```

You can also validate a concrete JSON document against a specific schema $id:

```bash
uv run python scripts/validate_schemas.py \
  --schema-id https://ovds.xyz/spec/v0.2.0/vehicle.schema.json \
  --instance examples/v0.2.0/ev.json
```

The validation script loads local schemas from `spec/` into an in-memory registry so
canonical `$id` references resolve without network access.

Reference examples under `examples/v0.2.0/` currently cover battery-electric, diesel ICE, natural-gas ICE, mild-hybrid, full-hybrid, plug-in hybrid, and series-hybrid configurations, including market-specific approval examples for EPA, EU type approval, and Mexico NOM.

## Compliance

A system can be described as OVDS-compliant when it produces or accepts payloads
that match a published OVDS schema version and follows the semantic rules in the
corresponding standard document.

## Contributing

See `CONTRIBUTING.md` for contribution and versioning rules.
