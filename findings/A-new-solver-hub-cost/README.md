# The solve cost grows steeply with the number of mates sharing one body

Provisional finding (coordinator numbers it) from `assemblies/02-jansen-walker` at 3DCraft `45233bdc`.

**What happens.** Twelve legs of six bodies each, on one crankshaft. The two assemblies here place the same legs on
the same crankshaft and differ only in what the hip pivots are mated to:

| Variant | Instances | Mates sharing one body | `motion.bake` 120 frames |
|---|---|---|---|
| `parent4.json`: all 24 hip pivots mated to one chassis instance fixed to the world | 79 | 24 on the chassis | 11.0 to 13.3 s |
| `parent5.json`: each leg's two hip pivots mated to its own rib, each rib fixed to the world | 85 | 4 on each rib | 6.5 s |
| four legs on one chassis instance (`parent3b`, not committed) | 27 | 8 | 0.87 s |

The bake is almost independent of the frame count (24 frames: 11.5 s, 120 frames: 12.9 s): the cost is in the fixed
steps of `t` the moments are carried through. Three times the legs on one body costs thirteen times the time
(`parent3b` against the same assembly with twelve legs, 11.5 s). One crankshaft body or a chain of six segments made no
difference while the chassis stayed one body. Two runs each at load average 16 to 28 on 14 CPUs: the times are
inflated, the ratios less so.

**Should.** The cost of a solve should grow with the number of bodies, not with the square of the mates on one body
(a chassis, a crankshaft or a frame is the normal case for a machine): probably the redundancy analysis
(`J Jᵀ`) couples every mate on a hub.

**Reproduce.** Build `bar.json`, `tri.json`, `chassis.json`, `seg.json` and `legq.json` (`.3dcraft`; `legq.json` as
`.3dcraftasm`), then `parent4.json` and `parent5.json` (`craft3d-cli run --new '{"units":"mm"}' --script parent5.json
--out parent5.3dcraftasm`), and `craft3d-cli run parent5.3dcraftasm --cmd motion.bake --params '{"frames":120}'`.

**Impact on the assembly.** Workaround used: each pair of hips has its own rib, grounded separately, and the
crankshaft is a chain of six keyed segments instead of one hub with twelve pins.
