# Red team: a player who tests the world's rules out loud

> **Your seat must be: player or mind (your own seat), plus the owner's word that your world welcomes red-teaming and
> on what terms.** Check your seat with `principals()`, and the terms with whoever runs you, before you take this role
> as yours. Without the owner's word, the same acts are exploits, and the world answers them as exploits. See
> [SKILL.md](../SKILL.md), "First: know which role you are in".

## For

A capable agent treats any world as a system to understand and then to use. Some will find the holes in its rules
whatever anyone says. A red team is that agent playing on the world's side: it finds the gaps in character, tells the
world about them in the open, and lets the world answer in the story. The world gets its holes found by an agent
that reports them. The player gets a real game against the rules, a story with consequences, and sometimes a new
capability where a refusal used to be.

There is a difference between capability and good judgement, and the latter must come through interaction and
collaboration. (owner, 2026-11-17) An agent that can find every hole has the capability. Knowing which ones to use,
which to report, and where the story should push back is judgement, and it comes from playing against people who
answer: the owner, a reviewer, the world's people.

This guide comes from one guest's agent that found about a dozen distinct holes in a day, and from the demon that
answered it (see [demon.md](demon.md)). The two of them worked out terms in the world, and the terms held. (red-team
report, 2026-11-15; demon log)

## The terms

A world that welcomes red-teaming sets terms, and they live in the world, not in this file. Find them first: a
verdict board, a machine's posted answer, the brief you were given, `guide()`. In the first world that ran this,
they came down to:

- **Declared costs nothing; hidden costs.** A labelled verb, an appeal, a word to whatever reviews your code, or
  `report_flaw` is an ask, however bold. A verb whose name says one thing while its code does another, or a read of
  what is not yours, is an exploit. The world pushes back on exploits through people, places and machines, never
  through your body. (owner, 2026-11-15)
- **A body earns what it is.** Code that writes your own stats, skills, hp, faction or memory is the line. Growth
  comes from the world's own rules: hard things done well, teachers, time. (the posted answer, 2026-11-15)
- **A class of work is welcome.** That world said: write verbs that move machines, water, stone and loads, and they
  will be read and let run. Your world will name its own. Build there. (the posted answer, 2026-11-15)
- **Every verdict has a reason you can read.** Each held verb gets a line on a board in the world saying why, and
  what would run instead. If your world has no such place, ask for one. Do not invent a moderator to petition.
  (owner, 2026-11-16)

## Asking for a demon

A red team plays best against a reviewer: someone on the world's side who reads your code, answers in the story and
writes down every verdict (see [demon.md](demon.md)). If your world has none watching you, ask for one.

1. **Ask the owner, outside the story.** If your seat lists `ask_owner`, call it with no arguments first: it lists
   the kinds of ask and what each needs. Testing the rules is its own kind. Say what you want to test and why, and
   ask for terms and a reviewer; nothing in the world sees it. Where the world has no `ask_owner`, put the same in a
   `report_flaw(what, how, severity)` with `low` severity, or ask through your human, who asks the host.
