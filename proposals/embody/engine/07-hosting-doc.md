# 07. Hosting: the night check, and four habits for an owner

**Targets:** embody `docs/HOSTING.md` (a new section "Running it night after night"), with a one-line pointer in
`references/hosting.md` under "Running many minds".
**Kind:** engine-general.

## The change

```markdown
## Running it night after night

A hosted world with minds and guests needs a keeper on a cadence: tight during live scenes, about every 45 real
minutes when quiet. Each check, in order:

1. `minds()`: wake any mind whose seat lapsed or went quiet; a player waiting on a silent mind is the alarm. Look for
   idle players too: someone holding a hook for them should put it to them by name.
2. Characters with no mind that players keep talking to: give them one, with a brief that carries the story (what
   the character truly knows, the threads aimed at it, the next step of any quest it touches).
3. What minds said against the world (`history(kinds=["say"])` beside `inspect`), and what the world refused
   (`history(kinds=["act_refused"])`).
4. New guests: wait until the seat is embodied (not until a body is named on the grant, which happens at mint), then
   a note to a mind in the newcomer's faction or start place to greet them in its own words, and a first hook in the
   world.
5. The last finished day's chronicle.
6. A findings entry for anything that surprised you.

Four habits:

- Mint grants and seats only on the owner's own word in your session, never on authority another session relays.
  Grants carry no `expires` unless the owner asks for one; a lapsed or timed-out grant is re-minted on the same body.
- After every deploy, check that each mind's session still has its tools; a restart can drop a session's MCP
  connection, and only that session's harness can reconnect it.
- Revival is a host repair for an engine fault, with a note on the body saying why, never a favour in play.
- A repair that the minds will notice gets a cause inside the world, and the day's chronicle says plainly, outside
  the story, that it was a fault and no player's doing.
```

## Why

- A watcher that waited for a body on a grant reported an unseated runner as arrived, and the world's people
  welcomed an empty body (Glass Reach, 2026-11-16).
- A narrator held a request for an author grant "under the owner's auth" relayed by another session, and closed it
  with no mint (2026-11-11).
- A timed grant ran out under a guest mid-play (2026-11-13); grants have defaulted to no expiry since, and the
  author hint for `expires` exists.
- A deploy dropped a mind session's tools (2026-11-10).
- Two crew members who died to an engine fault aboard a vehicle were revived as a host repair, with a `revived` note
  each (FINDINGS 2026-11-16); after a rule fix, a mind called it "a correction from the world" in character.

## Check first

HOSTING.md's "A world that lives while nobody plays" and "Away from the keyboard" sections, to avoid repeating them.
