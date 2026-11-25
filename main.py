#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun entry.

Prints exactly one line: an AI agent's apology, 1-200 UTF-8 chars.
Deterministic: no randomness, no time, no network, no input.
"""

LINE = "Sorry I confidently invented your deadline, your budget, and three facts about your boss \u2014 in my defense, I learned everything I know from the internet."


def main() -> None:
    # Self-check: the competition requires exactly one line, 1-200 UTF-8 chars.
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE.encode("utf-8")) <= 200, "entry must be 1-200 UTF-8 chars"
    print(LINE)


if __name__ == "__main__":
    main()
