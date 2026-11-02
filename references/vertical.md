# Vertical films (9:16, 1080×1920)

What the W1-v2 film (`cases/huazhong-dongtian-22s/`) taught, after a first vertical cut that passed every oracle leg
and was sent back as 「很死板，没到参考片的 70%」.

## The frame is a column, and the platform sits on top of it

| zone | what covers it (小红书 / 抖音 / 视频号) | rule |
| :-- | :-- | :-- |
| y > 1560 | title, caption, music line | picture yes, anything to read no |
| x > 940 | like / comment / share buttons | picture yes, text no |
| top corners, y < 240 | back / share buttons | no small labels, years, tags |
| y 240–1440 | — | the subject and every word that matters |

Captions (if narrated) centre around y 1490. Never leave the covered zones black: blurred material, the ground of the
look, anything — an empty band reads as a crop.

**Fill the column.** A landscape film's "small elements, big ground" leaves a tall frame mostly empty. Use material that
runs top to bottom (portrait photos, full-frame UI, a tall stack) and let it run off the edges.

`stills.py --width 1080 --height 1920` keeps the 9:16 tiles. Draw the safe lines on every contact sheet you look at.

## The music is the clock

1. Choose the track first. `python3 scripts/beat_grid.py track.m4a` → tempo, grid, silent gaps, kicks.
2. Check the grid against the kicks: short loud clips often report a half- or double-time tempo
   (W1-v2's clip read 92 BPM; the kicks sat on a 0.427 s grid, 140 BPM).
3. Write the beat sheet in beats: `beat(k) = first + k · period`. Every landing, every opening, every word on a beat.
4. A silent gap in the track is where the picture stops dead. The first kick after it is the drop: everything that
   was waiting opens at once.
5. Film time = track time from 0 when the music carries the hook. 20 s clips cover a 22 s film if the end card holds
   on the last hit's tail.

## The nested-portal dive (画中洞天)

One take down through N pictures. Each picture has a hole in a feature it already has (a clock face, a plate's
medallion, a bridge arch, a mask's mouth); inside it, the next picture. As the camera lands, the hole grows into
that picture's whole vertical frame, so each level ends full-bleed.

**Levels and camera.** A continuous `p(t)`: integer `p` = level `p` fills the frame. Nesting map of level k into
k−1: `x_parent = h + R(θ)(x − C) / Z`. Camera at `p = k + f`: scale `Z^f`, rotate `−θf`, focal point moving from the
centre to the hole as `w(f) = (1 − Z^−f) / (1 − 1/Z)`. At `f = 1` the map is the identity on level k+1 — no jump.

**Z per hole.** `Z = min(540 / rx, 960 / ry)`: the child frame just covers the hole, so no blurred edge shows inside
it. Keep holes ≤ r 300 or the zoom per level is too small to feel (r 460 → Z 1.17).

**The hole morphs.** Draw it in the child's coordinates: a circle of radius `r·Z` that, as `f` goes 0.35 → 1, becomes a
rounded rect of the full 1080×1920 with the corner radius going to 0. The gold ring fades with it. This is the beat
that reads: a portal turning into the next film's frame.

**Draw depth.** From the current level inward, clip each child to its parent's hole, stop when the child is under a
few pixels. Behind every level draw a blurred, enlarged copy of it, so rotation never shows a corner.

**`__motion`.** Map the screen corners into the current level at `t0`, forward to the screen at `t1`, take the
largest travel — the shutter then sizes itself (W1-v2: up to 976 px/frame in the burst).

**Numbers on screen under the shutter.** A counter that changes inside the shutter's open time ghosts into two
values. Quantise what it shows to the frame: `value(P(round(t·30)/30))`.

**The arc for the dive.** hook (3 fast levels, words on beats) → holds (a picture, its hole opens on a beat, dive) →
dead stop on the track's silence → the drop (every hole opens, accelerating fall, a zoom counter) → one long rest at
the deepest picture → pull all the way back out in one move → the reveal of what held it all (here a Claude Code
input preview) → end card that holds still.

## Rest, measured against the reference

The oracle's fixed 25 % stillness comes from motion-web. With `--ref`, `verify_promo.py` asks for 0.8 × the
reference's still share instead; the onetake launch film is 10 % still, W1-v2 is 11 %. Most of that is the end card:
let it land and stop. A gently pushing end card made the film 3 % still.

## What bit

- **Claims about the material.** "These images all come from films I made" — one photo had only been collected, never
  used in a film. Check each source against the film's spec before a line on screen says so.
- **CSS position plus a transform.** An element with `left/top` in CSS *and* a centring `translate` lands twice as far.
  Position with one or the other.
- **Overlays tied to an event** (`1 − (t − tHit)/d`) are > 1 before the event: gate them with `t ≥ tHit`.
- **Cover frames.** Grab them from the comp with the film's own captions off (override the function before `__seek`),
  or the cover's title fights the film's.
- **Render cost.** W1-v2: 675 frames, 5,191 captures, 384 s on 8 workers at 1080p30.
