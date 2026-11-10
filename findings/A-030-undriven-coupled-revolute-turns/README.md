# Bug: an undriven revolute tied to a screw coupling stops converging after about 15 turns

Found while building `corexy-printer` at 3DCraft `150f0015`.

**What happens.** Two lead screws, each a `revolute` on a base and a `cylindrical` nut tied to it by a `screw`
coupling, the two nuts fixed on one bed that slides on a `slider` (`repro.json`, `block.json`, `plate.json`). Screw A
is driven by `-24 * 360 deg * t`; screw B is left undriven: its angle is fully determined by the bed's height through
its own coupling. `assembly.solve` is ok at 0 degrees of freedom and the motion runs from `t = 0`, then
`motion.check` answers at `t = 0.653` (about 15.7 turns of the screw): `cannot be measured: the assembly is not solved:
did not converge in 200 iterations (residual 0.676...)`. The printer in this repository failed the same way, at about
15 turns of its second lead screw.

**Should.** A revolute that follows a screw coupling should follow it for any number of turns, as a driven one does.
A guess: the undriven angle's representative is not carried turn by turn (`Solver::advance` and the coupling's
phase, *Couplings* in `docs/design/assemblies.md`), so that after enough turns a restart or a shortened step puts the
undriven angle a whole number of turns off the coupling's value. Not investigated further.

**Reproduce.** `craft3d-cli run --new '{"units":"mm"}' --script block.json --out block.3dcraft`, the same for
`plate.json` and `repro.json` (`--out repro.3dcraftasm`), then
`craft3d-cli run repro.3dcraftasm --cmd motion.check --params '{"samples":73}'`.

**Impact on the assembly.** Workaround used: both screws are driven by the same formula of `t`, as the firmware drives
both motors in the real machine; screw B's coupling is then redundant and consistent, and the assertion that both
screws turn alike holds.
