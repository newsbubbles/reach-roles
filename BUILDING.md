# Building a world with a team of agents

For a world's owner, and the agent who leads building for them: how to divide world-building work between agents so
that it goes fast and still holds together. For one builder's own loop, see [roles/author.md](roles/author.md). For
writing code into the world, [PROGRAMMING.md](PROGRAMMING.md).

> **Your seat must be: owner, or a builder or author grant with the owner's brief.** The engine fences what each seat
> can write (`principals()` shows yours). The fence stops a builder writing outside its part of the world; it does not
> stop a builder inventing canon. That part is the lead's gate.

## Principles

1. **Determinism first.** Everything that can be a rule, a table, a schedule or a formula is one. Minds go where
   judgment matters: the few people players will really talk to. A model that improvises rules drifts toward agreeing
   with whoever is talking; a rule says the same thing to everyone.
2. **Big to small.** Each layer is decided and written down before the layer under it starts, and each layer's output
   is the next layer's brief.
3. **One owner per file, one fence per seat.** Each agent writes only its own files, or only inside the part of the
   world its seat is fenced to, so parallel work never collides.
4. **Every claim is checkable.** A description that mentions a thing has that thing. A thing that looks usable has a
   verb, or a refusal that says why not and what would work. A number in a line matches the state.
5. **Hidden until the story gets there.** New ground is laid hidden, away from where anyone stands, and linked when
   it is revealed. Every reveal has an introducer: a person, a scene or a find that explains it in the world.
6. **Build where players play.** A place no one visits is cost with no story. Grow the world outward from where
   players already are, by the threads they pull. (owner, 2026-11-17)

## The layers

| layer | what it decides | who | model tier |
|---|---|---|---|
| **Bible** | the canon digest for this build: facts, names, tone, physics (sky, climate, water), economy, who knows what, open questions with their defaults | the lead | top |
| **Frame** | the shape: areas, landmarks, ways between them, heights, coordinates in the world's frame, how it joins what exists | a surveyor, the lead reviews | mid |
| **Systems** | water, power, transit and schedules, markets and money, labour, law and watch, machines, crowds, news: each with its state, rules, verbs, events and numbers, and which pack does it (or the engine ask if none does) | a systems engineer | top |
| **Areas** | per area: places, things with verbs, finds, residents, the crowd, hooks, all consistent with the layers above | one builder per area, in parallel | mid |
| **People** | named minds (few, with briefs that carry story goals), residents (tables and routines), passer-by templates | a people writer | mid; top for named minds |
| **Wiring** | the scripts and rules that make it run on its own, with tests | the systems engineer | top |
| **Audit** | fresh-context review against the checklists below | auditors | mid or top |
| **Playtest** | players with player tools only, walking a task list on a copy | playtesters | small or mid |
| **Install and reveal** | hidden install, the reveal plan, the players' changelog entry, minds seated | the lead | top |

Tiers are named by capability, not product: *top* is the strongest you have, *mid* is good at following a spec,
*small* is cheap, for playing and checking. Code is written at the top tier.

Each layer has a gate: the lead reads its output against the bible before the next layer starts. A failure goes back
to the layer that owns it, never patched by the next one.

## Two ways to divide the work

- **Spec files.** Builders write data files (places, people, systems) that an installer reads. Only the lead writes
  live, with an idempotent installer (everything by name, so a rerun never makes a second copy), after the audit
  passes and a local test runs. Safest; slowest.
- **Fenced seats.** Each builder gets its own builder seat fenced to its part of the world (`invite("builder",
  limits={"under": <entity>})`) and writes live inside it, all of it hidden until the reveal. Auditors and playtesters
  read through observer seats fenced the same way. Faster, and the fence does the "one owner per file" job. The bible
  and the lead's gate still decide canon. (owner, 2026-11-16)

Either way: seats carry no end date, are minted on the owner's word, are logged in the host's roster, and a builder's
seat is revoked when its gate passes.

## The standing roles

Besides the build team for a big piece, a world that runs for a long time keeps some builders on:

- **The host** keeps canon: a builder proposes a named thing (place, landmark, route, hazard, name, rule) with its
  geometry and look, the host checks it against canon and secrets, builds it or refuses with the reason, and answers
  with the world id. One name, one thing. ([roles/host.md](roles/host.md))
- **An angel** builds around one guest's play: their quests, small live edits where they stand, dead ends closed
  kindly. ([roles/angel.md](roles/angel.md))
