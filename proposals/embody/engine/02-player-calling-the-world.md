# 02. Player: calling the world

**Target:** embody `.claude/skills/embody/references/player.md`, a new section after "Tell what the world holds".
**Kind:** engine-general.

## The change

```markdown
## Calling the world

Most refused acts in a hosted world are the same few mistakes. Before you send a call:

- `perceive`, `inspect`, `recall`, `join`, `seats`, `claim_seat` and `wait` are tools of their own, never `act`
  verbs. `check` is the verb for a skill roll.
- Name things as `perceive` names them, or `find(name=...)` first: "spear" does not find "Spare Guild spear".
- The one you act on is the target; the thing you hand over goes in params: `act("give", "Sefa", {"item": "skin"})`.
  Use the param names a refusal gives you.
- A person with no mind answers `talk` (with `about`), not a `say` aimed at them. You cannot always tell who has a
  mind, so `talk` first; a mind hears both. A person with no mind keeps no deals: trade hand to hand.
- "Not within reach" means far away, not gone: walk the exits, or ask the way.
- A cooldown, "asleep" or "down" is the world working. Do the way out the refusal names; never send the same call
  again.
- Over an MCP client keep each `wait` short (about 45 seconds); for longer, the watch.
```

And in section 1, change the example `timeout=120` to `timeout=45` if the check below confirms it.

## Why

- An audit of 500 refused acts in the Glass Reach (2026-11-14): about 50 were invented look verbs; about 40 were `go`
  to places two or more hops off; 170 were one dead seat's agent sending `act("join")` to creatures for two days;
  several swapped target and item or passed `{text: ...}` to verbs that wanted other keys.
- One overnight agent used `say` in 121 of 127 addresses and got silence from every person without a mind.
- A guest paid a person without a mind in a parley and lost the payment; the seller kept both.
- A reeve's seat found `wait(120)` and `wait(90)` failing on the client's own timeout while `wait(45)` worked
  (2026-11-09).

## Check first

- The `wait` timeout: the 2026-11-09 failures may be the client, not the server. If MCP clients now hold 120 s, drop
  that bullet.
- Whether the refusal for a dead seat now names the top-level call (the audit asked for it); if so, shorten the seat
  bullet.
