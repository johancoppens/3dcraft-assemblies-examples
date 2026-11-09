# A-041: an output of `clearance` is known where the same assertion is not proven

**Bug. 3DCraft 45233bdc, found in the task lamp's review.** `clearance` finds a gap between a pair of points (an upper
bound of the true gap) and proves a lower bound. Where the two are far apart (A-034), an assertion with a `max` reads
*not proven*, as it should. The same measure as an output (`variable.measure`) is `known` at the gap found, with no bound,
though the command's own text says an output is unknown when "what it proves is wider than the document's tolerance".
So one gap reads two ways in one document:

```
OUT    probe_side_play                 known      0.9 mm
ASSERT Probe side play on the output   failed     value: measured 0.9 mm, expected 0.2 mm to 0.6 mm
ASSERT Probe side play direct          notProven  clearance: not proven: found 0.9 mm (at least 0.416173598 mm)
```

Reproduce: in `assemblies/04-task-lamp/build.json`, pass the turret's `cheek_gap` as `cheek_inner + 0.5 mm` (its slot
1 mm wider), build the lamp, and run `probe.json` against the packed assembly:
`craft3d-cli run task-lamp.3dcraftasm --script probe.json`.

**Should:** one contract. Either the output is unknown, as documented, or it carries the interval it proves, and an
assertion on it says what the interval decides.

**Used deliberately:** the gap found is a real pair of points, so a `value` assertion with a `max` on the output passes
exactly when the clearance assertion's `max` would, and fails where the assertion only reads not proven. A loosened fit
then fails a mutation test. The lower side stays with the `clearance` assertion, whose bound is proven.