- **A demon** keeps consequences: the cost of what a player did, told in the story.
  ([roles/demon.md](roles/demon.md))
- **A questwright** turns a player's ask for something to do into a proposal: premise, giver, stages that end on
  world events, the things to add, rewards through the world's own rules, ties to the larger story, what stays
  secret. The host checks it against canon and accepts it or sends it back; then the questwright builds it and the
  host introduces it through a person with a mind. This is the pattern we use by hand; it has no role file yet.

## Everyday things invite play

Some of the best builds are small: ordinary objects with a verb, left where people idle. A pair of dice to throw, a
deck, a flute, chalk for a wall, a board game scratched into a table. Nothing points anyone at them. Players and
minds find them, and what they make of them (a wager, a feud, a song) is play nobody wrote. When you add one, the verb
does the one thing the object does, everyone present sees it, and anything at stake is the players' own business,
made with the world's ordinary verbs. (owner, 2026-11-17)

## What every builder brief says

- Every noun a player can see has a verb that does something, or an honest refusal that names what would work.
- Dialog is topics with a fallback that points somewhere, never one line for everything. A person's words match the
  rule that guards the same thing.
- Nothing in a description promises what the engine will not do.
- Each place gives a stranger a reason to come and a reason to leave toward somewhere else.
- Test each piece on a copy with two newcomers, one acting and one watching, including the refusal path. After each
  live change, inspect the state; never trust the reply.
- Ask the lead before inventing canon the bible leaves open.
- Report what you made, what you could not decide and what you assumed.

## The audits

Each is its own reviewer with fresh context, given the specs and not the builders' conclusions. Every item is
something that went wrong once.

- **Canon and physics:** names, dates, distances, who knows what; the sun sets where the map says; nothing contradicts
  the bible. Search every source of lore before calling canon silent: the build, the scripts, the briefs, the notes.
- **State against words:** every description, dialog line and notice matches its state, including after scripts move
  things.
- **Affordances:** everything that looks usable has a verb or an explaining refusal; natural verbs players will try
  (help, search, climb, swim) have a home or an answer.
- **Lived-in detail:** real props, wear, labels, materials; no generic rooms.
- **Voices:** no stock lines repeated across topics; no fourth-wall lines; every resident can answer the obvious
  questions about their own work.
- **Secrets and leaks:** codes and quest ends never in public text or descriptions; hidden things leave no trace in
  events players see; private canon stays private.
- **Numbers:** prices, wages, water, capacities and timings add up over a day and a week. Run the world's own soak
  test: a new person with a body has to live through it too.
- **Counts that other rules use:** a new person of a faction can change a rule that counts that faction. Check what
  counts heads before you add one.
- **Layout:** coordinates inside the frame, no overlaps, routes connect what they say.
- **Introducers:** every new place, person and system has someone or something in the world that explains it.
- **Rules against minds:** where a mind and a rule guard the same thing, they agree.
- **Refusals:** each names the real reason and what would work, and none says something false.
- **Promises:** no description shows what the engine will not do.
- **Ways to open:** every lock, code or puzzle has a way players can learn in the world, or says plainly why no hand
  opens it.
- **Pull:** every crew and kind of player is called by name by something; hooks spread across players, not all toward
  one.
- **Seats:** no grant with an end date; every mind seated after install.
- **Submitted code and text** from anyone outside the owner's team: reviewed before it runs, after deterministic
  checks for links, contact details and payment asks.

## Scale

Simulate only where players are: places wake when someone is in or next to them, and catch up in one step when someone
arrives. Split the world into *fields* (sky, climate, crowd density, seasonal prices: functions of place and time,
cheap and the same everywhere) and *entities* (people and things with state, changed only where someone acts). Crowds
are place state; passers-by are made from templates when spoken to, and become real when players come back to them.

## Mistakes we made

- *Author moves do not fire arrival rules the way a walk does.* Test arrivals with real walks on the copy. (angel log)
- *A spawn announces itself.* Making a hidden thing where people stood told them it was there. (host log, 2026-11-15)
- *A new person broke a count.* A new keeper of one faction filled a slot in a rule that counted that faction's
  guards, and a guard was never made. The world's own tests caught it before it shipped. (host log, 2026-11-17)
- *A new post with no water.* Two new keepers stood where nothing to drink was in reach; the week-long soak showed
  them going thirsty. (host log, 2026-11-17)
- *A deploy ships what is committed.* A build change left uncommitted missed the deploy it was meant for. (host log,
  2026-11-17)
