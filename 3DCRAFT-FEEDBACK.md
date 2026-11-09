# Feedback for 3DCraft

What building these assemblies showed 3DCraft gets wrong or lacks, collected for the developer to take to 3DCraft in
one go (nothing is fixed from here). Kinds: **Bug** (wrong result, crash, a valid request refused; with a reproducer in
`findings/`), **Missing capability** (phrased for any mechanism and anyone), **Performance** (with numbers), **Agent
friction** (what made building through commands slow or error-prone). See `AGENTS.md` §7. Entries already known from
the examples (`F-nnn`) or the Jigs (`J-nnn`) are cited there, not repeated.

All entries are against 3DCraft `45233bdc` unless they say otherwise.

**Status (2026-11-09):** 41 entries: 15 bugs (one also performance), 11 missing capabilities, 8 performance, 7 agent
friction. The most costly for the assemblies: A-015 (wood grain wrong on every moving part), A-014 (the camera jumps
while a motion plays), A-013 and A-012 (solve and rebuild cost in machines with many legs), A-016 (an unreported branch
jump), A-002 (no pattern of instances) and A-034 (fits that read not proven).

| Id | Kind | Title | Found in | Impact |
|---|---|---|---|---|
| [A-001](#a-001) | Bug | `check-range` cannot read the parts of an assembly that is not packed | building the tool | subassemblies are not range-checked on their own |
| [A-002](#a-002) | Missing capability | No pattern of instances | radial engine, Jansen walker | long, repetitive `build.json` |
| [A-003](#a-003) | Missing capability | No contact joint between curved faces | radial engine (valve train) | cam motion by formula, proven by measure |
| [A-004](#a-004) | Missing capability | A ball mate cannot be driven, limited or coupled | task lamp | the shade is only posed by hand |
| [A-005](#a-005) | Missing capability | A trace is not kept in the document | Jansen walker, CoreXY printer | a saved assembly opens without its path |
| [A-006](#a-006) | Missing capability | A part's own assertions are not checked per configuration | every assembly | a configured instance is proven only by the part's own range check |
| [A-007](#a-007) | Agent friction | Measures name their subjects differently, and a subassembly is not a subject | building the tool | a retry per measure |
| [A-008](#a-008) | Missing capability | `craft3d-cli replay` cannot make a video of a motion | writing the guide for this repository | a motion video needs `view.replay` and ffmpeg by hand |
| [A-009](#a-009) | Bug | `motion.check` with an inline measure is refused after `param.set` in the same run | toggle-clamp (review) | a probe assertion instead |
| [A-010](#a-010) | Agent friction | A multi-body instance is not a measure subject by its own name | toggle-clamp | measured body by body |
| [A-011](#a-011) | Agent friction | An instance parameter from a formula is refused when off the part's step | toggle-clamp | parameters published without a step |
| [A-012](#a-012) | Performance | A flexible subassembly whose `t` comes through `params` is rebuilt at every moment | jansen-walker | phase moved into the crankshaft's keyed mates |
| [A-013](#a-013) | Performance | The solve cost grows steeply with the number of mates on one body | jansen-walker | a rib per leg instead of one chassis |
| [A-014](#a-014) | Bug | The window's camera refits at every moment of a motion | seen by the developer while playing the assemblies | the view jumps while it plays |
| [A-015](#a-015) | Bug | A solid texture does not turn with an instance's placement | task-lamp, jansen-walker, seen by the developer while playing | wood grain crosses moving parts; workaround: no texture on moving wood |
| [A-016](#a-016) | Bug | The rest solve of a flexible subassembly can land on another branch unreported | jansen-walker | crank start limited to scanned values, gait asserted |
| [A-017](#a-017) | Missing capability | `bendable` has no one-stroke U-forming of two parallel bends | toggle-clamp, scissor-jack | U-sections not proven bendable |
| [A-018](#a-018) | Missing capability | No fillet of a sketch corner | toggle-clamp | literal tangent factors, exact only at the defaults |
| [A-019](#a-019) | Bug | A sheet-metal part fails when `param.set` reaches values a fresh build accepts | scissor-jack | arm keeps its own defaults; 0.3 mm root fillet |
| [A-020](#a-020) | Bug | A screw coupling cannot name one cylindrical mate twice | scissor-jack | a revolute drives, the coupling ties it to the slide |
| [A-021](#a-021) | Bug, performance | A flange outline with a formula curve renders blank at the default framing, and costs 13× a polyline | scissor-jack | chords and an explicit camera |
| [A-022](#a-022) | Agent friction | `sketch.path` refuses a pattern point as its start, `sketch.line` accepts it | scissor-jack | one extra step per flange |
| [A-023](#a-023) | Bug | A configuration whose feature fails is placed and the assembly's `document.check` says ok | task-lamp | narrow part ranges and their own `check-range` |
| [A-024](#a-024) | Bug | A material set before a later feature is lost to an instance | task-lamp, radial-engine | material set on the last feature |
| [A-025](#a-025) | Performance | A helical spring that follows `t` costs 200 to 350 ms per moment | task-lamp | half-turn revolves in patterns |
| [A-026](#a-026) | Agent friction | An instance's `position` and `rotation` cannot be expressions | corexy-printer | the frame is held by chains of fixed mates |
| [A-027](#a-027) | Missing capability | A mesh export cannot be turned into the print orientation | corexy-printer | 3MFs in the mating orientation, the README says how to lay them |
| [A-028](#a-028) | Performance | A part shared by several subassemblies is packed once inside each | corexy-printer | box beams on the bed; file size exception |
| [A-029](#a-029) | Performance | A revolved formula curve regenerates 8 to 20 times slower than a polyline of the same outline | corexy-printer | polyline vase |
| [A-030](#a-030) | Bug | An undriven revolute tied to a screw coupling stops converging after about 15 turns | corexy-printer | both lead screws driven |
| [A-031](#a-031) | Agent friction | Pose measures do not reach an instance inside a rigid subassembly; `clearance` does | radial-engine | firing order measured on the subassembly |
| [A-032](#a-032) | Bug | A union along a shared plane with half-revolved pads is refused by the kernel | radial-engine | overrun the plane and cut it away |
| [A-033](#a-033) | Performance | A fillet of seven pad junctions costs 15 to 25 s of CPU | radial-engine | heptagon crankcase with flats |
| [A-034](#a-034) | Performance | `clearance` proves only a coarse lower bound on some near-coaxial bodies, so a bounded fit reads not proven | walker, lamp, printer, radial | bounds widened, or `extent` of each body |
| [A-035](#a-035) | Bug | A face's own appearance is lost on an assembly instance | task-lamp | a separate liner body |
| [A-036](#a-036) | Bug | A free revolute that nothing drives moves in the rest solve | task-lamp | the base turn is a driven parameter |
| [A-037](#a-037) | Missing capability | No assertion of a measure's minimum, maximum or range over the motion; `measure.ray` cannot be asserted | radial-engine | strokes checked against an independent table |
| [A-038](#a-038) | Missing capability | `feature.thread` knows only ISO metric threads | scissor-jack | nominal size and pitch; thread cosmetic |
| [A-039](#a-039) | Agent friction | `motion.check` reports an angle's least and greatest value in radians beside an expectation in degrees | every assembly | convert by hand |
| [A-040](#a-040) | Performance (file size) | A packed assembly carries the thumbnail of every part with public parameters | radial engine (valve train) | barrel fins redrawn as a chained pattern to stay under 1 MB |
| [A-041](#a-041) | Bug | An output of `clearance` is known at the gap found where the same assertion reads not proven | task-lamp (review) | used deliberately: a fit's upper side asserted on the output |

## A-001

**Bug.** `craft3d-cli check-range` on a `.3dcraftasm` that is not packed fails every point: "its instance `Bar` is not
placed: its source `bar.3dcraft` has not been read (assembly.reload reads it)". `craft3d-cli run` opens the same file
and places it; `check-range` passes once the file is packed. **Should:** read the sources as `run` does. Reproducer:
[`findings/A-001-check-range-unpacked/`](findings/A-001-check-range-unpacked/). **Impact:** a subassembly cannot be
range-checked on its own; its parent's check covers it. **Workaround:** `tools/assemblies.py` skips it.

## A-002

**Missing capability.** Instances cannot be repeated by a pattern, linear or circular, with a value that varies per
copy. Seven pistons are seven `instance.add` steps and seven times their mates. `feature.pattern` does this for
features. **Should:** a pattern of instances and of their mates, each copy with its index in formulas.

## A-003

**Missing capability.** The solver knows frames, not geometry (`docs/design/assemblies.md`, *Limits*): a follower cannot
ride a curved face. **Should:** a joint that keeps a point, a line or a face in contact with a curved face, or a joint
whose motion is a function given by a profile. **Workaround:** the follower is driven by a formula of the law that draws
the cam, and the contact is proven by measure.

## A-004

**Missing capability.** A ball mate has no variables (`docs/design/assemblies.md`, *Limits*), so it cannot be driven,
limited or coupled. **Should:** its orientation as variables (Euler angles or a swing and twist) and a cone limit.

## A-005

**Missing capability.** `view.trace` is view state: it is not saved, so an assembly opens without the path that is its
point (a foot, a nozzle). **Should:** a trace that can be kept in the document, as a named object that follows the motion.

## A-006

**Missing capability.** A part's own assertions are not checked per configuration (a known gap, `docs/roadmap.md`), so an
instance placed with other parameters can break its part's checks unseen. **Should:** `document.check` of an assembly
checks every configuration's assertions.

## A-007

**Agent friction.** `overlap` takes `of` and `to`, `clearance` takes `from` and `to`; chapter 17 of the guide shows the
one and lists the other as working "as in a part". And a measure on a subassembly by its name answers "there is no
feature named `Arm`", though it is an instance of the assembly; only a path into it works. **Should:** one spelling, and
a subassembly as a subject, meaning its bodies.

## A-008

**Missing capability.** `craft3d-cli replay` makes a video of how a document is built, with no way to ask for its motion;
`view.replay {motion}` writes frames that have to be encoded by hand. **Should:** a `--motion` option.

## A-009

**Bug.** `motion.check` with an inline `measure` answers "assert.add: there is no assertion named `overMotion1`" when a
`param.set` ran before it in the same run; without the `param.set` it works. **Should:** work the same after a change of
parameters. Reproducer: [`findings/A-009-motion-check-after-param-set/`](findings/A-009-motion-check-after-param-set/).
**Workaround:** `assert.add` a probe instead.

## A-010

**Agent friction.** A measure on a plain instance of a part with two bodies answers "there is no feature named `Handle`",
though `Handle` is the instance; `Handle/First body` works, one body at a time. The other way round, on an instance of
a one-body part the body's path is refused (`Box/Bar`: "there is no feature named `Box/Bar`", in `assert.add` and
`variable.measure` alike), so how a subject is named depends on how many bodies its part has. It extends A-007.
**Should:** the instance's name means all its bodies, and `Instance/Body` always works. Reproducer:
[`findings/A-010-multibody-instance-subject/`](findings/A-010-multibody-instance-subject/).

## A-011

**Agent friction.** A value computed in `instance.add` `params` fails when it is off the part's published `step` ("its
value 9.899… mm is not on its step of 0.1 mm"). A step is what a form or slider offers, not a limit on a value a parent
computes. **Should:** a step limits interactive input and `param.set`, not a parent's `params`; or the refusal says to
remove the step. Reproducer: [`findings/A-011-computed-param-off-step/`](findings/A-011-computed-param-off-step/).
**Workaround:** publish such a parameter without a step.

## A-012

**Performance.** A leg subassembly placed twelve times with `"mode": "flexible"` and `"params": {"t": "t + phase"}` works, but the configuration key of an instance is its parameter values, so every moment of the motion is a new configuration of the subassembly although nothing of its geometry changes: 2097 configurations built and 7.5 s of bake against 3 configurations and 6.5 s with the phase in the parent's mates. **Should:** a parameter that only reaches a subassembly's drives is not a new configuration; reuse the parts and drive the joints. Reproducer: [`findings/A-012-params-t-rebuilds-subassembly/`](findings/A-012-params-t-rebuilds-subassembly/).

## A-013

**Performance.** Twelve legs on one crankshaft: with all 24 hip pivots mated to one chassis instance the bake takes 11 to 13 s; with a rib per leg (4 mates per body) 6.5 s; four legs on one chassis 0.87 s. Three times the legs on one body costs thirteen times the time. **Should:** the solve grows with the bodies, not with the square of the mates on one body (a frame or a crankshaft is the normal case). Reproducer: [`findings/A-013-solver-hub-cost/`](findings/A-013-solver-hub-cost/).

## A-014

**Bug.** While a motion plays in the window the view keeps refitting, so the model appears to zoom and shift. With the
camera on automatic fit (the default for a new tab), `Shell::sync` (`crates/ui-egui/src/shell.rs`, the `auto_fit` test
after `sync_joint_handles`) refits whenever `scene.frame_box()` differs from the box last framed. Each moment of a motion
is a scene of its own whose box is that of the bodies where they are at that moment (`frame_of`, `crates/engine/src/scene.rs`),
so a handle swinging out or a deck sliding changes it at nearly every moment. Nothing in the player holds it. `view.replay`
already avoids this ("framed on the box around every state so the camera does not jump", `docs/design/motion.md`). The
assembly cannot prevent it: the camera is not part of the document. **Should:** while a moment of the motion is shown, frame
on the box over the whole motion, or hold the camera as it was when the play started. **Reproduce:** open any assembly
with a large motion (`assemblies/01-toggle-clamp/toggle-clamp.3dcraftasm`) and play it without having zoomed or panned.
**Workaround:** zoom or pan once before playing (either turns the automatic fit off; orbiting does not).

## A-015

**Bug.** A body with a solid texture (`material.preset` `oak`, `walnut`, ...) placed by an instance's rotation keeps its
texture in the unrotated frame: the grain of a bar turned 60° still runs along the world's x axis and crosses the bar. A
part that a joint turns therefore shows grain that does not belong to it, and over a motion its grain should change as
it turns, so it would not stay on the wood. Seen in the task lamp's oak arms and the Jansen walker's walnut triangles (the
same material reading two ways). **Should:** the texture's frame follows the instance's placement and every moment of a
motion, in every renderer. Reproducer:
[`findings/A-015-solid-texture-ignores-placement/`](findings/A-015-solid-texture-ignores-placement/).
**Workaround:** `{"preset": "oak", "pattern": null}` on moving parts: oak's colour and density without the texture.

## A-016

**Bug.** Every instance of a flexible subassembly starts from the poses stored in that one document, and the parent's rest solve is one Newton solve from them. A leg whose crank lies far from its stored pose converges to the mirrored assembly of a loop and stays there for the whole motion; `assembly.solve` is ok with 0 degrees of freedom and nothing is reported (6 of 432 legs over crank starts every 10°). **Should:** report a branch change against the stored pose, or let a parent give an instance's start pose. Notes: [`findings/A-016-rest-solve-branch-jump/`](findings/A-016-rest-solve-branch-jump/).

## A-017

**Missing capability.** A U-section is formed in one stroke of a punch into a U-die. `bendable` can only put flanges on one line in one stroke ("flanges 0 and 1 cannot be bent in one stroke: they are not on one line"), and two strokes on a press brake collide, as on a real brake. On a part with a single bend `bendable` passes whatever the tools are, since it leaves out the bend's own strip. **Should:** a stroke of parallel bends formed together by a shaped die, and a note on what a single-bend check covers. Reproducer: [`findings/A-017-bendable-one-stroke-u/`](findings/A-017-bendable-one-stroke-u/).

## A-018

**Missing capability.** No sketch command rounds a corner between two lines (`sketch.fillet` is unknown). `sketch.path` can draw the arcs only from end points the author computes, so a variable-driven outline needs long expressions or literal tangent factors, exact at the defaults only. `feature.fillet` afterwards does not reach a sheet-metal flat. **Should:** a sketch corner fillet. Reproducer: [`findings/A-018-no-sketch-corner-fillet/`](findings/A-018-no-sketch-corner-fillet/).

## A-019

**Bug.** The scissor jack's arm built fresh at `inner_width` 34 mm and `tooth_hand` 1 is valid, but the saved part with other defaults fails when `param.set` reaches those values: "plate produced an invalid body: loop 3 of face 2 ... is outside the region they bound". 34.01 mm works. Small root fillets fail non-monotonically (0.25, 0.4, 0.5 mm fail, 0.3 does not). **Should:** a regeneration depends on the values, not on the path to them. Reproducer: [`findings/A-019-param-set-state-dependent/`](findings/A-019-param-set-state-dependent/).

## A-020

**Bug.** `docs/design/assemblies.md` says a screw coupling's two mates may be the same cylindrical mate; `coupling.add {"kind": "screw", "mates": ["Thread", "Thread"]}` is refused: "couples a mate to itself". **Should:** accept it, as the design says. Reproducer: [`findings/A-020-screw-coupling-one-mate/`](findings/A-020-screw-coupling-one-mate/).

## A-021

**Bug, performance.** A sheet-metal flange whose outline uses `sketch.curve` (an involute flank) regenerates and measures fine, but `view.render` at the default framing draws nothing (coverage 0, a box far larger than the body); chords of the same flank frame normally, and the formula curve costs about 13 times the regeneration. **Should:** frame on the body; a formula curve close to a polyline's cost. Reproducer: [`findings/A-021-curve-flange-default-view/`](findings/A-021-curve-flange-default-view/).

## A-022

**Agent friction.** After a chained `sketch.pattern`, `sketch.line {"from": "e4[last]"}` works and `sketch.path {"start": "e4[last]"}` fails ("e6 is a image, not a point"). **Should:** `sketch.path` takes pattern points as the other sketch commands do. Reproducer: [`findings/A-022-path-start-on-pattern-point/`](findings/A-022-path-start-on-pattern-point/).

## A-023

**Bug.** A part with a fillet whose radius is a published parameter, placed with a value too large for it: the part alone fails `document.check` ("radius: too large"), but the instance is placed from a partial regeneration and the assembly's `document.check` is ok. **Should:** an instance whose configuration has a failed feature fails the assembly's check, by name. Reproducer: [`findings/A-023-failed-configuration-reported-ok/`](findings/A-023-failed-configuration-reported-ok/).

## A-024

**Bug.** A part gives a body `material.preset` and a later feature (a boolean) takes that body. The part's own `mass` works; an instance of it answers "has no material, so no mass". **Should:** an instance sees the material its part's final body has. Reproducer: [`findings/A-024-instance-material-before-boolean/`](findings/A-024-instance-material-before-boolean/).

## A-025

**Performance.** A 30-coil spring (a `datum.helix` and one sweep) whose span follows `t` is rebuilt per moment: 200 to 350 ms each, 43 to 75 s for a 120-frame bake. Half-turn revolves in two patterns look the same and cost 5 s; tilted rings cost 0.06 s but read as rings. Collision checks on patterned multi-lump coils also cost 8 to 11 s per moment. **Should:** a helical sweep that is cheap to rebuild at another length, or a spring primitive. Reproducer: [`findings/A-025-helix-spring-per-moment/`](findings/A-025-helix-spring-per-moment/).

## A-026

**Agent friction.** `instance.add` `position` and `rotation` must be plain numbers (`["gap/2", 0, 0]` is refused), so an instance cannot start where the assembly's parameters put it. **Should:** expressions, re-evaluated when the parameters change. Reproducer: [`findings/A-026-instance-position-numbers-only/`](findings/A-026-instance-position-numbers-only/).

## A-027

**Missing capability.** `file.export` to 3MF writes a part in its own axes; a printed part drawn in the frame in which it mates cannot be exported in the frame in which it prints. **Should:** an orientation for the export (a rotation, or a face to lay on the bed). Notes: [`findings/A-027-no-export-orientation/`](findings/A-027-no-export-orientation/).

## A-028

**Performance (file size).** `assembly.pack` packs each subassembly with its own parts inside, so a part used by two subassemblies and by the parent is stored three times. In the printer one 66 KB T-slot profile is packed three times. **Should:** each source once per packed file, whatever subassemblies refer to it. Reproducer: [`findings/A-028-part-packed-per-subassembly/`](findings/A-028-part-packed-per-subassembly/).

## A-029

**Performance.** A thin-walled vase revolved from two `sketch.curve` walls regenerates about 8 to 20 times slower than a polyline of 32 points per wall on the same formula. **Should:** a formula curve close to a polyline's cost. Reproducer: [`findings/A-029-revolve-formula-curve-cost/`](findings/A-029-revolve-formula-curve-cost/).

## A-030

**Bug.** Two lead screws with screw couplings to their nuts on one bed: screw A driven, screw B left undriven but fully determined by its coupling. `assembly.solve` is ok, but `motion.check` stops at about 15.7 turns: "did not converge in 200 iterations". **Should:** an angle that a coupling fixes is solved at any number of turns. Reproducer: [`findings/A-030-undriven-coupled-revolute-turns/`](findings/A-030-undriven-coupled-revolute-turns/).

## A-031

**Agent friction.** In a parent with a rigid subassembly `Sub` holding `Inner`, `clearance` from `Sub/Inner` works, but `rotation` of `Sub/Inner` fails ("no instance Sub/Inner") while `Sub` is accepted. The guide says measures reach inner instances by their path. **Should:** one rule. Reproducer: [`findings/A-031-pose-measure-rigid-subassembly/`](findings/A-031-pose-measure-rigid-subassembly/).

## A-032

**Bug.** A revolved ring and seven pads, each a half revolve whose flat half lies in the ring's plane: the union is refused as "a bug in the kernel; please report the model". **Should:** a union along a shared plane succeeds. Reproducer: [`findings/A-032-coplanar-half-revolve-boolean/`](findings/A-032-coplanar-half-revolve-boolean/).

## A-033

**Performance.** A fillet (or chamfer) of the seven junction edges between cone pads and a revolved ring makes the part take 15 to 25 s of CPU to regenerate, against under 2 s without it. **Should:** seven similar blends cost a small part of a regeneration. Reproducer: [`findings/A-033-fillet-cost-pad-junction/`](findings/A-033-fillet-cost-pad-junction/).

## A-034

**Performance (precision).** `clearance` reports its proven lower bound beside the value it finds. On simple coaxial cylinders the bound is close (found 0.5 mm, at least 0.45, so a fit bounded at 0.2 mm fails as it should). On some bodies the bound is coarse: a printer carriage found 0.5 mm with at least 0.256 mm against a 0.35 mm maximum, a walker key 0.2 with at least 0.0525, a radial piston 0.16 with at least 0. A two-sided fit then reads *not proven* rather than failed or passed, and `document.check` only warns. The same holds between the flat faces of coaxial washers: in the task lamp's review a leather washer moved to 0.15 mm from its bar read "at least 0.089 mm" against a 0.1 mm maximum, so the upper bound of a thin gap cannot fail, and a loosened fit passes a mutation test. **Should:** a bound tight enough to decide a fit of tenths of a millimetre on turned and printed parts. No minimal reproducer: the coarse cases are in the assemblies named.

## A-035

**Bug.** A body's appearance reaches an instance; a face's own (`face.appearance`) does not: a green block with one cream face shows the face cream as a part and green as an instance. The task lamp's shade lost its cream inside. **Should:** an instance shows its part's face appearances. Reproducer: [`findings/A-035-face-appearance-lost-on-instance/`](findings/A-035-face-appearance-lost-on-instance/).

## A-036

**Bug.** In the task lamp, the base's turn left as a free revolute (nothing drives it) ends 7.1° from its start value after the rest solve, with 4 degrees of freedom reported; smaller subsets of the lamp keep it at 0. `docs/design/assemblies.md` says free directions are not moved. **Should:** a free motion keeps its value unless something drives it. No minimal reproducer: the lamp with `Turret_swivel`'s `joint.set` removed shows it.

## A-037

**Missing capability.** An assertion checks a measure at each sample of the motion, but cannot assert what the motion does as a whole: the stroke of a piston (greatest minus least position), the lift of a foot. `motion.check` reports the least and greatest values, but nothing in the document can assert them. Nor can `measure.ray` (a depth along a line) be used in an assertion or an output. **Should:** a measure over the motion (its least, greatest or range) usable in assertions and outputs, and `measure.ray` as a measure kind.

## A-038

**Missing capability.** `feature.thread` knows ISO metric threads only; a lead screw (trapezoidal, ACME, a multi-start T8) cannot be drawn. **Should:** the trapezoidal and ACME families, and starts.

## A-039

**Agent friction.** `motion.check` of a joint angle gives `expected` in degrees and the least and greatest values with `"unit": "rad"`, so a reader compares numbers in two units. **Should:** the values in the expectation's unit.

## A-040

**Performance (file size).** `assembly.pack` stores each part's document as it was saved, and a document with public parameters is saved with its 400 × 300 `thumb.png`. Inside a packed assembly nobody shows those pictures, but they count against the file: in the radial engine with its valve train they took about 216 KB of 1,007,330 bytes (the assembly's own 37.6 KB, the crankcase half 29.8, the piston 28.7, the barrel 23.6, and so on), and a subassembly packs its parts' thumbnails with its own. Together with the uncompressed, pretty-printed archive (examples [F-080](https://github.com/johancoppens/3dcraft-examples/blob/main/3DCRAFT-FEEDBACK.md#f-080), [F-138](https://github.com/johancoppens/3dcraft-examples/blob/main/3DCRAFT-FEEDBACK.md#f-138)) that took the file over its 1 MB budget. **Should:** pack the parts without their thumbnails (they can be drawn again when a part is unpacked), or compress the archive. Reproducer: [`findings/A-040-packed-part-thumbnails/`](findings/A-040-packed-part-thumbnails/). **Workaround:** the barrel's sixteen fins redrawn as one chained pattern (48 KB less), which brings the file to 965 KB.

## A-041

**Bug.** `clearance` finds a gap between a pair of points (an upper bound of the true gap) and proves a lower bound. Where the two are far apart (A-034), an assertion with a `max` reads *not proven*, as it should. The same measure as an output (`variable.measure`) is `known` at the gap found, with no bound, though `variable.measure` says an output is unknown when "what it proves is wider than the document's tolerance". In the task lamp with its turret slot 1 mm wider, one gap reads `known` 0.9 mm as an output, `failed` as a `value` assertion on that output, and `notProven` (at least 0.416 mm) as a `clearance` assertion. **Should:** one contract: the output unknown as documented, or carrying the interval it proves, with an assertion on it saying what the interval decides. Reproducer: [`findings/A-041-clearance-output-known-unproven/`](findings/A-041-clearance-output-known-unproven/). **Used deliberately:** a `value` assertion with a `max` on the output passes exactly when the clearance assertion's `max` would, and fails where that one only reads not proven, so a loosened fit fails a mutation test; the lower side stays with the `clearance` assertion, whose bound is proven.
