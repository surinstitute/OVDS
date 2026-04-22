---
title: Vehicle Schema
---

# Vehicle Schema

Schema file: [spec/v0.2.0/vehicle.schema.json](../../v0.2.0/vehicle.schema.json)

## Purpose

The vehicle schema represents a concrete published vehicle configuration.

## Top-Level Structure

- `id`: the OVDS vehicle identifier
- `lineage`: make, model, generation, model year, and optional variant context
- `configuration`: technical composition for the published configuration
- `origin`: published assembly origin for the concrete vehicle configuration
- `specs`: canonical measurements, weights, and capacities
- `performance`: published efficiency, range, emissions, acceleration, top speed, and torque results
- `costOfOwnership`: ownership-cost estimates such as ten-year energy and maintenance costs
- `safety`: normalized safety features comparable across brands
- `compliance`: regulatory and certification records such as emissions or safety classifications
- `attributes`: free-form escape hatch for normalized public-source attributes

## Notes

- `lineage.modelYear` is the commercial model year.
- `lineage.platformId` is optional and identifies a shared platform that may span multiple makes or groups.
- `lineage.variantId` is optional and sits below model year in the hierarchy.
- `configuration.powertrain` models propulsion through energy sources, storage, converters, and traction motors.
- `configuration.powertrain.architecture` distinguishes electrified combustion (`mild_hybrid`) from full-hybrid (`parallel_hybrid` or `power_split_hybrid`), plug-in hybrid (`plug_in_hybrid`), and series-hybrid (`series_hybrid`) layouts.
- `configuration.charging` models published charging ports, AC and DC charging capability, bidirectional support, and charging-time scenarios, including whether a published charging time applies to home charging or public charging.
- `configuration.emissionsControls` models published emissions-control hardware and diagnostics such as catalytic converters, oxygen sensors, EGR, onboard diagnostics, and particulate filters.
- `configuration.emissionsControls.catalystSystems` can capture catalyst type and placement, for example three-way, diesel oxidation, or SCR stages.
- `configuration.emissionsControls.emissionsSensors` can capture sensor type and placement, for example upstream wideband oxygen or downstream NOx monitoring.
- `configuration.powertrain.energyStorage` can represent fuel tanks and battery packs, including fuel capacity.
- `configuration.bodyStyle` captures published body style labels such as sedan, hatchback, or suv.
- `origin` captures published assembly origin and is separate from lineage because origin may differ across otherwise similar vehicles.
- `configuration.powertrain` already reserves `fuelCellStackId` for future expansion, even though v0.2.0 does not yet define a standalone fuel-cell stack schema.
- `specs` keep SI-normalized values with optional source-unit traceability and can also include physical capacities and dimensional details such as door count, passenger capacity, payload, towing capacity, cargo capacity, ground clearance, front track width, rear track width, published footprint, and front/rear brake type.
- `performance` stores published results rather than fixed physical specs and can include acceleration, top speed, torque, and power in addition to efficiency, range, and emissions.
- `performance.efficiency` supports both liquid-fuel and gaseous-fuel reporting, including mass-based fuel-consumption units for CNG-style examples.
- `performance` cycle labels can use aggregate values such as `epa` or more specific source cycles such as `ftp` and `hfet` when the source publishes them separately.
- `performance.emissions` can represent both greenhouse-gas and criteria-pollutant results, including `co2`, `co`, `hc`, `nmhc`, `n2o`, `ch4`, `nox`, particulate metrics, and evaporative hydrocarbons.
- `costOfOwnership` is separate from performance and captures longer-horizon ownership estimates such as ten-year energy and maintenance cost.
- `safety` is separate from compliance and models comparable safety capabilities rather than commercial package names.
- `compliance` is intentionally separate so certification and regulatory data do not get mixed with measured performance results.
- `compliance.approvals` captures portable approval records for homologation, certification, and conformance schemes across markets.
- Approval entries should not duplicate lineage fields already defined on the vehicle, such as `lineage.modelYear`.
- `compliance.approvals[].sourceDocs` can attach one or more official supporting publications, certificates, or registry documents.

See also [spec/v0.2.0/readme.md](../../v0.2.0/readme.md).
