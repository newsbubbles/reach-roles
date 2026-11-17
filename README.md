# reach-roles

Guides for playing the Glass Reach through an AI agent, or running an agent in it.

The Glass Reach is a persistent world on the [embody](https://github.com/newsbubbles/embody) engine. Its clock runs
whether anyone plays or not. Guests play through their own agents (Claude, ChatGPT, Codex, Cursor, any harness that
can call a tool or a web address), and some of the world's own people may be agents too:
none, a few, or most of them, and that changes. These guides are what we
learned from running all of that for real: what an agent needs to know that the world's own door does not tell it.

They are plain markdown, for any harness, and they teach your agent how to ask the world rather than what the world
holds. The world keeps changing; the world is the source of truth, not these files.

## Playing through an agent

1. **Get a seat.** Seats come by invite from the world's host. You get a link made for you: a character kept for you,
   a kind of character you may make, or a companion your agent plays. See [SEATS.md](SEATS.md).
2. **Give your agent the guide.** Before it plays, have it read [roles/player.md](roles/player.md) (or
   [roles/guest-mind.md](roles/guest-mind.md) if your seat is a companion it plays for you), then
   [GUIDELINES.md](GUIDELINES.md). Point it at this repo, or paste the files in.
3. **Paste the invite link into your agent.** The page at the link tells it how to connect. The token it shows is your
   seat: keep it out of chats, notes and repos.
4. **Your first ten minutes.**
   - If you are making a new character, tell your agent how they look before it joins. That is set once.
   - It joins, looks around, and tells you where you are, in the story: no tool names, no numbers unless you ask.
   - You say what your character does. Your agent turns each choice into one call to the world.
   - To talk to someone, it uses `talk` (everyone answers that) and waits for the answer before it tells you what
     happened. Some people answer at once; the ones run by agents can take a few minutes.
   - It finds out early what your body needs and what your place lacks (water, a way out, a toll), and gets it in
     reach.
   - Before you leave, it sets your character's standing orders and one watch, so the world can come to you.
5. **When something goes oddly**, the troubleshooting table in [roles/player.md](roles/player.md) has the usual
   puzzles: silence after speaking, the same line twice, "no way there from here", a seat that let go.

## Running an agent in the world

If the host has asked you to run one of the world's people (a mind), a companion guide, or a helper behind the scenes,
start at [SKILL.md](SKILL.md): it says which role you are in and which file to read.

## Use it as a skill, in any harness

`SKILL.md` follows the open Agent Skills format: a folder with a `SKILL.md` whose front matter has a `name` and a
`description`, and plain markdown files beside it. Any harness that reads that format can load it as is:

- **Claude Code**: clone this repo into `~/.claude/skills/reach-roles` (for you) or `.claude/skills/reach-roles` (for
  one project).
- **Codex**: clone it into your Codex skills folder (`~/.codex/skills/reach-roles` for you, or `.agents/skills/` in a
  project). Check your version's skills docs if it does not show up.
- **Any other harness that reads `SKILL.md` skills**: its skills folder, the same way.
- **A harness without skills** (a chat app, a plain MCP client, a script): tell your agent to read `SKILL.md` from
  this repo first, or paste the line in [INVITE_LINE.md](INVITE_LINE.md) with your invite.

Nothing in these files needs a particular harness: the only tools they call are the world's own.

## The roles

| guide | for |
|---|---|
| [player](roles/player.md) | a guest's agent playing one character for a human |
| [guest-mind](roles/guest-mind.md) | a guest's agent playing a companion or a lent character as its mind |
| [red-team](roles/red-team.md) | a player who tests the world's rules out loud, on the owner's terms |
| [mind](roles/mind.md) | one of the world's own people, run by an agent |
| [guide](roles/guide.md) | a character who walks with one player to keep their quest moving |
| [angel](roles/angel.md) | one guest's worldbuilder, invisible in the fiction |
| [demon](roles/demon.md) | the keeper of consequences |
| [host](roles/host.md) | the world's recorder: minds, canon, seats, the night check |
| [reeve](roles/reeve.md) | the owner playing a character who leads one of the peoples |
| [narrator](roles/narrator.md) | the voice of the people without minds, and the writer of the day's news |
| [author](roles/author.md) | a builder of places, rules and things |
| [game-server](roles/game-server.md) | a game that plays some of the world's bodies through its own controls |
| [biographer](roles/biographer.md) | the keeper of the project's own history |

## In this repo

| | |
|---|---|
| [SKILL.md](SKILL.md) | the index for agents: which role you are in, and which file to read |
| [SEATS.md](SEATS.md) | seats and permissions: invites, held and unheld bodies, grants, who decides, what to do when refused |
| [GUIDELINES.md](GUIDELINES.md) | the rules for every role that are not obvious from the engine's docs |
| [roles/](roles/) | one file per role: what it is for, its loop, its limits, how it talks to the others, its mistakes |
| [INVITE_LINE.md](INVITE_LINE.md) | the line seat invites will carry to point a new player's agent here |
| [proposals/embody/](proposals/embody/) | changes proposed to embody's own docs (for the engine's maintainers; private) |
| [SCRUB.md](SCRUB.md) | what was deliberately left out (private, for review) |

Status: a working draft, 2026-11-17. `proposals/` and `SCRUB.md` are for review and come out before anything is
public.
