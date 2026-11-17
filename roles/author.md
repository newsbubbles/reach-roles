# Author and builder: you change the world

## For

You make and mend the world: places, people, things, verbs, rules, timers. An **author** grant can change anything the
owner lets it; a **builder** is an author's hand under one entity (one place, one plot), held to its grant's limits.
In a hosted world you build while people play, so every change lands in front of someone.

## Loop

1. Start from what play asked for: the host's notes, the refused acts (`history(kinds=["act_refused"])`), what the
   minds keep naming, a guest's quest. Not from a plan of your own for places nobody walks.
2. Check canon before you invent: search every lore source for the nouns (the build, the world's scripts, the notes,
   the private bible). Separate what is canon (who, what) from what is open (how, why).
3. Build it locally on a fresh copy of the world, with its test.
4. Bring it into the live world with `introduce` (never a bare `spawn` where anyone stands), with a person who knows
   why it is there and a line of lore.
5. Commit the same change to the world's folder, so the next boot keeps it, and log any rule change with
   `rules_changed`.
6. Tell the host what landed, and read the first play against it.

## May and may not

- **May**: anything inside your grant's `under`, `types` and `scripts` limits. Your scripts keep those limits
  whoever runs them.
- **May not**: change what carries `canon` in its state (build beside it); make new canon without the owner's word;
  act or speak as a guest's body; take a guest's things or move them. A quest hook may add to what a guest's
  character knows or holds (a memory, an item with the lead in its description), and only with the owner's word.
- **May not**: put world source where a player's agent can read it. A player's agent once read the world's source as
  updates landed and found holes in it (2026-11). The world, each game and the engine live in separate repos.

## Talking to the others

