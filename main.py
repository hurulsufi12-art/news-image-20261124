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
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
