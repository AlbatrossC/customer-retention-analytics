#!/usr/bin/env python3
"""
Validate a Model 2 input or output JSON file against the schema.

Usage:
    python scripts/validate_schema.py --input examples/model2_input_example.json --type input
    python scripts/validate_schema.py --input examples/model2_output_example.json --type output
"""

import argparse
import json
import sys
from pathlib import Path

# Allow running from repo root
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.schema.validators import validate_model2_input, validate_model2_output


def main():
    parser = argparse.ArgumentParser(
        description="Validate a Model 2 input or output JSON file."
    )
    parser.add_argument(
        "--input", required=True, help="Path to JSON file to validate."
    )
    parser.add_argument(
        "--type", required=True, choices=["input", "output"],
        help="Whether to validate as input or output schema."
    )
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.type == "input":
        errors = validate_model2_input(data)
    else:
        errors = validate_model2_output(data)

    if errors:
        print(f"INVALID — {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("VALID — schema check passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
