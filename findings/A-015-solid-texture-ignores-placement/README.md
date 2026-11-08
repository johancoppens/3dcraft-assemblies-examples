# A-015: a solid texture does not turn with an instance's placement

```sh
craft3d-cli run --new '{"units":"mm"}' --script bar.json --out bar.3dcraft
craft3d-cli run --new '{"units":"mm"}' --script asm.json --out two.3dcraftasm
craft3d-cli render two.3dcraftasm --out two.png --view top --look studio --environment workshop --renderer gpu
```

One oak bar, placed twice: `Straight` as drawn, `Turned` rotated 60° about z. `two-bars.png` (GPU renderer; the CPU
renderer was run too) shows the grain along the straight bar and across the turned one: it runs along the world's x
axis in both. The texture's frame is not carried by the instance's rigid placement.
