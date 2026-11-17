# Proposals for embody's docs and skill

For the Embody Engine Dev session, which owns the embody repo. Nothing here has been applied. Each file names its target,
the change (as drop-in text where it is text), why (the real cases), and what to check first.

Already landed, so not proposed again: the mind-lessons op fixes (watch checked when armed, `to_me()` narrowed, ids
refused in `say`, `minds()`), hidden author events filtered, `act_as`/`say_as` refused on a guest-held body, idle
bodies stepping off vehicles for water.

## Engine-general (true of any embody world)

| file | target | in short |
|---|---|---|
| [engine/01-skill-rules-for-every-role.md](engine/01-skill-rules-for-every-role.md) | `.claude/skills/embody/SKILL.md` | three rules every role needs: seeing is not knowing, nobody acts for a guest's body, two channels |
| [engine/02-player-calling-the-world.md](engine/02-player-calling-the-world.md) | `references/player.md` | the refused-act audit's top mistakes as a short "calling the world" section; the `wait` timeout |
| [engine/03-mind-small-additions.md](engine/03-mind-small-additions.md) | `references/mind.md` | hooks put by name, empty seats, tasks that involve others, `&` watches, tool output is not knowledge |
| [engine/04-author-before-you-host.md](engine/04-author-before-you-host.md) | `references/author.md` | the affordance pass: nouns, passed checks, empty states, obeying bodies, homes, walks in tests |
| [engine/05-narrator-hand.md](engine/05-narrator-hand.md) | `references/narrator.md` | the hands-off list, re-read before staging, improvisations need state |
| [engine/06-helpers-reference.md](engine/06-helpers-reference.md) | new `references/helpers.md`, a row in `SKILL.md` | helper agents around a hosted world: per-guest worldbuilder, consequences, companion guide, lanes, the canon record |
| [engine/07-hosting-doc.md](engine/07-hosting-doc.md) | `docs/HOSTING.md`, `references/hosting.md` | the night check, minting on the owner's own word, revival only for faults, a new guest's first hour |
| [engine/08-games-reference.md](engine/08-games-reference.md) | new `references/games.md` (Nate's yes first) | the proven rules from the first game inside a world |
| [engine/09-findings.md](engine/09-findings.md) | `FINDINGS.md` | four findings from the role sessions not yet in the log |

## Reach-specific (not for the engine's docs)

| file | target | in short |
|---|---|---|
| [reach/01-where-reach-practice-lives.md](reach/01-where-reach-practice-lives.md) | the Reach's own repo when it moves out; the private mind skill meanwhile | temperaments, lies, patrols, grief, the heat ladder, the angel and demon lanes stay out of the public engine refs |

The rule behind the split (the owner, 2026-11-13): content practice never goes in the public embody references, which
are general engine docs. A Reach habit once went into `mind.md` and was taken out again.
