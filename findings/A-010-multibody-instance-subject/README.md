# Agent friction: a multi-body instance is not a measure subject by its own name

Found while building `toggle-clamp` at 3DCraft 45233bdc.

Build `two_bodies.json` to `two_bodies.3dcraft`, then run `repro.json`. `assert.add` with `from: "Handle"` answers
`cannot be measured: there is no feature named 'Handle'`, though `Handle` is the instance. The same subject works as
`Handle/First body`, one body at a time. (`A-007` covers a subassembly's name; this is a plain instance of a part with
two bodies.) Should: the instance's name means all its bodies, as `overlap` of an instance with one body does.
