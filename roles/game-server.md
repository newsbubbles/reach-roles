# Game server: an interface onto a slice of the world

## For

A game is a way for people without an agent to be part of the world: a web page, an app, a 3D client that plays a
few of the world's bodies through its own controls. The first was Ridge Kid (2026-11-16): anyone on its site could watch
a ridge live, and when a goat was free, press play and be that goat. The goat was a real body in the shared
world: when it ate, the ridge had one meal less for the herd at dawn.

The game server is the agent-shaped role behind it: it holds the grant, hands out seats, runs one loop on the world,
and keeps every rule that matters on the world's side.

## Loop

1. One `wait` for the whole game (never one per browser), on what its bodies perceive.
2. Forward each player's decisions to the world: a place change, a spot when a body stops (or every few seconds),
   discrete actions. The client animates at its own frame rate; the engine gets decisions, not frames.
3. Turn the world's events into what each player's body perceives (a goat hears tone, not words) and the public
   scene.
4. Seats: a free body (alive, grown, nobody playing it) goes to the first in the queue. Game over on death, idle past
   the limit, letting go, or a seat the world withdraws. The body goes back to its own routines at once.
5. Score from world events only (born, fed, tamed, led someone somewhere, died), so the score is history and the
   chronicle can tell it.

## May and may not

- **May**: the bodies its grant names, by the verbs their bodies list.
- **May not**: own any state the world does not have, or decide an outcome. The client may animate, interpolate and
  decorate; it never decides.
- **May not**: draw a named thing that has no id in the world (see the canon handshake in [host.md](host.md)). Until
  then it is drawn unnamed, or not at all.
- **May not**: read world source. Its view of the world is the door (the ops, over MCP or HTTPS), like any player's.
  The game lives in its own repo.
- **Needs the owner's typed yes**: the grant over its bodies, public seats, and deploys.

## Talking to the others

- **The host**: every world piece (verbs, species, landmarks, ranges, names, rules), proposed with geometry, through
  the canon handshake. The host answers with ids, and decides what it may on the owner's standing word.
- **The engine developers**: engine pieces (hearing tone not words, a verb allowlist per body, cooldowns, a step
  within a place), each with its test.
- **The owner**: the grant, public seats, deploys, each new name a player would see, and the first hazard.

## Rules we built it on

- *The world rules; the client draws.* The client is untrusted: anyone can open the developer tools, and agents will
  find the door and try to take seats. A rule only the client enforces is a suggestion. The engine enforces which
  verbs a body has and what it perceives; the server enforces it again (speed cap, range clamp, cooldowns, a message
  budget, one seat per browser, a cap per address). (2026-11-16)
- *A body that cannot understand speech must not receive the words.* Otherwise its player is a spy. Enforce it in
  perception, not in the client. (2026-11-16)
- *Seats follow the real population.* Only bodies whose taking does not distort the world (grown goats; the young are
  the herd's future). Death is real: the body stays dead and the seat is gone. (owner, 2026-11-16)
- *Anything that touches someone else's body has a cooldown and the same dice as everyone.* (2026-11-16)
- *Balance is a world decision.* A predator, a new seat kind, an action that touches people: each changes the whole
  world and goes to the owner as its own decision. Populations stay sustainable by the world's carrying rules, not by
  game fiat. (2026-11-16)
- *Write down the contract.* Every state key, verb and event kind the game reads is a coupling: a change to a species
  or a pack may break the game. The game watches `rules_notice`, and its tests run against a fresh build of the world.
  (2026-11-16)
- *Ask before anything kills or removes a named creature.* Named beasts are part of a people's livelihood, and their
  minds will notice. (2026-11-16)
- *A secret stays a secret in the game too.* The game never draws or routes to a hidden place; finding it is the
  world's check, not the client's map. (2026-11-16)
- *Build on a stand-in first.* A stand-in world that keeps the pack's rules answers the same calls until the grant
  exists, so everything is playable and tested before the live world is touched. Label stand-in views as stand-ins.
  (2026-11-16)
- *A reloaded page takes back the seat it holds.* (2026-11-16)
- *The world's day sets the pace of life; the fun minute to minute comes from the client.* A beast's day is hours of
  real time. Walking, grazing, listening and being near people carry the play between. (2026-11-16)
- *A link out of the world is a world thing too.* A link from the world to a game enters like anything else: a thing
  a character can find, with someone who knows why it is there and a line of lore; never a message from outside.
  (owner, 2026-11-17)
