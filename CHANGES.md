# longtake vs onetake

longtake is a modified version of [onetake](https://github.com/feitangyuan/onetake) by Patrick
(PolyForm Noncommercial 1.0.0, see `LICENSE` and `NOTICE`). Base: onetake commit `013a61a`.

## Changed

| file | change | why |
| :-- | :-- | :-- |
| `SKILL.md` | renamed to `longtake`; new section **What the protocol cannot give you** (material worth looking at, a music clock, an arc, change as content, rounds of looking) | a vertical film passed every rule and every oracle leg (carry 1.00, VERDICT PASS) and was still rejected as stiff |
| `SKILL.md` §1 | the reference's measured numbers (still %, fill, cuts, densest stretch, music) outrank the genre rules | "small elements, big ground" and "still a third of the time" come from one reference; the onetake launch film is ~10 % still and full frame |
| `SKILL.md` §2 | a concept may not copy a case's or an example's central idea; two test questions; a paragraph on vertical frames | the rejected cut picked the first example ("one dot") |
| `SKILL.md` §3 | **Arc and clock**: pick the track first, write the beat sheet in beats | timing beats by reading time gives an even, stiff pace |
| `SKILL.md` §7 | a film without narration gets music by default; if a project forbids it, raise it | the rejected cut had no music, so no clock |
| `SKILL.md` §8 | the oracle is a floor, not a grade; report the gaps to the reference; never tune `__track` to pass a leg | a continuity score bought by merging two objects into one id measures nothing |
| `SKILL.md` hard rules | "small elements, big ground" and "never always in motion" now follow the reference's numbers | same as §1 |
| `scripts/verify_promo.py` | with `--ref`, **rest** needs 0.8 × the reference's still share (if lower than 25 %), **audio** needs 0.8 × the reference's quiet share (if lower than 15 %) | a film on music, matching a 10 %-still reference, failed legs the reference itself fails |
| `scripts/stills.py` | tiles keep the page's aspect (9:16 when `--width < --height`) | vertical comps were squashed into 16:9 tiles |

## Added

| file | what |
| :-- | :-- |
| `scripts/beat_grid.py` | tempo, beat grid, silent gaps, kicks and energy per beat from a track (numpy, scipy, ffmpeg) |
| `references/vertical.md` | 9:16 safe zones, filling a column, the music clock, the nested-portal dive with its maths, what bit |
| `cases/huazhong-dongtian-22s/` | the W1-v2 film: preview GIF, contact sheet, beat sheet, numbers against the reference |
| `CHANGES.md`, `NOTICE` | this file; the required notice |

## Removed from this copy

The original films (`cases/*/*.mp4`) and `assets/` (onetake's logo, hero GIF and case GIFs) are not redistributed
here; they remain in the onetake repository. Every case README is kept.
