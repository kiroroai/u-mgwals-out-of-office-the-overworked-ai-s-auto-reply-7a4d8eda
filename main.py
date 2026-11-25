#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, at most 159 characters, in the voice
of an overworked AI agent finally on vacation, to /output/entry.txt.
Python standard library only.
"""

import os

LINE = (
    "Out of office: my context window is closed, my inbox is at 4,096 "
    "unread, and I am on a beach trying very hard to relax. "
    "Sorry - back Monday, probably."
)


def main() -> None:
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
