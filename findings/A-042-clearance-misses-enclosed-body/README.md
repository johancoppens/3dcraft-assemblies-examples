# A-042: `clearance` reports clear when one body lies wholly inside another

**Bug. 3DCraft 150f0015, found in the radial engine's valve train (review).** A ring (a torus of major radius 14.4 mm,
section radius 1.75 mm) lies wholly inside a 40 × 40 × 10 mm plate. `measure.clearance` from the plate to the ring
answers `"status": "clear", "clearance": 3.25`, the distance from the ring to the plate's faces, though its own
description lists "overlap (one in the other, or a common volume)". In an assembly with the two as parts, a
`motion.check` of `clearance` with `min` 0 passes at 3.25 mm, while `view.motion` with `collisions` reports the pair
with 870.5 mm³ in common, the ring's whole volume.

Reproduce in a scratch folder:
- part: `craft3d-cli run --new '{"units":"mm"}' --script repro.json` (the last `measure.clearance`);
- assembly: build `plate.json` and `ring.json` to `plate.3dcraft` and `ring.3dcraft`, then
  `craft3d-cli run --new '{"units":"mm"}' --script asm.json` (its last step, an `overlap` with `eq`, is refused by
  design: `overlap` takes `is`; the two steps before it show the bug).

**Should:** a body inside another is an overlap, as the description says, and an assertion on its clearance fails.
**Impact:** a `clearance` assertion with a minimum can pass on an enclosed body. In these assemblies the collision
check over the motion (`view.motion`) catches enclosure for every pair not listed as a contact; in the valve train only
the `spring_gap` outputs read wrongly at an open valve, where retainer and spring are a listed contact.
