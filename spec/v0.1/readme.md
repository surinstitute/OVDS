# OVDS Standard v0.1

## Status

Draft.

## Scope

This document defines the semantic meaning and intended usage of the OVDS v0.1 schemas.

The JSON Schema files define structure. This document defines normative meaning.

## Entity Model

OVDS v0.1 includes the following primary entities:

- group
- make
- platform
- vehicle
- safety
- engine
- electric motor
- battery pack
- transmission

Fuel-cell stacks are not yet defined as a standalone reusable schema in v0.1.
The vehicle powertrain model reserves a `fuelCellStackId` reference so a future version can introduce that entity without redesigning the powertrain structure.

## Vehicle Semantics

A vehicle record represents a concrete published vehicle configuration.

## Identifier Semantics

OVDS identifiers are intended for open, portable referencing across datasets and implementations.

They should be:

- human-readable
- deterministic for the same published entity
- uppercase and tokenized with hyphens
- namespaced by entity type
- derived from canonical commercial hierarchy when the entity belongs to lineage
- derived from stable technical identity when the entity is a reusable component

The v0.1 identifier shape is:

- `OVDS-GR-...` for groups
- `OVDS-MK-...` for makes
- `OVDS-MD-...` for models
- `OVDS-PF-...` for platforms
- `OVDS-GN-...` for generations
- `OVDS-VR-...` for variants
- `OVDS-SM-...` for submodels
- `OVDS-TR-...` for transmissions
- `OVDS-EG-...` for engines
- `OVDS-EM-...` for electric motors
- `OVDS-BP-...` for battery packs
- `OVDS-FC-...` for future fuel-cell stacks
- `OVDS-V-...` for vehicles

The `OVDS` namespace prefix is used consistently in v0.1 to match the standard name and avoid ambiguity with external identifier systems.

For lineage entities, identifiers should follow the commercial hierarchy already modeled by OVDS.

- `makeId`: `OVDS-MK-<MAKE>`
- `modelId`: `OVDS-MD-<MAKE>-<MODEL>`
- `generationId`: `OVDS-GN-<MAKE>-<MODEL>-<GENERATION>` when generation is known
- `variantId`: `OVDS-VR-<MAKE>-<MODEL>-<MODELYEAR>-<VARIANT>` when variant is known
- `vehicle.id`: `OVDS-V-<MAKE>-<MODEL>-<MODELYEAR>-<VARIANT>-<CONFIGURATION>` for a concrete published configuration

This means lineage identifiers become more specific as they move down the hierarchy.

Uniqueness is scoped by entity level rather than forced across the full product tree.

- `makeId` is unique for a make.
- `modelId` is unique for a model or nameplate.
- `generationId` is unique for a generation.
- `variantId` is unique for a commercial variant, but a variant may still map to multiple technical configurations.
- `vehicle.id` is the most granular published identifier in v0.1 and should be unique for each concrete configuration record.

This means a single variant may legitimately have multiple vehicles beneath it, for example when the same trim is sold with multiple engines, battery packs, drivetrains, or transmissions.

For reusable technical entities, identifiers should not inherit full vehicle lineage unless that lineage is part of the component's stable public identity.

- `engine.id`: prefer a stable engine family or engine code, for example `OVDS-EG-2ZR-FXE`
- `electricMotor.id`: prefer a stable motor family or supplier/model code, for example `OVDS-EM-APP550`
- `batteryPack.id`: prefer a stable pack family or published pack designation, for example `OVDS-BP-AURORA-84`
- `platform.id`: prefer the stable platform name, for example `OVDS-PF-AURORA-EV`

The goal is open referencing. A reader should be able to infer what an identifier represents without consulting a private lookup table.

The `lineage` block identifies the commercial lineage of that configuration.

- `makeId` identifies the brand.
- `platformId`, when present, identifies a shared vehicle platform that may span multiple makes or groups.
- `modelId` identifies the stable model or nameplate.
- `generationId`, when present, identifies a generation spanning multiple model years.
- `modelYear` identifies the commercial model year.
- `variantId`, when present, identifies the trim or commercial variant for that model year.

`variantId` does not need to identify a single motorization or a single technical configuration.

`vehicle.id` is the identifier that distinguishes concrete published configurations within the same commercial variant.

The lineage identifier policy follows that same hierarchy: make first, then model, then generation, then model year and variant where applicable.

The `configuration` block identifies the technical composition of the vehicle.

- `powertrain` identifies the propulsion architecture and its energy roles.
- `charging`, when present, identifies the charging interfaces, AC/DC charging capability, and published charging-time scenarios.
- `transmissionId`, when present, identifies the transmission used by the configuration.
- `bodyStyle`, when present, identifies the published body style classification of the configuration.

