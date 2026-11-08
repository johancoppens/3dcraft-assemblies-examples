# A-009: motion.check with an inline measure is refused after param.set in the same run

```sh
craft3d-cli run --new '{"units":"mm"}' --script bar.json --out bar.3dcraft
craft3d-cli run --new '{"units":"mm"}' --script repro.json --out hinge.3dcraftasm
M='{"samples":2,"measure":{"measure":"jointAngle","mate":"Hinge","min":"-360 deg"}}'
craft3d-cli run hinge.3dcraftasm --cmd motion.check --params "$M"       # works
craft3d-cli run hinge.3dcraftasm --cmd param.set --params '{"values":{"swing":20}}' --cmd motion.check --params "$M"
```

The second run stops with: `motion.check: measure: assert.add: there is no assertion named 'overMotion1'`.
