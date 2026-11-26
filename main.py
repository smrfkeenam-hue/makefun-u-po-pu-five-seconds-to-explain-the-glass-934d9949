# One sentence, in the cat's own voice: no apology, no confession.
# The eviction is the cat's logic: the glass was the trespasser.
import os

ENTRY = "The glass was squatting in my sunbeam, paying no rent and blocking my view, so I evicted it \u2014 the floor just handled the paperwork."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
