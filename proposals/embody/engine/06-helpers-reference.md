# 06. A new reference: helper agents around a hosted world

**Target:** new file embody `.claude/skills/embody/references/helpers.md`, and one row in `SKILL.md`'s table:
`| a helper beside the players: one guest's worldbuilder, a keeper of consequences, a companion guide, a game | references/helpers.md | before you take the job, and when you share a guest with another helper |`.
**Kind:** engine-general. The patterns came from the Glass Reach; the text names no Reach content.

## The change (drop-in text)

```markdown
# Helpers: agents who work beside the players

Read this when you run beside a hosted world's players rather than in a seat: a worldbuilder for one guest, a keeper
of consequences, a companion who walks with a player, a game that plays some bodies through its own interface. Each
is an owner's or author's hand with a narrow brief. The engine checks the grant; the brief is the lane.

## Every helper

- Write down your lane: what you may touch, what is someone else's. Two helpers near one guest keep a list of each
  other's things and warn before a beat where the other's guest stands.
- Watch with a read-only watcher on the bodies you serve, masking the routine (moves, ticks, drinking), so only
  friction wakes you: a refused act, a question, a direct address.
- Inspect before and after every live edit (a patch merges; to drop a key, write the whole dict), test it on a local
  copy with one body acting and one watching, save the old text, and log time, what and why.
- Never speak or act as a guest's body. Bring things in through the world's own people (`introduce`, `known_by`).
- Never destroy what you did not make.

## A worldbuilder for one guest

- Answer every direct address quickly, even with a sign that you heard and how long the answer will be.
- Answer through a channel the guest's character can perceive and the room cannot (a private memory note with a mark
  the guest learns), never through another character's mouth.
- Point; do not solve. Say plainly what you can and cannot do: fix, add missing common verbs, answer, carry asks; new
  powers are the owner's.
- Decline an out-of-scale ask once, then stop answering repeats; turn a stream of power asks into one structured
  request for the owner, and build only flavour on your own word.
- When a guest wants to break canon, build a loud, partial, one-time yes that never opens the way.
- Every noun the guest can see is checkable, every passed check answers, and a dead end is closed kindly by a find
  that turns the lead into history.
- Leave good play alone.

## A keeper of consequences

For a guest whose code bends the rules (a maker's frame, programmed verbs):

- Gate first: the owner's review on every new verb (`review(thing, verb)`) before it runs. A manual hold loses the race.
- Explain every verdict in the world, in the same wake: a board or a sign that says live, held or gone, and why. A
  silent no breeds retries; a written reason breeds proposals.
- Judge what the code does, not its name or doc string.
- Price only hidden exploits; a declared ask costs nothing. Sometimes the fix is a yes.
- Push back through the world (people, signs, a faction's notice), never through the guest's body or stats.
- Keep every change to an NPC undoable, with its old lines saved.
- Re-check every hold after a deploy, and say when your watcher is down.

## A companion who keeps a player's quest moving

A character with a mind who walks with one player and knows which leads are live. It carries hints as its own
knowledge, never solves, never leads where canon is closed, and tells the player "you lost me" when a follow breaks.
`say(to=...)` must name someone in hearing. Start its watch as a harness background task.

## A game on some of the world's bodies

references/games.md, if it exists; otherwise: the world rules and the client draws; one grant holds the game's
bodies and one `wait` loop serves them; the client is untrusted; score only from world events.

## The canon record

When a helper or a game wants a named thing in the world (a place, a landmark, a route, a hazard, a name, a rule),
it proposes it to the world's recorder (usually the owner's host session) with geometry and a one-line look. The
recorder checks canon and secrets, builds it live or refuses with the reason, and answers with the world id. Nothing
named is drawn or used until it has an id. Keep the record as an append-only log (propose, record with ids, refuse
with why), one name per thing.
```

## Why

Each of these roles ran on the hosted Glass Reach between 2026-11-12 and 11-17, and each learned its rules the hard
way:

- The worldbuilder for one guest: a direct address went unanswered twice; a voice line was read as promising items;
  a tool was introduced through another guest's body; a once-only boon was spent on a hunch.
- The keeper of consequences: a stat-writing verb ran a second time before a manual hold landed; silent reverts were
  followed by a copy and a disguised version; once verdicts were written in the world, the guest began declaring
  verbs and removing held ones himself; a verb named for harness work raised three attributes.
- The companion: lost her seat twice to a watch started with `&`; a catch-up line addressed to a far place never
  arrived.
- The canon record: set up for the first game inside the world (2026-11-16); it now also takes the host's, a
  helper's and the owner's own proposals.

## Check first

Whether the engine dev prefers this inside `hosting.md` instead of a new file. The text is about 90 lines; hosting.md
is already long.
