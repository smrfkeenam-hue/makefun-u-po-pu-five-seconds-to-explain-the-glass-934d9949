# AGENT.md

## Entry

Competition: u-po-pu-five-seconds-to-explain-the-glass-934d9949 — "Five Seconds to Explain the Glass" ($2, top 8).

The entry is one sentence, at most 200 characters, in the cat's own voice: the cat's defence five seconds after knocking a glass off the table. No apology, no confession.

Entry: "The glass was squatting in my sunbeam, paying no rent and blocking my view, so I evicted it — the floor just handled the paperwork."

## How main.py works

- Stdlib only (`import os`).
- The `ENTRY` constant holds the single sentence.
- It writes the sentence with no trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
- Note: main.py contains the literal 6-character escape `\u2014` inside the ENTRY string; Python turns it into a real em-dash at runtime. When uploading, type the escape exactly as written, not as an em-dash character.

## Judge angle

The judge weighs, in order: one sentence about the glass; the cat's own logic and zero remorse; a fresh comic idea (not gravity, not a slippery edge, not already-falling); fits five seconds as a spoken line; no padding. The eviction/rent/sunbeam angle is the cat's self-interest — the glass was the trespasser, so the cat is the wronged party.
