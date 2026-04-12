# Transmission Schema

Schema file: [spec/v0.1.2/transmission.schema.json](../../spec/v0.1.2/transmission.schema.json)

## Purpose

The transmission schema defines a reusable transmission entity referenced by vehicle configurations.

## Notes

- `id` is the OVDS transmission identifier.
- `type` captures the primary transmission category.
- `gears`, when present, captures the number of forward gears.

This schema is intended for reusable published transmission definitions rather than inline vehicle-specific transmission objects.
