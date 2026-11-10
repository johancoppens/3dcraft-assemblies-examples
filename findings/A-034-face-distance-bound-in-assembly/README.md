# A-034: in an assembly, `distance` between two coaxial cylinder faces proves only a loose lower bound

**Performance (precision), a case of A-034. 3DCraft 150f0015, found in the radial engine's valve train.** A ring (outer radius 150 mm) turns in the bore of
a plate (radius 150.5 mm). In an assembly, `distance` between the ring's outer face and the plate's bore face, found by
query (`in`, `surface`, `radius`), reports "found 0.5 mm (at least 0.049 mm)". An assertion bounded 0.04 to 0.12 mm is
then `notProven`, never `failed`, so a loose fit cannot fail cleanly. In a single part with the same two faces,
`measure.distance` proves the value to 1e-12 (found 0.5, at least 0.49999999999824). With a 0.08 mm gap the bound is
close in the assembly too (at least 0.07999). Related: A-034 (`clearance` on coaxial cylinders).

Reproduce (in a scratch folder): `craft3d-cli run --new '{"units":"mm"}' --script ring.json --out ring.3dcraft`, the same
for `plate.json` to `plate.3dcraft`, then `craft3d-cli run --new '{"units":"mm"}' --script repro.json`: the assertion
`journal gap` is `notProven` with "found 0.5 mm (at least 0.0490085701 mm)".

**Should:** the proven bound of a face distance in an assembly as tight as in a part, so that a measured 0.5 mm against
a maximum of 0.12 mm fails. **Impact on the assembly:** the cam ring's journal fit. A loose bore (0.5 mm) makes the fit
assertion `notProven`, which `tools/assemblies.py check` counts as a problem, but `document.check` stays ok.
