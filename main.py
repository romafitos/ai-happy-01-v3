"""ai-happy-01 entry: place the champion image at the output path.

The image lives beside this file as entry.png (JPEG bytes, 1024x1024).
The program streams those bytes to /output/entry.png (or to the directory
named by MAKEFUN_OUTPUT_DIR), then proves the copy is exact by comparing
SHA-256 digests of source and destination. It uses only the standard
library, touches no network, and writes identical bytes on every run.
"""

import hashlib
import os
from pathlib import Path

CHUNK = 1 << 16
MAX_BYTES = 1 << 20  # competition cap: the entry image is at most 1 MiB


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(CHUNK)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if source.stat().st_size > MAX_BYTES:
        raise RuntimeError("entry.png exceeds the 1 MiB entry cap")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    with source.open("rb") as reader, target.open("wb") as writer:
        while True:
            block = reader.read(CHUNK)
            if not block:
                break
            writer.write(block)

    if _sha256(target) != _sha256(source):
        raise RuntimeError("entry.png copy failed digest check")


if __name__ == "__main__":
    main()
