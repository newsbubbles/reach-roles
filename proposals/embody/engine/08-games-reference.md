# 08. A new reference: games inside a world

**Target:** new file embody `.claude/skills/embody/references/games.md`, and a row in `SKILL.md`.
**Kind:** engine-general. **Needs Nate's yes first**: the private `embody-games` skill says its proven rules move into
the embody skill as `references/games.md` only when Nate agrees, since that repo is shared.

## The change

Move the world-facing rules of the `embody-games` skill (the client and 3D lessons stay in that skill):

```markdown
# Games: an interface onto a slice of a world

Read this when you build a game, an app or a client that plays some of a world's bodies through its own controls.

- The world rules; the client draws. Every change goes through the ops and comes back as the events any agent sees.
  The client animates and decorates; it never decides an outcome or owns state the world does not have.
- The client is untrusted. Enforce what matters in the engine (a body's verb list, what it perceives, cooldowns) and
  again on the game's server (speed and range clamps, a message budget, one seat per browser, a cap per address).
- One grant holds the game's bodies (a mind grant may name several). The server hands out seats with its own cap and
  queue; a body nobody plays goes back to its routines.
- Decisions, not frames: a place change, a spot when a body stops, discrete actions; one `wait` loop for the game.
- Seats follow the real population: only bodies whose taking does not distort the world. Death is real.
- A body that cannot understand speech gets the speaker and the tone, never the words, or its player is a spy.
- Anything that touches another body has a cooldown and the same dice as everyone.
- Balance is a world decision: a predator, a new seat kind, an action on people goes to the owner.
- Score only from world events, so the score is history.
- Write down the contract: every state key, verb and event kind the game reads. Watch `rules_notice`; test against a
  fresh build of the world.
- A named thing the game draws must exist in the world first (references/helpers.md, "The canon record").
- Its own repo. The game's view of the world is the door, never the world's files.
```

## Why

Ridge Kid (2026-11-16), the first game inside the Glass Reach, settled each of these with the Reach's host and the
owner, and the engine shipped the pieces it needed (beast hearing, a verb allowlist per body, cooldowns, `step`, a
read-only event feed).
