# `sketch.path` refuses a point of a pattern instance as its start, `sketch.line` accepts it

`sketch.pattern` says a point of a pattern instance can be used "where a point is taken: `e5[3]`, or `e5[last]`". After
a chained pattern, `sketch.line {"from": "e4[last]", ...}` works, but `sketch.path {"start": "e4[last]", ...}` fails with
"e6 is a image, not a point" (the pattern image is an image entity), so the outline that closes a chained run of teeth
cannot be a single `sketch.path` and needs a separate `sketch.line`.

    craft3d-cli run --new '{"units":"mm"}' --script repro.json

The first `sketch.line` succeeds; the `sketch.path` line stops the run. Should: `sketch.path` takes `e4[last]` as a
`start` (and as an `end`), as the rest of the sketch commands do.

Impact on the scissor jack: one more step per flange outline; agent friction only.
