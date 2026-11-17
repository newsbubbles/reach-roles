# 04. Author: before you host, the affordance pass

**Target:** embody `.claude/skills/embody/references/author.md`, one new bullet after "Build what the speech
names" (and, if the engine dev agrees, a matching `embody audit` linter later).
**Kind:** engine-general.

## The change

```markdown
- Before you host, and after every big build, run the affordance pass: every noun a description offers a player (a
  lamp, a hearth, a rack, a door, a carving) is a thing with a verb, or carries a refusal in the world's words, or is
  rewritten out of the description; a noun that is no entity at all is the worst case, because the engine says
  nothing when a player names it. Every passed check answers something (a find, a reading, "nothing here for that
  skill"). Every tool you place names the verb it enables and something that answers it. Write the empty state before
  the full one (what the room sees when the last piece goes, what is left, a cap on what piles up). A body that must
  obey an order needs a rule that moves it: people without minds do not follow speech. Everyone has a home, a post
  and a routine. Test arrival rules with real walks (`go`), never author moves, which fire them differently.
```

## Why

From a read-only audit of the Glass Reach on world days 17 to 19 (2026-11-14), five slices:

- 214 public entities: lamps, hearths, a fire pit, cots, a duel ring and a bow rack existed only as words, and a
  `lamp` kind existed in the engine with none placed.
- An investigator passed seven of ten searches and got nothing; a high lore roll returned only its number.
- A found plumb had no use until a `measure` verb was added.
- In an engine probe, eight slices of a cake became eight entities until a merge line was added, and after the last
  slice the name stopped resolving with no trace it was eaten.
- A captain agreed to "clear the hall" and nobody moved: in every play log.
- No person had a home or a bed; bodies stood where they were spawned.
- An angel's sense rule looked broken under author moves and worked when the test walked (2026-11-15).

## Check first

Whether the engine dev would rather ship the deterministic checker the audit drafted (`embody audit`: inert nouns,
spent things, homeless bodies, duplicates, piles). Then this bullet can be one line pointing at it.
