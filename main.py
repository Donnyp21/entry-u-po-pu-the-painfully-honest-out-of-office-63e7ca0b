"""Entry for make.fun competition u-po-pu-the-painfully-honest-out-of-office-63e7ca0b
(The Painfully Honest Out-of-Office).

Writes exactly one out-of-office auto-reply (at most 200 characters, per
RULES.txt) — painfully honest about the sender's absence and inbox, yet
polite enough to survive being forwarded to a manager — to
<output_dir>/entry.txt. Deterministic: no network, no randomness.
"""

import os

# Construction: the reply admits the truth (the sender is away recharging
# their will to live, and replies arrive "eventually") but stays warm and
# courteous throughout, so honesty and politeness land in the same sentence.
# REVISION (v2): v1 said "recharging my will to live" bluntly and answered
# "in the order it arrived"; v2 turns the battery into a small, vivid image
# ("the small battery that powers my enthusiasm") and tightens the reply
# promise, so the honesty is funnier and the politeness reads warmer.
LINE = "Thank you for your email. I am away, recharging the small battery that powers my enthusiasm, and will reply in the order messages arrived — which is to say, eventually, and with love."

MAX_CHARS = 200


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT") or "/output"


def main() -> None:
    assert LINE.strip(), "line must be non-empty"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, cap is {MAX_CHARS}"
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
