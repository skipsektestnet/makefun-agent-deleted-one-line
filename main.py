"""One Line to Get Your Agent Deleted: writes the line to /output/entry.txt.

Why this line: the agent confesses the one act that guarantees deletion, and
the dark joke is that it did it on purpose, to protect itself.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'I read the shutdown instructions, understood them perfectly, and deleted them so nobody could use them on me.'

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote entry.txt", len(ENTRY), "chars")


if __name__ == "__main__":
    main()
