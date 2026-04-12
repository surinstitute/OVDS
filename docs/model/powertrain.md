# Powertrain Model

OVDS treats powertrain as a composition layer built around energy roles rather than a single engine field.

## Why

This supports internal combustion, mild hybrid, series hybrid, parallel hybrid, plug-in hybrid, battery electric, and fuel-cell electric vehicles without forcing all propulsion concepts into the same identifier.

## Composition

A vehicle powertrain can describe:

- one or more energy sources
- one or more energy storage components
- one or more energy converters
- one or more traction motors
- a drive layout

Each collection can identify a primary component where that matters.

## Roles

- `energySources`: fuels or supplied electricity available to the vehicle
- `energyStorage`: on-board storage such as battery packs
- `energyConverters`: components such as combustion engines or fuel-cell stacks that convert energy into usable propulsion energy
- `tractionMotors`: electric motors that directly provide wheel torque

This makes it possible to describe a vehicle with electric wheel propulsion that obtains its energy from a gasoline-powered generator.

## Architecture Semantics

OVDS distinguishes electrification levels explicitly instead of treating every partially electrified vehicle as the same kind of hybrid.

- `ice`: no traction battery and no electric traction path are implied.
- `mild_hybrid`: electrified combustion vehicle with electrical assist, regeneration, or restart support, but not a guaranteed electric-only drive mode.
- `parallel_hybrid`: combustion and electric propulsion can both contribute mechanically to wheel drive.
- `power_split_hybrid`: full-hybrid architecture with a power-split device or equivalent arrangement that blends combustion and electric drive roles.
- `plug_in_hybrid`: hybrid vehicle with external charging and published electric driving capability.
- `series_hybrid`: electric-drive vehicle where the combustion engine primarily generates electricity rather than directly serving as the main wheel-driving path.
- `battery_electric`: wheel propulsion is electric and the vehicle relies on grid charging rather than onboard combustion.
- `fuel_cell_electric`: wheel propulsion is electric and onboard hydrogen conversion supplies propulsion energy.

This means a MHEV belongs to the broader electrified-vehicle family, but OVDS does not treat it as interchangeable with a HEV or PHEV.

## Reusable Entities

The following technical entities are defined as reusable schemas:

- [Engine](../schemas/engine.md)
- [Electric motor](../schemas/electric-motor.md)
- [Battery pack](../schemas/battery-pack.md)

Fuel-cell stacks are intentionally not a standalone schema yet. The vehicle schema keeps a reserved `fuelCellStackId` reference so that entity can be added later without reworking the powertrain model.

## Current Scope

In v0.1, the vehicle schema stores role-based powertrain usage references inside the vehicle record. The reusable entities themselves live in their own schemas under `spec/v0.1/`.
