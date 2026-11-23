"""Hire Me In One Line — make.fun entry program.

Writes one sentence — the pitch — to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Self-validates against the contest gate (UTF-8 text,
1-200 characters, not only whitespace, a single sentence on one line)
before and after an atomic write, and fails loudly on any breach.
"""

import os
import sys
import tempfile

ENTRY = "I turn the 200 emails you dread into the five decisions you need to make."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError if text breaches the contest gate."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, gate requires "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Exactly one sentence: one terminal full stop, at the end, no others.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def validate_bytes(data: bytes) -> str:
    """Strictly decode bytes as UTF-8, then run the text gate on them.

    (Calling .encode() on a str can never fail, so the byte-level check is
    the one that actually proves the file on disk is valid UTF-8.)
    """
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"entry is not valid UTF-8: {exc}") from exc
    validate(text)
    return text


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    validate(ENTRY)

    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")

    # Atomic write: temp file in the same directory, then replace.
    fd, tmp_path = tempfile.mkstemp(
        dir=out_dir, prefix=".entry-", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
            fh.write(ENTRY)
        with open(tmp_path, "rb") as fh:
            written = validate_bytes(fh.read())
        if written != ENTRY:
            raise ValueError("written text does not match the entry")
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

    # Verify the final file on disk, as the grader will read it.
    with open(target, "rb") as fh:
        final = validate_bytes(fh.read())
    if final != ENTRY:
        print("error: final entry.txt does not match the entry", file=sys.stderr)
        return 1

    print(f"wrote {target} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
