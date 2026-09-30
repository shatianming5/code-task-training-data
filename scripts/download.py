#!/usr/bin/env python3
"""Download a catalogued dataset from Hugging Face into ./data.

This repository does not rehost third-party rows. Each dataset stays under
its original license on Hugging Face.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "catalog.json").read_text())


def items() -> list[dict]:
    return list(CATALOG["rl"]) + list(CATALOG["sft"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_id", nargs="?", help="Hugging Face dataset id")
    parser.add_argument("--list", action="store_true", help="Print catalog ids")
    parser.add_argument("--out", default=str(ROOT / "data"), help="Download directory")
    args = parser.parse_args()

    if args.list:
        seen: set[str] = set()
        for row in items():
            if row["id"] in seen:
                continue
            seen.add(row["id"])
            print(f"{row['id']}\t{row.get('size')}\t{row.get('n_files')}\t{row.get('license')}\t{row.get('hf_url')}")
        return

    if not args.dataset_id:
        raise SystemExit("pass a dataset id, or --list")

    known = {row["id"] for row in items()}
    if args.dataset_id not in known:
        raise SystemExit(f"not in catalog: {args.dataset_id}")

    from huggingface_hub import snapshot_download

    dest = Path(args.out) / args.dataset_id.replace("/", "__")
    snapshot_download(
        repo_id=args.dataset_id,
        repo_type="dataset",
        local_dir=str(dest),
    )
    print(dest)


if __name__ == "__main__":
    main()
