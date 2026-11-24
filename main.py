#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

Deterministic, no network, no randomness, no LLM calls.
Writes the entry sentence to /output/entry.txt
(or $ENTRY_OUTPUT_DIR/entry.txt when set) and prints it.
"""

import os
from pathlib import Path

ENTRY = "The lift mirror shows me leaving before I have pressed the button, and for a moment I am not sure which of us is going home."


def main() -> None:
    # Self-check gate: fail loudly if the entry is invalid.
    assert ENTRY.strip(), "entry must not be blank"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    ENTRY.encode("utf-8")  # must be valid UTF-8 text

    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY + "\n", encoding="utf-8")
    # Verify the write: read it back and confirm it matches exactly.
    assert out_path.read_text(encoding="utf-8") == ENTRY + "\n", "written entry does not match ENTRY"
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()
