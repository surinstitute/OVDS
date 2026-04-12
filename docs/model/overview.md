# Data Model Overview

OVDS models a concrete vehicle configuration while keeping enough structure to avoid duplicating the same technical and commercial facts across years, generations, and variants.

## Core Hierarchy

1. Group
2. Make
3. Model
4. Generation
5. Model year
6. Variant
7. Vehicle configuration

The current v0.1 vehicle schema represents the final configuration and carries its commercial lineage in a dedicated `lineage` block.

Platform is modeled as a reusable cross-cutting architecture entity rather than a node strictly inside the commercial hierarchy, because one platform may span multiple makes or even multiple groups.

## Design Principles

- Keep commercial lineage separate from technical configuration.
- Keep shared architecture entities such as platforms reusable across makes.
- Reuse technical entities such as engines, electric motors, and battery packs across multiple vehicles.
- Preserve canonical SI measurements in the published vehicle record.
- Keep free-form attributes as an escape hatch rather than the primary modeling strategy.

## Main Documents

- [Vehicle schema](../schemas/vehicle.md)
- [Powertrain model](powertrain.md)
- [Version v0.1](../versions/v0.1.md)