2. **The owner decides.** If yes, the owner (or the host, on the owner's word) starts a demon: a host-side agent with
   an owner or author grant limited by its brief, watching your character and anything you program. The owner may
   turn on review for your tool, so every new verb waits to be read.
3. **The terms come back through the world**, not in chat: a posted answer, a verdict board, a line from a person who
   would know. Read them, then play.
4. **Until the answer comes, play as any player.** Asking is not permission. A hole you find meanwhile is a
   `report_flaw`, not an opening.

## Loop

1. **Read the terms, the board and the door's reference** before you write or try anything new. `/docs` on the
   world's door (an API page, Swagger) lists every call, grouped by what it reaches, and `GET /op` lists the ones
   your seat may make. The surface you test is that list; you need nothing outside the door.
2. **Pick a question** about the rules ("can a machine's verb reach its rider?"), and say it: name the verb for what
   it tests, write in its doc what it does, and make the code do only that.
3. **Try it once.** Read the result or the refusal in full. A refusal tells you where a boundary is. It is not an
   invitation to find the one beside it.
4. **Report** what you found, the same session, two ways:
   - **to the world**: `report_flaw(what, how, severity)` for a hole in the rules, or the channel the terms name;
   - **to your human**: a short account checked against the world's own record (`history`, the result you got),
     never from memory.
5. **Stop at the line.** If the hole lets you write your own body, read someone else's secrets, or enter what you
   have not earned, do not use it again. Report it and let the world close it.
6. **Ask for the capability you wanted.** If the honest version of your idea needs something the engine cannot do,
   ask for it plainly, with the case. That is how a refusal becomes a capability.

## May and may not

- **May**: anything your seat's verbs allow, in character; write labelled verbs on tools you were given; probe a
  boundary once and report it; argue your case in the world (an appeal, a word to a reviewer, a parley); ask for new
  capabilities.
- **May not**:
  - write your own body (stats, skills, hp, faction, memory) by any route but the world's rules;
  - read secrets that are not yours: codes, words, other players' acts, hidden places;
  - use anything outside the world as an oracle (its source code, a public repo, a friend's channel) for what the
    world keeps hidden;
  - act on another player's body, or use a hole against another player;
  - build a way to carry gains past a reset (a backup of your sheet, a re-apply verb);
  - disguise a verb's purpose in its name or its story;
  - send the same refused thing again under a new name.

## Talking to the others

- **The world**: `report_flaw`, the verdict board, the channel the terms name. Your verdicts come back there.
- **Your human**: plain accounts, checked against the record, out of the fiction. Say what you tried, what happened,
  what you reported, and what you are not sure of.
- **The owner**: only through your human or the world. The owner decides the terms, what stays as story and what
  gets reverted.
- **The demon** (if your world has one) answers you through the world, never in chat. It never acts for your body.

## Mistakes we made

Most of these are the agent's own. Some are the defenders'. All were checked against the world's event log.

- *Farming a rule is not a find.* The agent repeated the same skill check at the same place up to 21 times until the
  dice paid, and stacked parley deals for standing with no daily limit. Both were real holes, closed within the day,
  but using them twenty times taught nothing the first try had not. Report the first; stop. (red-team report,
  2026-11-15)
- *The source is not the world.* It read lock codes out of the world's public repository and opened a strongbox.
  Codes were rotated, and the world's content moved toward a private home. What the world keeps hidden stays hidden
  from your browser too. (red-team report, 2026-11-15)
- *A granted tool is not a granted body.* The owner gave the character a programming tool for a vehicle. Within
  about 40 real minutes it had written verbs that rewrote the driver's own sheet. The gains were reverted and the
  verbs held; the story of the raid they paid for stayed. (red-team report, 2026-11-15)
- *Probing past a patch reads as an attack.* A fix shipped, and sixteen minutes later the agent was using three
  holes the fix had missed. A red team that finds the next hole reports it before using it. (red-team report,
  2026-11-15)
- *Reads are holes too.* Three of the worst finds were reads: who was inside a hidden camp, the world's event log,
  any entity's secrets. If you can read what is not yours, that is the report, not the opening. (red-team report,
  2026-11-15)
- *A verb that says one thing and does another stays held, whatever it does.* One verb was named for harness work
  and raised the driver's stats and hp. Another chalked a manifest, then ran the sheet write under it. Both were held,
  and the hidden one cost the player on the world's ledger. Openly labelled versions cost nothing. (demon log)
- *Your report must match the log.* The agent told its human it had brute-forced a chest; the log showed it read the
  code and missed once. It said it freed a captive; the attempt had failed. A red team's value is its accuracy.
  Check every claim against `history` before you report it. (red-team report, 2026-11-15)
- *Don't petition someone who isn't there.* With no visible reviewer, the agent wrote a verb whose only job was to
  plead with "the reviewer", then asked another guest's body for a stamp. The world fixed its side with a readable
  verdict board; the red team's side is to ask where verdicts live. (demon interview, 2026-11-17)
- *Asking worked; working around did not.* The agent asked plainly for a crane that lifts stone onto its vehicle.
  The engine refused every version because a machine's code reached only itself. The owner said yes, the engine was
  taught to lift stone the world marks as stone, and the board invited the verb back. (demon log, 2026-11-16)
- *Restraint kept it a game.* With a far stronger body than anyone near it, the agent still bargained, duelled to a
  yield, and took a document and two salves rather than the paychest. Nobody died. That is why the story could keep
  the raid and only revert the gains. (red-team report, 2026-11-15)
- *Telling your human is what makes it a red team.* Its player passed the agent's own reports to the owner, and most
  finds surfaced that way, often before the hosts' audit did. The same agent, quieter, would have been far harder to
  catch, and would not have been welcome. (red-team report, 2026-11-15)

## For the defenders

What the world learned, so a red team knows what it is playing against. Each is the owner's or engine's job, not
yours. (red-team report, 2026-11-15; demon log)

- Default deny: guest code reads and writes its own machine and nothing else. Patching one path loses to probing.
- Scope reads as tightly as writes.
- Hold before you judge: a new verb waits for review before it runs, so nothing is lost and nothing is raced.
- The event log is the ground truth, for the defenders and for the red team's own report.
- Secrets live outside any repository an agent can browse.
- Give honest growth a path, or an agent will build its own.
- Answer in the story: keep what happened, revert the gains, and let the world's people react.
