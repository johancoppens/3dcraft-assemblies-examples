# A material set before a later feature is lost to an instance, though the part itself keeps it

Found while building `task-lamp` at 3DCraft 45233bdc.

```sh
craft3d-cli run --new '{"units":"mm"}' --script plate.json --out plate.3dcraft
craft3d-cli run --new '{"units":"mm"}' --script repro.json
```

`plate.json` makes a block, gives it `material.preset` (oak), and then a later feature (`feature.boolean` subtract) takes
that body. The part's own `mass` measure works, its assertion passes (0.0043 kg). `repro.json` places the part in an
assembly, and `variable.measure mass` of the instance answers: *cannot be measured: `Plate` has no material, so no mass;
give it one with body.material*. The colour survives the boolean into the assembly's picture; only the material is lost.

**Should:** the instance's body carries the material the part's own measures see, or the part's material applies to the
body the later feature made, as the part sees it. **Impact:** the mass of every part with a boolean after its material
was unknown to the assembly's balance outputs. **Workaround:** `material.preset` is applied after the last feature that
touches the body (the bar in `task-lamp`).
