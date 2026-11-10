# Performance: a revolved formula curve (`sketch.curve`) regenerates about 8 to 20 times slower than a polyline of the same outline

Found while building `corexy-printer` at 3DCraft `150f0015`.

**What happens.** A thin-walled vase of revolution is revolved from a closed outline of two `sketch.curve` formula
curves (`curve.json`) or from a polyline with 32 points per wall on the same formula (`polyline.json`): same outline to
within the polyline's chord error. Opening and regenerating the part with `craft3d-cli info`, on a busy reference
machine (load average 38 to 47, so absolute numbers are inflated; the ratio is the point):

| Outline | `craft3d-cli info` of the part (three runs each) |
|---|---|
| `curve.json`, two `sketch.curve` walls | 0.50, 0.59, 0.57 s (load 38); 1.34 to 1.96 s (load 47) |
| `polyline.json`, 64 polyline points | 0.06, 0.07, 0.11 s |

The part is regenerated at every moment of a motion in which its height follows `t`, so this decides whether a part
can follow the timeline.

**Should.** A revolve whose profile is a smooth fitted curve should cost little more than a polyline of the same
number of faces; the cost is probably in the B-spline surface of revolution, or the fitted curve's re-fit at each
regeneration.

**Reproduce.** `craft3d-cli run --new '{"units":"mm"}' --script curve.json --out curve.3dcraft`, the same for
`polyline.json`, then `craft3d-cli info` on each.

**Impact on the assembly.** Workaround used: the vase's outline is a polyline of 24 points per wall in
`parts/vase.json` (the README says so); a smooth `sketch.curve` would not fit the motion's budget.
