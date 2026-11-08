# A part that builds at some values fails when `param.set` reaches them from other values

`repro-arm.json` is the scissor jack's arm with the defaults `inner_width` 41.5 mm and `tooth_hand` 0. A fresh build of
the same source with the defaults changed to 34 mm and 1 is fine, and so is the same configuration as an assembly's
instance. On the saved part, `param.set {"inner_width": 34, "tooth_hand": 1}` fails:

    Arm failed: plate produced an invalid body: loop 3 of face 2 does not lie where the face's other loops leave it
    room: it is outside the region they bound; loop 6 of face 3 ...

    craft3d-cli run --new '{"units":"mm"}' --script repro-arm.json --out arm.3dcraft
    craft3d-cli run arm.3dcraft --cmd param.set --params '{"values":{"inner_width":34,"tooth_hand":1},"clamp":false}' --cmd document.inspect

34.01 mm reaches it without trouble and 35 mm too, so it is not the geometry at those values that fails but the way a
regeneration reaches them from another state: the result depends on the path. Saved with the defaults 34 mm and 1,
`param.set` to every other combination (41.5/0, 41.5/1, 34/0, 35/0) and back works.

Impact on the jack: none in the assembly, whose instances build fine; the flat-pattern exports (`file.export` with
`values` go through `param.set`), so the arm's source keeps the defaults 34 mm, hand 1. Worth knowing because a
`check-range` or a configurator can hit such a state.

**The same failure on a fresh build at other values.** `repro-fresh-failure.json` is the arm with `arm_length` 190 mm,
`inner_width` 44 mm, `pitch_radius` 19 mm, `mesh_middle` 138°, `pin_hole` 11 mm and hand 1 and fails on a fresh build:
`Arm failed: plate produced an invalid body: loop 3 of face 2 ...`. Those values are nothing unusual for a gear, so the
message reads as a kernel limit rather than a design error. The failures come and go by small changes of parameters and
of the path (the same point is fine fresh and fails through `param.set`), so a part with several public parameters is at risk
of this in `check-range`: with nine public parameters the arm failed 29 of 69 points, with three, none.

Impact on the jack: the arm publishes only its length, inner width and tooth hand. Its sheet thickness, bend radius, pitch
radius and hole sizes are its own copies of the assembly's values, kept equal by the assembly's fit and gear-mesh
assertions, instead of being passed by `params`. (That the arm cannot publish them is the workaround.)

**Scan of the root fillet.** The failure's frequency over the 28 arm configurations the assembly can ask (7 lengths × 2 widths × 2 hands, each reached by `param.set` from the source's defaults) against the tooth's root fillet: 0.2 mm 0, 0.25 mm 5, 0.3 mm 0, 0.4 mm 2, 0.5 mm 1, 0.8 mm 1, 1.0 mm 5. It is not monotone, which reads as numerics, not geometry. The jack uses 0.3 mm.
