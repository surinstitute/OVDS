# Vehicle Schema

Schema file: [spec/v0.1/vehicle.schema.json](../../spec/v0.1/vehicle.schema.json)

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
- `configuration.powertrain.energyStorage` can represent fuel tanks and battery packs, including fuel capacity.
- `configuration.bodyStyle` captures published body style labels such as sedan, hatchback, or suv.
- `origin` captures published assembly origin and is separate from lineage because origin may differ across otherwise similar vehicles.
- `configuration.powertrain` already reserves `fuelCellStackId` for future expansion, even though v0.1 does not yet define a standalone fuel-cell stack schema.
- `specs` keep SI-normalized values with optional source-unit traceability and can also include physical capacities such as passenger, payload, towing capacity, cargo capacity, ground clearance, and published footprint.
- `performance` stores published results rather than fixed physical specs and can include acceleration, top speed, and torque in addition to efficiency, range, and emissions.
- `costOfOwnership` is separate from performance and captures longer-horizon ownership estimates such as ten-year energy and maintenance cost.
- `safety` is separate from compliance and models comparable safety capabilities rather than commercial package names.
- `compliance` is intentionally separate so certification and regulatory data do not get mixed with measured performance results.

See also [spec/v0.1/readme.md](../../spec/v0.1/readme.md).
