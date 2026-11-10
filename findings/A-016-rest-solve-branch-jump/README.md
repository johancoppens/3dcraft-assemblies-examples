# One start pose for every instance of a flexible subassembly: the rest solve can land on another branch

Provisional finding (coordinator numbers it) from `assemblies/02-jansen-walker` at 3DCraft `150f0015`.

**What happens.** Twelve instances of one flexible leg subassembly start from the poses stored in that one document
(`position` and `rotation` belong to the subassembly as a whole, so a leg's parts cannot start per instance). The parent's rest
solve is a single Newton solve at the driven values from those poses. A leg whose crank pin lies far from its stored pose
can converge to the mirrored assembly of a loop (another branch of the linkage) and then stays there for the whole
motion: nothing is reported; `assembly.solve` is ok with 0 degrees of freedom.

Measured on the walker (scratch scans, the closed form of the leg against every foot): 6 of 432 legs off the branch over crank start
angles every 10 degrees with the stored pose at 30 degrees of crank; 16, 99 and 40 of 432 with stored poses at 100, 190 and 250
degrees; with the crank pins re-ordered to 0, 60, 120, 180, 240, 300 degrees (the reviewer's mutation), `Aft[6]` was off the
branch. The same parameters with the segments started elsewhere give other legs, so the outcome is sensitive to the start.

**Should.** Either carry a rest solve from the document's stored state along a path (as `view.motion` and `view.drive` do),
or let the parent give an instance of a flexible subassembly per-instance starting poses (or a pose parameter for
the sub's start that is not a drive), or report that a solve converged to a different branch than the start pose.

**Reproduce.** `parts/` of the walker: in a scratch copy of its `build.json` widen the `variable.publish` of `crank_start`
to +-360 degrees, set `crank_start` to `180 deg`, build with `tools/assemblies.py build`-style commands (each part, then
the assembly), and run `motion.check` at 73 samples: `Every foot stays inside the closed-form gait` fails at 70 samples, while the
solve is ok and has no dead points; the default (0 degrees) passes.

**Impact on the assembly.** Workaround used: the published crank start is -120 to 120 degrees in steps of 60; all 45
public values were scanned against the closed form (540 leg solves, none off the branch), and assertions report a
leg off the branch over the motion.
