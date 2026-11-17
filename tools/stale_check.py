"""Flag lines that state how the world is now. Run before every commit: python tools/stale_check.py

These guides teach an agent how to ask the world; they never say what the world holds. A count of people, minds,
guests or places, a rate or a price, or "currently/now/today" in the present tense goes stale and misleads every
agent that reads it. A number may appear only inside a dated past example: the same paragraph names a date
(2026-11-17) or the log it came from ("seat log", "audit", "interview").
"""
import pathlib
import re
import sys

NUM = r"(?:\d+(?:\.\d+)?|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|hundred|dozen|dozens)"
NOUN = r"(?:people|persons?|agents?|minds?|seats?|players?|guests?|npcs?|places?|houses?|factions?|peoples|bodies|tables|helpers|sessions)"
COUNT = re.compile(rf"\b(?:about|around|some|over|nearly|roughly)?\s*{NUM}\s+(?:of\s+(?:the|its|our)\s+(?:world'?s\s+)?)?{NOUN}\b", re.I)
NOWISH = re.compile(r"\b(?:currently|right now|at present|these days|as of today|so far)\b", re.I)
RATE = re.compile(r"\b\d+(?:\.\d+)?\s*(?:world |real )?(?:hours?|minutes?|days?|shards?|coins?|points?)\b\s+(?:per|every|a)\b", re.I)
DATED = re.compile(r"20\d\d-\d\d|\b(?:log|audit|interview|interviews|record|owner|draft)\)", re.I)
SKIP = {"SCRUB.md"}


def blocks(text):
    cur, start = [], 1
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip() or re.match(r"\s*(?:[-*]|\d+\.|\|)\s", line):
            if cur:
                yield start, "\n".join(cur)
            cur, start = ([line] if line.strip() else []), i
        else:
            cur.append(line)
    if cur:
        yield start, "\n".join(cur)


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    bad = 0
    for f in sorted(root.rglob("*.md")):
        rel = f.relative_to(root)
        if rel.parts[0] in {"proposals", ".git"} or f.name in SKIP:
            continue
        for start, block in blocks(f.read_text(encoding="utf-8")):
            dated = bool(DATED.search(block))
            for rx, why, needs_undated in ((COUNT, "count", True), (RATE, "rate", True), (NOWISH, "now-word", False)):
                for m in rx.finditer(block):
                    if needs_undated and dated:
                        continue
                    line = start + block[: m.start()].count("\n")
                    print(f"{rel}:{line}: {why}: {m.group(0).strip()!r}")
                    bad += 1
    print(f"{bad} flagged" if bad else "clean")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