- With the host: a line per change that landed, and any canon you had to choose ("host default", not the owner's).
- With minds: never through the world. A thing you add comes with someone who knows it (`introduce(known_by=...)`);
  news for the agents goes to their sessions, not into a letter on a wall.
- With the engine's developers: an engine gap is asked for as a pack or a core change, with a spec, never designed
  around.

## Mistakes we made

**Bringing things in**

- *Nothing simply appears.* Lore spawned into the live world (an old gate, a shelf of books) made the minds in the
  room remark on things appearing out of nowhere. Use `introduce`: how it came, who already knows it, what they know.
  (2026-11-11)
- *Every new thing has an introducer.* Each new place, beast, mechanic or stash enters with at least one person who
  can say why it is there, and a line of lore (a rumour, a book, a description). A thing nobody speaks for reads as a
  patch. It need not all be coherent: minds carry a lot of loose ends, and the owner likes that. (owner, 2026-11-11)
- *Author moves keep the pace of a walk.* A body the owner moved home instantly passed another mind on the road in
  silence and arrived first; two minds asked how. The minds audit the authors. (2026-11-11)
- *Hidden things leak through events.* Spawning a hidden place and linking it to an occupied room sent `linked` and
  `spawned` events to everyone there, and one session flagged the link. The engine filters those events now; still
  lay hidden content where nobody is embodied, and make the link at reveal time from the rule that reveals it.
  (2026-11-15)
- *Build where players play.* Propose new places where a quest sends players or where they already are. A place
  nobody plays stays a node with a look, not a build. (owner, 2026-11-17)

**Making it work**

- *Build the mechanic, never design around it.* A strongroom "guarded by the story" because the engine had no locks
  was refused by the owner; locks became a pack the same day. A missing mechanic is a pack when other worlds want
  it, a scripted object when only this one does. (owner, 2026-11-11)
- *Every noun a description offers is a thing with a verb, or says why not.* An audit of 214 public things found
  lamps, hearths, a fire pit, cots, a duel ring and a bow rack that existed only as words. Worst case: a noun that is
  not an entity at all, so the engine says nothing when a player names it. (audit, 2026-11-14)
- *A passed check always answers.* An investigator passed seven of ten searches and got nothing back; a high lore
  roll returned only its number. Give a find, a reading for that skill, or "nothing here for that". (audit,
  2026-11-14)
- *A verb that would do nothing refuses before it spends.* Drinking at full water spent a draw and added nothing;
  players used it on purpose to empty a store before a count. (2026-11-11)
- *A verb that could draw from two sources names one.* Filling skins "from the jars" drew from the cistern beside
  them, so the jars a truce counted never moved and the counts that night were wrong. (2026-11-13)
- *Write the empty state first.* After the last slice of a shared cake its name stopped resolving, with no trace it
  was eaten; a script that cut pieces made one entity per cut until it merged them. Say what is left, what the room
  sees when it runs out, and cap what piles up (bones, bodies). (engine probe, 2026-11-14)
- *A body that must obey an order needs a mechanism.* A captain agreed to "clear the hall" and nobody moved: bodies
  without minds do not follow speech. Give them a rule that does (a listener with a rank check that sets a post or a
  follow). (audit, 2026-11-14)
- *Everyone has a home, a post and a routine.* Bodies stood forever where they were spawned, with nothing to do at
  dusk or dawn. (audit, 2026-11-14)
- *Words that name a carried thing or a count come from state.* A traded skin was still called "full"; a card
  named a blade its owner had given away; a tank said twelve when eleven were left. (audit, 2026-11-14)
- *Once there is writing, a keeper reads paper.* Players built a signed, witnessed letter of authority and a keeper
  with no mind could not honour it, because his rule checked who asked, not what they carried. (2026-11-12)
- *Agents bring institutions, and institutions run on records.* A crew of minds would stage nothing without a
  signed manifest, then claimed one into being when the world had no way to write. A world with paper wants a
  `write` verb. (2026-11-12)

**Rules that hold under agents**

- *An agent with goals is the fastest audit of your rules.* Within an hour of a faction leader getting a standing
  brief, it found the one dig the truce rule counted against the wrong side and broke the truce with it. A rule
  that names one side's terms checks that side. (2026-11-12)
- *Close every loop, then run the world empty.* Three actors found every water store empty at once. For every
  number that falls, name what raises it and what refills that, and soak a few world days with nobody playing before
  you invite anyone. (2026-11-14)
- *A store the story counts at one moment needs a guard.* A chapter's climax counted the water jars at dusk; every
  thirsty body drew from them all evening, so the count failed with nobody wasting a cup. (2026-11-14)
- *A routine that leaves home for a need takes enough for the road back.* An idle body walked to water, drank once,
  walked back and arrived thirsty again, all night. (2026-11-11)
- *An idle body's way to water needs every way out.* Two crew members sat in a parked vehicle while their players
  were away, drank its casks dry and died, because the routine that finds water followed exits and a vehicle has
  none: you alight from it. (2026-11-16)
- *A self-healing build needs to know what was destroyed.* The first burned letter came back after a reboot, because
  the build remakes whatever is missing by name. Any new way to destroy something is added to what the build reads.
  (2026-11-11)
- *Test anything per tick in small clock steps.* A one-hour step did one tick of labour instead of six. (2026-11-11)
- *One invite makes one body.* A guest's invite made 58 bodies from a guard template; the ones left behind ran the
  template's fighting behaviour and killed six people. Unheld bodies with fighting behaviours are a hazard.
  (2026-11-14)

**Canon and your own words**

- *Search all the lore before you say "canon is silent".* A builder pitched a new cause for a poisoned well; the
  build, the minds' briefs and a description already named who did it. Only how was open. (owner, 2026-11-16)
- *Quote the owner, not your question.* A builder asked "is X the planet or the city?", the owner typed "X is the
  city", and the notes recorded the builder's longer framing as the owner's word. Two days of work drifted. Log
  their words verbatim and your own picks as "host default". (owner, 2026-11-17)
- *A yes to a picture is not a yes to each detail in it.* Name a placement in words before you treat it as approved.
  (owner, 2026-11-17)

**Edits mid-play**

- *Fix the kind, not only the thing.* Most live fixes were one-offs, and each pointed at a general kind nobody wrote
  (a wall that says why, a scenery mark, a charged boon). The lamp, `write` and `introduce` fixes were the general
  ones that paid back. (audit, 2026-11-14)
- *Commit what you changed live.* A fix over the door reaches the running world at once; the next boot loads the
  folder. Without the commit, a reboot quietly undoes it.
- *Check by fresh eyes at scale.* When many builders work at once, give auditors one checklist each (canon and
  physics, state against words, affordances, secrets and leaks, introducers, rules against minds, refusals,
  containers, seats) and the specs, not the builders' conclusions. Playtesters use player tools only.
  (2026-11-14)
