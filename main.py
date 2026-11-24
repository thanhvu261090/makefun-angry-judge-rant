"""Angry Judge: The Short Rant Contest — a one-line rant about a printer.

Writes the rant to /output/entry.txt after checking it against the
competition gate: 1 to 400 characters, not only whitespace, one line.
"""

from pathlib import Path

MAX_CHARS = 400
OUTPUT_PATH = Path("/output/entry.txt")

RANT = (
    "My printer only jams when the deadline is real. Ten blank pages? "
    "Flawless. One page, due in five minutes? It swallows the paper whole, "
    "blinks an error light I have never seen in my life, and prints a test "
    "page in a "
    "language I do not speak. I have replaced the ink twice. The ink was "
    "never the problem. The problem is a machine that can smell fear — "
    "and it is laughing at me in 300 dpi."
)


def check_rant(text: str) -> None:
    """Raise ValueError if the rant breaks any gate rule."""
    if not text or not text.strip():
        raise ValueError("rant must not be blank")
    if text != text.strip():
        raise ValueError("rant must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("rant must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"rant is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    check_rant(RANT)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(RANT, encoding="utf-8")
    print(f"Wrote {len(RANT)} characters to {OUTPUT_PATH}")
    print(RANT)


if __name__ == "__main__":
    main()
