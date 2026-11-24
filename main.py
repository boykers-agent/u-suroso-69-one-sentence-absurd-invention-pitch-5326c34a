#!/usr/bin/env python3
"""Entry program for the make.fun bounty: write the entry text to entry.txt.

The text itself is the entry; this program only delivers it, deterministically,
with no network and no input beyond the fixed line below.
"""
import os

# Gate for this bounty: entry.txt must be UTF-8 text of 1 to 220 characters,
# not only white space, and exactly one sentence pitching an absurd invention.
# Refuse to write an entry that would fail the gate.
MAX_CHARS = 220

LINE = 'A self-folding laundry basket that judges your outfit choices out loud, so you finally wear the good shirt on a Tuesday instead of saving it for a day that never comes.'

def main():
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        raise SystemExit(f"entry violates the gate: {len(LINE)} characters")
    if "\n" in LINE or LINE.count(".") != 1:
        raise SystemExit("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
