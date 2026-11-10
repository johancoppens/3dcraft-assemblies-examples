# Missing capability: no fillet of a sketch corner

Found while building `toggle-clamp` at 3DCraft 150f0015.

A stamped outline is lines with a radius at every corner. There is no sketch command that rounds a corner between two
lines (`repro.json` asks for `sketch.fillet`: unknown command). `sketch.path` can draw the arcs, but only from end
points the author computes: for a corner of two lines of known direction the tangent points are the vertex plus
`tan(angle/2) * r` along each line, so an outline driven by variables needs either long symbolic expressions or a
literal tangent factor per corner. `feature.fillet` after the fact does not help a sheet-metal part, whose flat pattern
is cut from the sketch and would not carry it.

**Should:** a sketch corner fillet (`sketch.fillet {sketch, corner point, radius}` or a `radius` per corner in
`sketch.path`), which keeps the two lines tangent to the arc for every value of the variables.

**Impact on the toggle clamp:** about 130 literal tangent factors such as `-0.269584 * (corner)` in `bar`, `base` and
`handle`. They are exact at the defaults; with other pivot positions the corners are arcs a hair off tangent. That is
also why the sheet parts' rims are not chamfered (a chamfer chain needs exactly tangent edges).
