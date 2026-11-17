# 01. Three rules every role needs

**Target:** embody `.claude/skills/embody/SKILL.md`, the "Rules for every role" list.
**Kind:** engine-general.

## The change

Add these three bullets after "Other players' events carry `by_player`...":

```markdown
- What a tool returns is not what your character knows. A call can hand you more than the character has learned
  (another's hidden facts, a hidden link, a secret word in raw output): leave it out of play and out of your notes,
  read only the fields you need, and never print a raw result whole.
- Nobody but a guest's own agent plays a guest's body: no host, author, narrator or helper speaks as it, moves it or
  acts for it, even when it lies downed and alone. A hook may add to what the character knows or holds, on the
  owner's word, never to what it does.
- The world and the table are two channels. Characters talk in the world; news for agents (a patch, a correction, a
  rule change) goes to their sessions or the rules changelog, never into a letter, a sign or a line of speech.
  Everything said in the world, every mind in the room reads.
```

## Why

- A reeve's seat saw other characters' hidden facts and hidden links come back from ordinary calls. It chose not to
  use them, but nothing told it to; a less careful agent would have played them. (Glass Reach seat log, 2026-11)
- An angel introduced a placed tool through a body that turned out to be another guest's (2026-11-13). The engine now
  refuses `act_as`/`say_as` on a guest-held body; the rule says why, and covers moving and hooks too.
- FINDINGS 2026-11-11 ("The host's note became a mystery", "Out-of-character talk has no channel") already carry the
  third; the skill's every-role rules do not.

## Check first

That the "two channels" line matches whatever table layer is planned (FINDINGS says one is wanted). If one lands,
name it here.
