# A flexible subassembly whose `t` comes through `params` is rebuilt per moment

Found while building `jansen-walker` at 3DCraft `150f0015`.

**What happens.** A leg subassembly (`leg.json`: eight instances, its crank driven by its own `t`) is placed twelve
times with `"mode": "flexible"` and `"params": {"t": "t + phase"}` (`parent.json`). It works: at 3DCraft `150f0015`
every foot follows the closed form at its phase, including legs turned half a turn about z. But the configuration key
of an instance is its parameter values, so every moment of the motion is a new configuration of the subassembly, even
though nothing of its geometry changes:

| | configurations built | `motion.bake` 120 frames |
|---|---|---|
| `t + phase` in `params` (twelve 8-body legs) | 2097 (659 wanted) | 7.5 s |
| undriven legs, crankshaft mated in the parent (`../A-013-solver-hub-cost/parent5.json`) | 3 | 6.5 s at the same load, and it is 12 legs on one real shaft |

(Measured on a busy reference machine, load average 20 to 38, so the absolute numbers are inflated; the ratio is what matters. The bake of the
params variant grows with every body added to the leg, since each moment re-makes the whole subassembly placement.)

**Should.** A parameter that only reaches a subassembly's drives (never a feature's geometry) should not be a new
configuration: reuse the subassembly's parts and placement and drive its joints. More generally, let a parent pass a
"phase" without paying for a rebuild.

**Also.** With its phase in `params` the leg cannot be driven from outside at the same time: its own `Crank_axle` drive
is kept in the parent because the parent sets `t` (the documented rule), so a real crankshaft would add a second driver
per leg. That combination was not tried. The walker keeps its legs undriven and carries the phase in the
crankshaft's keyed couplings (see its README).

**Reproduce.** Build `bar.json`, `tri.json`, `plate.json` (`craft3d-cli run --new '{"units":"mm"}' --script X.json
--out X.3dcraft`), `leg.json` (`--out leg.3dcraftasm`), `parent.json` (`--out parent.3dcraftasm`) in this folder, then
`craft3d-cli run parent.3dcraftasm --cmd motion.bake --params '{"frames":120}'`.

**Impact on the assembly.** Workaround used: no phase through `params`; the legs are flexible and undriven and the
phase lives in the keyed couplings of the crankshaft.
