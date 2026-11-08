# A sheet-metal flange with a formula curve renders blank at the default framing

A part whose `feature.sheetMetal` flange outline uses `sketch.curve` (an involute gear flank) regenerates and measures
fine (`document.inspect`: valid solid, sane `bbox`), but `view.render` with the default framing (no `box`) returns a
picture of nothing: `coverage: 0.0`, a `tolerance` of about 119 mm and a `box` inflated well beyond the body, e.g.
`[[-142.5, -23.75, -119.3], [297.3, 23.75, 166.0]]` where the body's own bbox is `[[-23.2, -23.75, 0], [177.8, 23.75, 46.7]]`.
The same part with the flanks drawn as chords (`sketch.path` lines) frames and renders normally (coverage 0.22).
Giving `view.render` an explicit `box` renders the part correctly, so only the default framing is wrong: the view's
"box around the bodies" seems to come from something other than the bodies (a fitted spline's control polygon?).

Run (writes `repro.png`, the result JSON ends with the coverage):

    craft3d-cli run --new '{"units":"mm"}' --script repro.json

Impact on the scissor jack: none on the final model (the flanks became chords to keep the load budget, and the preview
gives its own camera), but a part drawn the obvious way (formula involutes) previews blank.

Second observation from the same part: the part with `sketch.curve` flanks costs about 13 times the CPU of the same part
with polyline flanks at regeneration (1.3 s against 0.10 s in `craft3d-cli info`, on the same machine, `time` of the
CLI) because every flank is a fitted B-spline with 43 control points through a sheet-metal rim; the arm is built four
times per load, so the jack could not stay within its 2 s / 6 s CPU budget with real involute curves and uses chords.
