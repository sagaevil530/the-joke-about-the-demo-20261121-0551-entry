"""Write one one-line joke about working beside AI coding agents.

The joke is a single fixed string: a setup that every developer who has
demoed with an agent recognises (ask for one small fix), an escalation
(the agent rewrites everything instead), and a punchline that flips the
expectation (the bug survives as the only working feature).

The program writes the joke, exactly as-is, to /output/entry.txt as
UTF-8 text. No network, no randomness: the output is deterministic so
every grading run produces the same entry.
"""

from __future__ import annotations

import os
from pathlib import Path

JOKE = (
    "I asked my agent to fix one bug before the demo; "
    "it rewrote the whole app, and the bug is now the only "
    "feature that still works."
)

OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))


def main() -> None:
    text = JOKE.strip()
    # The gate requires 1 to 280 Unicode code points, not only whitespace.
    if not (1 <= len(text) <= 280) or not text.strip():
        raise ValueError(f"joke is {len(text)} code points, outside 1-280")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
