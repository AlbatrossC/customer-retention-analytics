#!/usr/bin/env python3
"""
Run single-record Model 2 inference from a JSON file.

Usage:
    python scripts/run_inference.py --input examples/model2_input_example.json [--output result.json]
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
        description="Run Model 2 single-record inference."
    )
    parser.add_argument(
        "--input", required=True, help="Path to a JSON file containing one Model 2 input record."
    )
    parser.add_argument(
        "--output", default=None, help="Path to write the output JSON (default: stdout)."
    )
    parser.add_argument(
        "--adapter-path", default=None,
        help="Override adapter path (default: from config)."
    )
    parser.add_argument(
        "--no-4bit", action="store_true",
        help="Disable 4-bit quantization (uses more memory)."
    )
    args = parser.parse_args()

    # Load input
    with open(args.input, "r", encoding="utf-8") as f:
        case_input = json.load(f)

    # Initialize engine
    engine_kwargs = {"load_in_4bit": not args.no_4bit}
    if args.adapter_path:
        engine_kwargs["adapter_path"] = args.adapter_path

    print("Loading model...", file=sys.stderr)
    engine = Model2Engine(**engine_kwargs)
    print("Model loaded. Running inference...", file=sys.stderr)

    result = engine.predict(case_input)

    output_data = {
        "ok": result["ok"],
        "prediction": result["parsed"],
        "raw_text": result["raw_text"],
        "error": result["error"],
        "latency_s": round(result["latency_s"], 4),
    }

    output_json = json.dumps(output_data, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_json + "\n")
        print(f"Result written to {args.output}", file=sys.stderr)
    else:
        print(output_json)

    engine.unload()


if __name__ == "__main__":
    main()
