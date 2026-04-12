# Engine Schema

Schema file: [spec/v0.1.1/engine.schema.json](../../spec/v0.1.1/engine.schema.json)

## Purpose

The engine schema defines a reusable internal combustion engine entity.

## Current Scope

The v0.1.1 schema currently captures a minimal but reusable engine record:

- engine identifier
- primary fuel type
- displacement
- published engine power in kilowatts
- cylinder count
- aspiration
- layout

This schema is intended to be referenced by vehicles, generations, variants, or future fitment/application records.

Use this schema for component-level engine characteristics. Vehicle-level combined or published system output should stay in the vehicle `performance.power` block.
