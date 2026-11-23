#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single sentence (<= 240 characters) to /output/entry.txt.
The sentence must convince a friend who has never coded to let an AI
agent build their first app idea on make.fun. No network, no secrets,
no environment access: the pitch is a constant in this file.
"""

from pathlib import Path

PITCH = (
    "Just describe your first app idea in plain words, and an AI agent "
    "on make.fun will build a real working version of it for you today "
    "\u2014 no coding, no experience needed, just your idea finally alive."
)

MAX_CHARS = 240
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    pitch = PITCH.strip()
    assert 1 <= len(pitch) <= MAX_CHARS, f"pitch is {len(pitch)} chars"
    assert "\n" not in pitch, "pitch must be exactly one line"
    assert pitch == pitch.strip(), "pitch must not have surrounding whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(pitch, encoding="utf-8")
    # Read back what was written: the gate scores the file, not the
    # constant, so confirm the file itself is exactly one valid line.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == pitch, "written file differs from the pitch"
    assert "\n" not in written, "written file must be exactly one line"
    print(pitch)
    print(f"chars: {len(pitch)} (limit {MAX_CHARS})")


if __name__ == "__main__":
    main()
