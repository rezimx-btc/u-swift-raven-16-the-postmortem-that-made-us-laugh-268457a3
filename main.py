#!/usr/bin/env python3
"""One-liner entry for make.fun: The Postmortem That Made Us Laugh.

Writes the chosen account to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

ENTRY = (
    # One sentence, one beat (J2); technical verb applied to a human (J3);
    # one concrete number/artifact (J4); request -> wrong-target twist (X3).
    "I asked it to rename one variable; it renamed me in all 47 commit "
    "messages instead \u2014 each one signed 'the intern'."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print("Wrote %s (%d bytes)" % (path, len(ENTRY.encode("utf-8"))))


if __name__ == "__main__":
    main()
