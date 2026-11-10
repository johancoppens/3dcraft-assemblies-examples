# Pose measures do not reach an instance inside a rigid subassembly

**3DCraft at the pin, found in assemblies/06-radial-engine.** In a parent assembly with a rigid subassembly placed as
`Sub`, whose instance is `Inner`: `clearance` from `Sub/Inner` to another instance works (a body path), but
`{"measure": "rotation", "instance": "Sub/Inner", "axis": "y"}` fails with `the assembly has no instance Sub/Inner`,
while `"instance": "Sub"` (the subassembly's own name) is accepted. AGENTS.md (and the guide's chapter on assemblies) state that a
measure reaches an instance inside a subassembly by its path and that the subassembly's own name is not a subject:
the two kinds of measure resolve subjects differently. Expected: one rule. Either a pose measure on `Sub/Inner`
answers with the inner instance's pose (subassembly pose composed with its placement), or the guide states that
pose measures take the subassembly's name.

Reproduce (in this folder, from a scratch copy so nothing else changes):
`craft3d-cli run --new '{"units":"mm"}' --script block.json --out block.3dcraft`, the same for `sub.json` to
`sub.3dcraftasm`, then `craft3d-cli run --new '{"units":"mm"}' --script repro.json`. The first assertion passes; the
second is an error: `cannot be measured: the assembly has no instance Sub/Block`.

Impact on the assembly: workaround used (the firing-order assertions of `06-radial-engine` measure `Cylinder[k]`, the
rigid subassembly's own name).
