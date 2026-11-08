# Feedback for 3DCraft

What building these assemblies showed 3DCraft gets wrong or lacks, collected for the developer to take to 3DCraft in
one go (nothing is fixed from here). Kinds: **Bug** (wrong result, crash, a valid request refused; with a reproducer in
`findings/`), **Missing capability** (phrased for any mechanism and anyone), **Performance** (with numbers), **Agent
friction** (what made building through commands slow or error-prone). See `AGENTS.md` §7. Entries already known from
the examples (`F-nnn`) or the Jigs (`J-nnn`) are cited there, not repeated.

All entries are against 3DCraft `45233bdc` unless they say otherwise.

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
| [A-014](#a-014) | Bug | The window's camera refits at every moment of a motion | seen by the developer while playing the assemblies | the view jumps while it plays |
| [A-015](#a-015) | Bug | A solid texture does not turn with an instance's placement | task-lamp, jansen-walker, seen by the developer while playing | wood grain crosses moving parts; workaround: no texture on moving wood |

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
though `Handle` is the instance; `Handle/First body` works, one body at a time. It extends A-007. **Should:** the
instance's name means all its bodies. Reproducer:
[`findings/A-010-multibody-instance-subject/`](findings/A-010-multibody-instance-subject/).

## A-011

**Agent friction.** A value computed in `instance.add` `params` fails when it is off the part's published `step` ("its
value 9.899… mm is not on its step of 0.1 mm"). A step is what a form or slider offers, not a limit on a value a parent
computes. **Should:** a step limits interactive input and `param.set`, not a parent's `params`; or the refusal says to
remove the step. Reproducer: [`findings/A-011-computed-param-off-step/`](findings/A-011-computed-param-off-step/).
**Workaround:** publish such a parameter without a step.

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
