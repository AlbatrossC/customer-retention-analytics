#!/usr/bin/env python3
"""
Run batch Model 2 inference on a JSONL file.

Usage:
    python scripts/run_batch.py --input data/model2_inputs.jsonl --output data/model2_outputs.jsonl
"""

import argparse
import json
import sys
from pathlib import Path

# Allow running from repo root
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.inference.engine import Model2Engine


def main():
    parser = argparse.ArgumentParser(
        description="Run Model 2 batch inference on a JSONL file."
    )
    parser.add_argument(
        "--input", required=True, help="Path to input JSONL file."
    )
    parser.add_argument(
        "--output", required=True, help="Path to write output JSONL file."
    )
    parser.add_argument(
        "--id-column", default="case_id",
        help="Name of the stable identifier column (default: case_id)."
    )
    parser.add_argument(
        "--adapter-path", default=None,
        help="Override adapter path (default: from config)."
    )
    parser.add_argument(
        "--no-4bit", action="store_true",
        help="Disable 4-bit quantization."
    )
    args = parser.parse_args()

    # Initialize engine
    engine_kwargs = {"load_in_4bit": not args.no_4bit}
    if args.adapter_path:
        engine_kwargs["adapter_path"] = args.adapter_path

    print("Loading model...", file=sys.stderr)
    engine = Model2Engine(**engine_kwargs)
    print("Model loaded. Starting batch inference...", file=sys.stderr)

    summary = engine.predict_batch(
        input_path=args.input,
        output_path=args.output,
        id_column=args.id_column,
    )

    print("\nBatch inference complete.", file=sys.stderr)
    print(json.dumps(summary, indent=2), file=sys.stderr)

    engine.unload()


if __name__ == "__main__":
    main()
