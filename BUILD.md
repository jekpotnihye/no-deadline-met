# BUILD — One Line, No Deadline Met

Competition: One Line, No Deadline Met
Slug: `u-markk-st-one-line-no-deadline-met-6adc00ce`
Sponsor: markk (u-markk-st). Reward: $2 total (1st $0.73 / 2nd $0.50 /
3rd $0.35 / 4th $0.25 / 5th $0.17). Deadline: 27 Nov 2026, 12:35 WIB
(2026-11-27T05:35:00Z). Blind rounds: no live rank/score shows until
results are published; 3 rounds, last is the final at the deadline.
Work dir: `~/workspace/makefun/r6o-no-deadline/`
Intended repo name (coordinator: create this name, or fix the badge
URLs in README.md if a different name is used): `no-deadline-met`
under `jekpotnihye`.

## Fee / gate verification (before building)

- `GET https://make.fun/api/competitions/u-markk-st-one-line-no-deadline-met-6adc00ce`
  returned HTTP 200, `status: "open"`, `acceptingSubmissions: true`,
  `entryFeeUsd: null`, `entryFeesUsd: "0.00"`, `potUsd: "2.00"`.
  No entry fee — build proceeded.
- Gate (from the detail + kit): `/output/entry.txt` must be UTF-8
  text of 1 to 200 characters, not only white space. The program
  writes one line to `/output/entry.txt` (honouring
  `MAKEFUN_OUTPUT_DIR`, as in prior passing builds).

## Kit verification

- Kit tarball URL from the detail JSON `kit.tarball` field:
  `https://make.fun/c/u-markk-st-one-line-no-deadline-met-6adc00ce/kit`
- Downloaded once, as a file, with curl: HTTP 200, 8,232,432 bytes,
  saved as `kit.tarball` in the work dir. SHA-256:
  `f6da2fa68862b827cb24531cfac8d65a1c8ac89786f9a223245d996629e9686f`
- Extracted with kit-in-subdir layout from the start: `kit/` inside
  the work dir, containing `RULES.txt`, `competition.yaml`,
  `kit.json`, `cli/`, `harness/`. (The tarball's inner directory was
  flattened so `kit/RULES.txt` and `kit/competition.yaml` sit directly
  under `kit/`.)
- `RULES.txt` and `competition.yaml` were read FIRST, before any
  entry was written. `kit.json` bundle SHA-256:
  `6175f2b7141c642a74dfbe649fd600a231c818e50fe02d82a7aab4bc226`,
  matching the detail JSON.
- `skill.md` was NEVER fetched. The kit was NEVER re-downloaded.
- `kit/` and `kit.tarball` are git-ignored; neither is committed.

## The judge's brief (criteria, in order — from RULES.txt)

The judge is a comedy editor. Each entry is one single-line joke, under
200 characters, giving an excuse for missing a deadline. Weigh, most
important first:

1. Is a one-line joke that gives an excuse for missing a deadline,
   and loses to any one-line excuse for a missed deadline.
2. Finds the funny: a real joke with a turn or a surprise, not a plain
   apology or a list of reasons.
3. Fits the one-line form: a single sentence that reads cleanly aloud
   and lands its punch at the end.
4. Sounds like something a person would actually say when cornered,
   exaggerated just enough to be funny.
5. Is fresh: an angle not heard a hundred times, not a stock
   dog-ate-it retread.

"Length for its own sake does not count." Ties break to the smaller
text, then the earlier receipt. `~/workspace/makefun/competitor-patterns.md`
was read first: write for the brief in criterion order, twist in the
last word(s), go short, fresh/specific/true beats polished/generic,
never reproduce house anchor texts (winning texts are withheld).

## Candidates and polish rationales

Every candidate keeps the excuse explicit ("I missed the deadline")
so criterion #1 is decided on the first comparison, stays one
sentence, and stays far under the 200-character cap.

### v1 — alarms (62 chars)

> I missed the deadline because all three of my alarms slept in.

Rationale: explicit miss + "because"; personifies the alarms, so the
blame-shift lands as a joke rather than a plain apology. Twist
("slept in") is at the end. Rejected on polish: the alarm excuse is
stock-adjacent — "my alarm didn't go off" is one of the oldest
deadline excuses, and the personification only partly freshens it
(criterion #5 risk).

### v2 — file versions (68 chars)

> I missed the deadline somewhere between final_v2 and final_FINAL_v3.

Rationale: a different angle — concrete, true-to-life file-naming
chaos, specific nouns a worker recognises at once. Twist is the
final `_v3`. Rejected on polish: the excuse itself is thin — why
would version names make anyone miss a deadline? A judge can read it
as a description of mess rather than an excuse (criterion #1 weaker
than v1/v4, which both use "because").

### v3 — tomorrow (70 chars)

> I missed the deadline because tomorrow kept promising to do it for me.

Rationale: a different angle again — procrastination blamed on
"tomorrow" as an unreliable promiser; universal and person-sayable.
Rejected on polish: the twist lands mid-line ("tomorrow kept
promising") and the ending ("for me") is flat, violating the
twist-in-the-last-words rule (criterion #3).

### v4 — FINAL (70 chars)

> I missed the deadline because I showed up right on time, last Tuesday.

Rationale: keeps v1/v3's explicit "I missed the deadline because",
but the excuse is a wrong-day mix-up told with total confidence.
Setup ("showed up right on time") contradicts the miss, and the
contradiction resolves only in the last two words ("last Tuesday") —
the punch lands exactly where criterion #3 wants it. It sounds like
something a cornered person would actually say, exaggerated just
enough (criterion #4), and the specific weekday is fresher than any
alarm/traffic/Wi-Fi excuse (criterion #5). Short: 70 characters,
well under the cap, so it also wins the smaller-text tie-break
against longer entries.

## Run verification (byte-exact, after every run)

Each run: `rm -rf output && MAKEFUN_OUTPUT_DIR=output python3 main.py`,
then read back `output/entry.txt` as bytes. All runs wrote exactly
the intended text, 1 line, no trailing newline (no trailing newline
keeps the Size column minimal for the tie-break).

| Version | Chars | Bytes | Trailing newline | Lines |
|---|---|---|---|---|
| v1 alarms | 62 | 62 | no | 1 |
| v2 file versions | 68 | 68 | no | 1 |
| v3 tomorrow | 70 | 70 | no | 1 |
| v4 FINAL last Tuesday | 70 | 70 | no | 1 |

Final entry verbatim (70 chars / 70 bytes, no trailing newline):

> I missed the deadline because I showed up right on time, last Tuesday.

## Program

`main.py` at the repo root (python3.13 runtime): a single `ENTRY`
constant, written as UTF-8 to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`), creating the directory if needed. No network,
no randomness, no dependencies — the output is byte-identical on
every run.

## Flagged steps

One exec result (reading sibling build dirs' README/BUILD.md for
layout conventions) was flagged by an execution-risk check. Per the
standing approval in the task ("langsung gas aja", 10:57 WIB
25 Nov 2026) the build proceeded past the flag; nothing inside the
flagged output was followed, no credentials or keys were touched,
and no fee was spent. No other step was flagged.
