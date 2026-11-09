# A-035: a face's own appearance is lost on an assembly instance

```sh
craft3d-cli run --new '{"units":"mm"}' --script plate.json --out plate.3dcraft
craft3d-cli run --new '{"units":"mm"}' --script repro.json --out plate-asm.3dcraftasm
craft3d-cli render plate.3dcraft --out part.png --view iso --renderer cpu
craft3d-cli render plate-asm.3dcraftasm --out asm.png --view iso --renderer cpu
```

`plate.json` is a green block with one face given a cream colour by `face.appearance`. The part shows that face cream
(`plate-3dcraft.png`); the same part placed once in an assembly shows it green like the rest of the body
(`plate-asm-3dcraftasm.png`). The body's own appearance reaches the instance; the face's does not.
