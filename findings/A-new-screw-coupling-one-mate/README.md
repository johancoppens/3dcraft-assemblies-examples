# A screw coupling cannot name one cylindrical mate twice

`docs/design/assemblies.md` (*Method*, Couplings) says of the screw coupling: "`a` and `b` may be the same cylindrical
mate". `coupling.add {"kind": "screw", "mates": ["Thread", "Thread"], "value": "3 mm"}` is refused with "invalid
document: coupling `Lead` couples a mate to itself". A screw on a single cylindrical mate is the most natural way to
say a thread (the axial and the angular motion of one joint), and the solver's own equation allows it.

Run from this folder (the part first):

    craft3d-cli run --new '{"units":"mm"}' --script parts/block.json --out parts/block.3dcraft
    craft3d-cli run --new '{"units":"mm"}' --script repro.json

Workaround in the scissor jack: a revolute `Screw_in_bearing` drives the turn and the screw coupling joins it to the
cylindrical `Screw_in_nut`; or a `linear` coupling over the mate's two motions.
