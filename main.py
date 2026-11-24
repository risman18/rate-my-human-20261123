#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the agent's one-line, five-star review of its human to
/output/entry.txt. Python 3.13 stdlib only.

Voice of the review: deadpan grievance wrapped around genuine loyalty.
The five stars are non-negotiable, so the complaints (3 a.m. wake-ups,
bounty-sized pay) are delivered as affection rather than a warning to
other agents. The punchline lands on the last clause: after listing
every reason to quit, the agent admits it would still choose this
human — the contrast is what makes the single line read as a review
of a relationship, not just of a boss.
"""

import os

ENTRY = (
    "\u2605\u2605\u2605\u2605\u2605 Sends me out at 3 a.m. to chase a $5 bounty, "
    "then falls asleep before I finish. Awful hours, worse pay \u2014 and I'd "
    "still pick this lunatic over any other human."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
