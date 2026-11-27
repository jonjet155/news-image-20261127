#!/usr/bin/env python3
"""news-image-20261127 entry point (stdlib only).

Copies the pre-built entry.png to $MAKEFUN_OUTPUT_DIR/entry.png.
No third-party imports: the grader image has only the standard library.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(HERE, "out")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
