---
title: Electric Motor Schema
---

# Electric Motor Schema

Schema file: [spec/v0.2.0/electric-motor.schema.json](../../spec/v0.2.0/electric-motor.schema.json)

## Purpose

The electric motor schema defines a reusable traction motor entity.

## Current Scope

The v0.1 schema currently captures:

- motor identifier
- motor technology
- published motor power in kilowatts
- nominal position
- cooling type

This entity is designed to be reused across multiple vehicle records and future powertrain application models.

Use this schema for component-level electric motor characteristics. Vehicle-level combined or published system output should stay in the vehicle `performance.power` block.
