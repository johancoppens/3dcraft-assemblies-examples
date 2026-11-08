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
