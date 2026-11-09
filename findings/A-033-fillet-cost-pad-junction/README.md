# A fillet of seven circles where a cone meets a ring costs 15 to 25 s of CPU

**3DCraft 45233bdc, found in 06-radial-engine (performance).** A cast-style shape: seven pads, each a cone, on a revolved
ring; `feature.fillet` of the seven junction edges (3.5 mm) makes the document take 15 to 25 s of CPU to regenerate (the
part without the fillet: under 2 s, measured on a busy machine with `craft3d-cli info`). `feature.chamfer` on the same
edges costs as much. Expected: seven similar edge blends of this size should be a small part of a regeneration.

`craft3d-cli run --new '{"units":"mm"}' --script repro.json`. Workaround used: the pads are given up for a heptagonal
crankcase with machined flats (no such junction).
