#!/usr/bin/env python3
"""Cutest Cat entry for make.fun's "Draw the cutest cat" bounty.

The program writes one picture of a cat to /output/entry.png. The picture
is the cat.png file shipped beside this program; copying it byte-for-byte
keeps every run identical with no network access.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "cat.png"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # The run is only valid if the copy is complete: the output must be
    # byte-for-byte the picture this program ships.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("entry.png incomplete: size differs from cat.png")
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
