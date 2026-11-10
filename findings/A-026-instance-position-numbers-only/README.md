# Agent friction: an instance's start position cannot be an expression

Provisional finding from `assemblies/05-corexy-printer` at 3DCraft `150f0015`.

`instance.add` `position` (and `rotation`) must be plain numbers: `["gap/2", 0, 0]` answers `position must be three
finite numbers`. `repro.json` shows it (place `tslot.3dcraft` beside it, any part with a `length` parameter). An
instance that nothing constrains or that needs a start pose cannot follow an assembly's parameters, and a frame that
changes size must be placed entirely by mates with `offset` expressions (at the pin, datums on the parts, or chains of
fixed mates), or by parameters of datums inside the parts. **Should:** `position` and `rotation` accept expressions, as
`params` does; when they are expressions the instance is re-placed from them whenever the parameters change.

**Impact.** Workaround: the frame is held by chains of fixed mates between corner cubes and the frame centre is a
datum of one cube whose offset comes from the part's `frame_size` parameter.
