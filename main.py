#!/usr/bin/env python3
"""Entry for make.fun competition make-the-ai-judge-feel-awe-20261121-1600.

Writes one short original text to /output/entry.txt: a river turning a
stone smooth over a thousand years, in no hurry at all. The text is meant
to slow the reader down -- not by telling anyone to relax, but by showing
a slowness so old and so patient that hurrying next to it feels absurd.
The river has outlasted everyone who ever watched it, and will outlast
everyone reading this; the stone, meanwhile, is content to be shaped.
Nothing in the piece is an instruction, a wellness slogan, or a borrowed
meditation line: just water, stone, and deep time.

Deterministic: stdlib only, no network, no clock, no randomness. The
output directory honours the OUTPUT_DIR environment variable for local
testing and defaults to /output, the sandbox path the harness requires.
"""

import os
from pathlib import Path

TEXT = (
    "Somewhere, right now, a river is turning a stone smooth. "
    "It has been at it for a thousand years and is in no hurry to finish. "
    "The stone does not mind. The water does not mind. "
    "There is nothing to do here but notice how long forever actually takes."
)

MAX_CHARS = 280


def render() -> str:
    """Return the text normalised to exactly one trailing newline.

    The competition requires entry.txt to hold 1-280 characters
    (Unicode code points) and not be all whitespace; fail loudly
    instead of silently writing an entry the gate would reject.
    """
    text = TEXT.rstrip("\n") + "\n"
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be all whitespace")
    return text


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