The `origin` block identifies where the concrete vehicle configuration is assembled.

- `assemblyCountry` identifies the country of assembly for the published configuration.
- `assemblyRegion`, when present, identifies a published state, province, or region.
- `assemblyPlant`, when present, identifies the published plant or factory name.

Assembly origin is modeled separately from `lineage` because manufacturing location is not the same thing as make, model, or generation, and it may vary across otherwise similar vehicle records.

The `specs` block contains canonical SI measurements and weights for the published vehicle configuration.

The `specs` block may also contain published physical capacities such as passenger capacity, payload capacity, towing capacity, cargo capacity, and ground clearance.

`footprint`, when present, is treated as a published physical measurement rather than an internally derived value.

The `performance` block contains published results such as efficiency, range, emissions, acceleration, top speed, and torque.

Charging is modeled as part of `configuration` rather than as part of the battery pack because published charging behavior depends on the full vehicle charging system, not only on the pack itself.

Published charging-time results may also identify the supply context, such as a standard home outlet, dedicated home AC charging, public AC charging, or public DC charging.

The `costOfOwnership` block contains published ownership-cost estimates over a ten-year horizon.

The `safety` block contains normalized safety features intended to be comparable across brands without relying on commercial package names.

The `compliance` block contains regulatory or certification classifications that should not be mixed with measured or published performance results.

## Powertrain Semantics

Powertrain composition is modeled through roles rather than a single engine concept.

- `energySources` describe where the vehicle obtains energy.
- `energyStorage` describes how the vehicle stores energy on board.
- `energyConverters` describe components that convert source energy into usable propulsion energy.
- `tractionMotors` describe electric motors that deliver torque to the driven wheels.

Fuel-tank capacity is modeled as an energy storage property rather than as a vehicle dimension or a published performance result.

This allows OVDS to represent internal-combustion vehicles, mild hybrids, series hybrids, parallel hybrids, plug-in hybrids, battery-electric vehicles, and fuel-cell electric vehicles with a consistent model.

Within that taxonomy, `mild_hybrid` is treated as an electrified combustion architecture rather than as a full hybrid in the strict functional sense.

- `mild_hybrid` indicates an internal-combustion vehicle with a supporting electrical system that may provide start-stop, regeneration, or torque assist, but does not imply meaningful electric-only driving capability.
- `parallel_hybrid` and `power_split_hybrid` indicate hybrid architectures where combustion and electric propulsion both participate in vehicle drive.
- `plug_in_hybrid` indicates a hybrid architecture with external charging capability and a traction battery sized for published electric driving operation.
- `series_hybrid` indicates a hybrid architecture where wheel propulsion is electric and the combustion engine acts primarily as an onboard generator or range extender.

For example, a range-extended vehicle may use gasoline as an energy source, a combustion engine as a generator, a battery pack as energy storage, and one or more electric traction motors.

Fuel-cell electric vehicles are represented structurally in v0.1, but the referenced fuel-cell stack remains a forward-compatible placeholder until a dedicated schema is introduced.

## Performance And Compliance Semantics

Efficiency, range, and emissions are modeled as separate published results rather than as static specifications.

- `performance.efficiency` contains cycle-based efficiency results.
- `performance.range` contains cycle-based range results.
- `performance.emissions` contains cycle-based emissions results.

These values may vary by test cycle, scope, and market publication method.

Cost-of-ownership data is modeled separately from performance results.

- `costOfOwnership.tenYear` contains a ten-year estimate with annual driving distance, energy cost, maintenance cost, and total cost.

Compliance data is modeled separately from those results.

- `compliance.emissions` contains regulatory or certification classifications related to emissions.
- `compliance.safety` contains safety classifications or certification records.

## Safety Semantics

Safety features are modeled in a dedicated schema and grouped by capability area rather than by commercial package.

The v0.1 safety model uses grouped boolean features for cross-brand comparability.

This taxonomy is intentionally simple in v0.1 and may evolve in future versions without changing the role of safety as a standalone comparable feature set.

## Reusable Technical Entities

The engine, electric motor, battery pack, and transmission schemas are reusable across multiple vehicles.

The group, make, and platform schemas define reusable identity and architecture entities above the vehicle level.

This allows a single technical entity to be referenced by multiple model years, variants, or future fitment/application records without duplicating the same definition.

## Documentation Model

The content under `docs/` is explanatory documentation intended to support implementers and future site generation.

This `readme.md` file is the normative source for v0.1 semantic rules.
