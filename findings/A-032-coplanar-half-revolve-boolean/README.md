# Union of half-revolved pads with a shell they share a plane with is refused

**3DCraft 150f0015, found in 06-radial-engine.** A revolved ring (y >= 0) and seven pads, each a half revolve about its
own axis so that their flat half lies in the ring's plane y = 0: `feature.boolean` union fails with "the result is not
the boolean of its operands and was refused (a bug in the kernel; please report the model): face 3 of the tool, out of
the other's reach, is not in the result as it was". Expected: a union along a shared plane is a valid boolean.

`craft3d-cli run --new '{"units":"mm"}' --script repro.json`. Workaround used: the shell and pads overrun the plane and
one block removes everything below it afterwards.
