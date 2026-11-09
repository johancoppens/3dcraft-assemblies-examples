# A configuration whose feature fails is placed and `document.check` of the assembly says ok

Found while building `task-lamp` at 3DCraft 45233bdc.

```sh
craft3d-cli run --new '{"units":"mm"}' --script plate.json --out plate.3dcraft
craft3d-cli run --new '{"units":"mm"}' --script repro.json
```

`plate.json` is a block with a `feature.fillet` of radius `corner` (published, default 1 mm). `repro.json` places it with
`"params": {"corner": "12 mm"}`, more than the 4 mm plate allows. The same value in the part itself
(`param.set`, then `document.check`) fails with *radius: too large for edges.0*. In the assembly the instance's row
says `"status": "ok"`, `"error": null`, and the assembly's `document.check` is `{"ok": true, "problems": []}`: the
instance is built from a partial regeneration and placed without a word.

In the lamp the turret was placed this way with a turret fillet that failed for its computed parameters: `Turret` showed
four separate intermediate bodies (`Turret/Turret foot`, `Turret/Cheek plate`, the tools of its cuts), each overlapping
the bars and pins; only `assembly.inspect` (four body ids) and the collisions gave it away. **Should:** an instance whose
configuration has a failed feature fails by name (`status`, `error`, and `document.check` lists it), as a mate whose face is
gone does. **Impact:** cost an hour of diagnosis on the lamp; a silent failure in any assembly that passes a computed
parameter to a part. **Workaround:** none: narrow the parts' public ranges and check them by `check-range`.
