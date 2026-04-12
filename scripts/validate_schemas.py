import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import ValidationError
from jsonschema.validators import validator_for
from referencing import Registry, Resource


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_files(spec_dir: Path) -> list[Path]:
    return sorted(spec_dir.rglob("*.schema.json"))


def build_registry(paths: list[Path]) -> tuple[dict[str, Any], Registry]:
    schemas_by_id: dict[str, Any] = {}
    resources: list[tuple[str, Resource[Any]]] = []

    for path in paths:
        schema = load_json(path)
        schema_id = schema.get("$id")

        if not isinstance(schema_id, str) or not schema_id:
            raise ValueError(f"Schema is missing a valid $id: {path}")

        schemas_by_id[schema_id] = schema
        resources.append((schema_id, Resource.from_contents(schema)))

    return schemas_by_id, Registry().with_resources(resources)


def validate_schemas(schemas_by_id: dict[str, Any]) -> None:
    for schema_id, schema in schemas_by_id.items():
        validator_for(schema).check_schema(schema)
        print(f"OK schema  {schema_id}")


def format_path(parts: list[Any]) -> str:
    if not parts:
        return "$"

    formatted: list[str] = ["$"]
    for part in parts:
        if isinstance(part, int):
            formatted.append(f"[{part}]")
        else:
            formatted.append(f".{part}")
    return "".join(formatted)


def validate_instance(instance_path: Path, schema: Any, registry: Registry) -> None:
    validator_cls = validator_for(schema)
    validator = validator_cls(schema, registry=registry)
    instance = load_json(instance_path)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))

    if not errors:
        print(f"OK instance {instance_path}")
        return

    print(f"FAIL instance {instance_path}")
    for error in errors:
        print(f"  - {format_path(list(error.path))}: {error.message}")
    raise ValidationError(f"Instance validation failed: {instance_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate OVDS JSON Schemas and optional JSON instances."
    )
    parser.add_argument(
        "--spec-dir",
        default="spec",
        help="Directory containing versioned OVDS schemas. Defaults to spec.",
    )
    parser.add_argument(
        "--schema-id",
        help="Schema $id to use when validating one or more JSON instances.",
    )
    parser.add_argument(
        "--instance",
        action="append",
        default=[],
        help="Path to a JSON document to validate against --schema-id. Repeatable.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    spec_dir = Path(args.spec_dir)

    if not spec_dir.exists():
        print(f"Spec directory does not exist: {spec_dir}", file=sys.stderr)
        return 1

    paths = schema_files(spec_dir)
    if not paths:
        print(f"No schema files found under: {spec_dir}", file=sys.stderr)
        return 1

    try:
        schemas_by_id, registry = build_registry(paths)
        validate_schemas(schemas_by_id)

        if args.instance:
            if not args.schema_id:
                print("--schema-id is required when using --instance", file=sys.stderr)
                return 1

            schema = schemas_by_id.get(args.schema_id)
            if schema is None:
                print(f"Schema not found for $id: {args.schema_id}", file=sys.stderr)
                return 1

            for instance in args.instance:
                validate_instance(Path(instance), schema, registry)
        elif args.schema_id:
            print("--schema-id requires at least one --instance", file=sys.stderr)
            return 1
    except (OSError, ValueError, json.JSONDecodeError, ValidationError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())