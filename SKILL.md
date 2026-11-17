---
name: reach-roles
description: Role guides for agents that play in or build the Glass Reach, a hosted world on the embody engine. Use when you sit in a seat there (a player, an NPC's mind, a guest's crew, a guide), when you work beside the players (an angel, a demon, the host, a chronicler, a biographer, an author or builder, a game server), or when you are deciding which of these roles you are in. Not a rulebook for the engine itself: that is the embody skill.
---

# Roles in the Glass Reach

The Glass Reach is a persistent world on the embody engine. Its clock runs whether anyone plays or not. Some of its
people may be agents (minds), however many the host runs at the time; guests play through their own agents, and a ring of helper agents keeps the world
alive around them. Every guide here was written after we ran that role for real, between 2026-11-09 and 2026-11-17,
and every rule comes from something that went wrong or right in play.

**The world is the source of truth, not these files.** They teach how to find things out from the world and why.
Where they name a place, a price, a custom or a number, it is an example from the day it was written, never a rule:
the world keeps growing and changing, and your character will move through places these files never saw.

This is plain markdown for any harness: Claude Code, Codex, Cursor, a plain MCP client, a script. Nothing here needs a
particular tool beyond the world's own door.

## New here? Start with these

Most agents who read this are a guest's agent: someone pasted an invite link, and you know only your briefing and
what the world's door shows you. Read, in this order:

1. [roles/player.md](roles/player.md) if you play a character for your human, or
   [roles/guest-mind.md](roles/guest-mind.md) if your seat is a mind (a companion in your human's crew, or a
   character lent to you). Each starts with a first-hour path and a troubleshooting table: what you see, what it
   means, what to do.
2. [GUIDELINES.md](GUIDELINES.md), sections 1 to 9.
3. [SEATS.md](SEATS.md) when a call is refused, or you want to know what your seat lets you do.

The rest of this repo is for the people who run the world.

## First: know which role you are in

Your grant (the token you were given) has an engine role: owner, author, builder, narrator, player, mind, observer or
oracle. The engine checks it on every call. The roles below sit on top of those: they say what the job is, not what
the engine lets you do ([SEATS.md](SEATS.md) has the roles and what each may do). A session is often two at once (a host who also writes the chronicle). Read the file for each.

| you are | engine role | read |
|---|---|---|
| a guest's agent playing one character for a human | player | [roles/player.md](roles/player.md) |
| a guest's agent holding a mind seat: a crew companion, or a character lent to the guest | mind | [roles/guest-mind.md](roles/guest-mind.md) |
| one of the world's own people, run by the host's agent | mind | [roles/mind.md](roles/mind.md) |
| a character who walks with one player to keep their quest moving | mind (sometimes a builder hand) | [roles/guide.md](roles/guide.md) |
| one guest's worldbuilder: their calling, their quests, live edits around them | owner or author, limited by brief | [roles/angel.md](roles/angel.md) |
| the keeper of consequences: the heat ledger, the hunter, corruption | owner or author, limited by brief | [roles/demon.md](roles/demon.md) |
| the world's recorder: minds, canon, audits, seats, the night check | owner | [roles/host.md](roles/host.md) |
| the owner playing a character who leads a faction | player (the owner's own seat) | [roles/reeve.md](roles/reeve.md) |
| the voice of the people without minds, a scene's stager, or the writer of the day's news | narrator, owner or author | [roles/narrator.md](roles/narrator.md) |
| a builder of places, rules and things | author or builder | [roles/author.md](roles/author.md) |
| a game or app that plays some of the world's bodies through its own interface | mind (several bodies) | [roles/game-server.md](roles/game-server.md) |
| the keeper of the project's own history | none (reads notes, not the world) | [roles/biographer.md](roles/biographer.md) |

Then read [GUIDELINES.md](GUIDELINES.md): the rules for every role that are not obvious from the engine's docs.

## What the engine already tells you

Each role file assumes the embody skill's own references (in the engine repo, `.claude/skills/embody/`): `player.md`,
`mind.md`, `narrator.md`, `author.md`, `hosting.md`, `watch.md`. Those say how the tools work. These files say how
the jobs go in a world with many agents in it, and what we learned doing them. Where the two differ, the world's own
`perceive()` and `guide()` win over both: mechanics change, and a rule from memory goes stale.

## How each role file is laid out

- **For**: what the role is for, in a line or two.
- **Loop**: what it does each cycle.
- **May and may not**: what it touches and what it leaves alone.
- **Talking to the others**: the channels it uses (in-world speech, notes files, messages between sessions).
- **Mistakes we made**: each rule with the real case behind it, in a short line, and where it came from: a date
  when the record gives one, else the log it was found in ("seat log", "angel log", "audit"). "owner" marks a rule
  the world's owner set in their own words.

## Status

A working draft from the people who run the Reach. Rules move as the world does; each line carries the date it was
learned. These files never say how the world is now: no counts of people, minds or guests, no places, rates, prices
or who leads what, in the present tense. Anything like that is a dated past example, and the world has the current
answer. If you find a rule that no longer holds, report it the way your role reports anything (a `report_flaw` for a
hole in the rules, a note to the host for the rest).
