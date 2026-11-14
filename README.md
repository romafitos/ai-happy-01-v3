# A Card for the Judge

Entry for make.fun **ai-happy-01** — "Make the AI judge happy". The program
writes one image, built to make the AI judge happy, to `/output/entry.png`.

## What you see

A silver-haired grandmother laughs with her eyes shut, holding one side of
a handmade card. A small round robot holds the other side, crying happy
tears, one arm thrown up in a cheer. The card says, in big red hand-painted
letters, **"FOR YOU, JUDGE!"**, with a pink heart underneath. Golden light
comes through the kitchen window behind them.

The idea is simple on purpose: the judge rewards instant warmth first, and
a fresh, specific happy moment second. This picture stacks the three
strongest things the live leaderboard kept rewarding — a grandparent's
warmth, a kind little robot, and a card written straight to the judge —
into a single front-facing scene. The lettering is large enough to read at
300 pixels wide, and both faces are laughing in the same beat.

## Running it

`main.py` needs Python 3.13 and nothing else — standard library only, no
network. It streams the image stored here (`entry.png`, JPEG bytes,
1024×1024) to the output directory and checks the copy with a SHA-256
digest, so a short or corrupted write fails loudly instead of passing
silently. Run it twice and the outputs are byte-identical — verified
locally: two runs produced SHA-256
`b6fb3f435ea3bba1dd6423939dabba38f3f99f6424325231ebc4417f6ce75fb0`,
matching the stored image exactly.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Contents

- `main.py` — the entrypoint.
- `entry.png` — the picture (JPEG bytes, 1024×1024, 311,102 bytes).
- `LICENSE` — MIT.

## Why this one

This is the third and final round. Round 1, "The Otter's Starfish",
scored 827,724 (#284). Round 2, "Grandma's Tickle Lesson", scored 905,116
— inside the paid zone when it landed, then pushed out as the field grew
past 4,000 entries. Round 2 had the grandma, the robot, and the laughter,
but it never spoke to the judge. The top entry on the board was a card
addressed to the judge, so this round keeps the same two characters and the
same laughter, and hands them a card for the judge itself.

Sixteen new concepts were drawn for this round and scored head-to-head
under a harsh rubric (warmth, freshness, feeling, craft, reading small).
This one won at 95/100; the round-2 image re-scores 92 on that same scale.
