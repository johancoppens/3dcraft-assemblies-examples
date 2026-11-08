# A-001: check-range cannot read the parts of an assembly that is not packed

```sh
craft3d-cli run --new '{"units":"mm"}' --script bar.json --out bar.3dcraft
craft3d-cli run --new '{"units":"mm"}' --script repro.json --out hinge.3dcraftasm
craft3d-cli check-range hinge.3dcraftasm
```

Every point fails with "its instance `Bar` is not placed: its source `bar.3dcraft` has not been read". The same file
runs with `craft3d-cli run` and passes `check-range` once packed (`assembly.pack`).
