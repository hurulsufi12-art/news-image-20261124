"""Write the finished 24 Nov 2026 news image to the output directory.

Entry for the make.fun bounty "news-image-20261124": one 1024x1024
infographic summing up Tuesday 24 November 2026 in six verified stories.
The picture is pre-rendered and shipped beside this file as entry.png;
this program only copies those exact bytes to the output path, so both
grader runs produce identical output. Python standard library only:
no image library, no network, no other file read, no logging.
"""
import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"


def _same_bytes(a, b):
    """True only when two files hold exactly the same bytes."""
    with open(a, "rb") as fa, open(b, "rb") as fb:
        while True:
            ca, cb = fa.read(65536), fb.read(65536)
            if ca != cb:
                return False
            if not ca:
                return True


def verify_copy(source, target):
    """True only when the copied bytes are exactly the shipped image."""
    return source.is_file() and target.is_file() and _same_bytes(source, target)


def output_path():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir, out_dir / IMAGE_NAME


def run():
    here = Path(__file__).resolve().parent
    source = here / IMAGE_NAME
    if not source.is_file():
        print("error: shipped image missing: " + str(source), file=sys.stderr)
        return 1
    out_dir, target = output_path()
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    if not verify_copy(source, target):
        print("error: copied image differs from shipped image", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
