# Rebuild chat: seven-cylinder radial engine with its valve train

Paste these turns, one by one, into an AI connected to 3DCraft.

**1.** Build a generic seven-cylinder, four-stroke, air-cooled radial aero engine of the 220 hp class (not any
maker's engine), about one metre across, with bore 130 mm and stroke 117.5 mm. Set it up as an assembly with the
crankshaft on the world y axis, the propeller towards −y, cylinder 1 at the top, the cylinders numbered clockwise as seen from the rear, the
propeller end at the front. Give it a cast-grey crankcase in two halves, one source placed twice and split on the
centre line of the cylinders, a rounded heptagon with seven flat cylinder seats and through-bolts at the parting; give it
main bearings around the crank journals, and cut the front half away in a wedge so the rods inside can be seen.

**2.** Make the single-throw built-up crankshaft in two halves with a crank radius of 58.75 mm: a front half with nose, journal,
web and a big crank pin with a spigot, and a rear half with tail, journal and a web that clamps the spigot with a bolt,
counterweights integral with the webs, and a propeller hub on a taper on the nose, held by a nut. On the crank pin goes a one-piece master rod with
a flanged big end: two flange plates carrying six knuckle pins at a 72 mm radius, one every 360/7 degrees, and an
H-section shank to the wrist pin at 235 mm, four crank radii. Six identical articulated rods, each the master rod's length less the knuckle radius (163 mm), swing between the
flange plates on those knuckle pins, closed by a lock plate on each face of the flange. Show polished steel H-section rods with rounded edges, real fits at every pin
and side clearance between rods and plates.

**3.** Make one piston, placed seven times, aluminium with four rings and a floating wrist pin with aluminium plugs, its crown
64 mm above the pin and its skirt only 32 mm below it, so neighbouring pistons clear each other near bottom dead centre, and one
finned cylinder unit, also placed seven times: a dark steel barrel with its fins machined in, held to its crankcase
seat by a flange with eight studs and nuts, and a darker finned aluminium head with a flat-roofed combustion chamber cut 23.7 mm deep into the head above its face, which sits on the barrel's top at the deck; the
piston crown stops 3 mm below that face at top dead centre; and a copper spark plug into the chamber. The cylinder seats
are 224 mm from the axis and the deck, the barrel's top, 360.75 mm (crank radius, master rod, crown height and the 3 mm). Open cylinders 2 and 3 at the front with a section cut so you can see a piston and its rings
inside. Pistons slide on a cylindrical joint in the bore, and the wrist pin stops their roll.

**4.** Drive the crank with one motion: two full turns over the timeline, one engine cycle, closing on itself, with the crank turning
clockwise seen from the rear. Make every moving part a real joint, and leave no degrees of freedom. A crank start angle of 0 puts cylinder 1 at top dead centre on its firing turn. Check the
firing order 1-3-5-7-2-4-6 at a firing interval of 102.86 degrees against how the cylinders are placed.

**5.** Prove the kinematics. Every piston must follow, at every moment, the exact position you can calculate
yourself from the two rod lengths and the crank radius. Measure each cylinder's stroke and top dead centre: the
master cylinder should stroke exactly twice the crank radius, while the articulated cylinders stroke slightly
differently, and because of that each cylinder has its own compression ratio. State the compression ratio of the
master cylinder and how much the others differ. Also measure the clearances: side clearance of rods in the plates,
rods against the crankcase, neighbouring pistons, and show the fits at the pins from above and below.

**6.** Add the valve train. A double-track cam ring with three lobes per track turns at one sixth of the crank speed
against it, driven from the crank through a compound idler (a 24-tooth crank gear drives the idler's 36, the idler's 20 drives an 80-tooth
internal gear in the ring; gears drawn as plain cylinders) in a nose case on the front of the crankcase; the ring is held concentric by a locating spigot on its front face running in a groove of the nose plate, with a stated fit. On each
cylinder give an intake and an exhaust valve side by side across the head, 32 mm either side of the cylinder's centre line and
crosswise to the crank axis, so each rocker swings in a plane parallel to the crank axis and its pushrod runs forward to a
cam track in front of the rods (the two tracks 158 and 186 mm in front of the cylinders' plane); each with a roller tappet in a guide
boss (the roller on an axle pressed into its fork), a pushrod, a rocker on a pin pressed through a bracket, and a poppet
valve on a seat, with two split locks in its stem groove, a retainer and a spring drawn at its 33 mm installed height that does not compress (say so). Keep a constant 0.05 mm
gap between each rocker pad and its valve tip for the lash. Make
each of these one part placed many times, with its pieces as separate bodies that can be put together. Use rockers of 46 to 40 mm arms (valve side to pushrod side), so the valves lift about 11.5 mm. Draw the lobes
from a lift law, tappet lift 10 mm, and drive the tappets and valves by formulas of the same law: a cam is not a joint.

**7.** Prove the timing: 20° before TDC intake opens, 60° after BDC it closes, 65° before BDC the exhaust opens, 20° after TDC it closes,
measured in crank degrees for every valve; the ring at one sixth of the crank; each roller on its lobe and each rocker pad on
its valve tip by measure, not by assumption; piston-to-valve clearance over the motion, which must show the valves near their seats whenever a piston is at the top.

**8.** Keep it light enough to open in a few seconds, with bore, stroke, rod ratio and crank start angle as the
public parameters. Check it for collisions over the whole motion, then play it and show me a picture with the
two opened cylinders toward the camera.

## Acceptance

- 100 instances: the 39 of the engine (7 cylinders, 7 pistons, 7 wrist pins, 6 link rods, 6 knuckle pins, master rod, two crank halves, hub, two crankcase halves) and the valve train (nose case, cam ring, crank gear, idler and its stud, 14 each of tappets, pushrods, rockers and valves); one part placed many times; 0 degrees of freedom; `document.check` ok.
- Bore 130 mm and stroke 117.5 mm within 0.5 mm; master rod 4 crank radii; knuckle radius 72 mm; firing interval 102.86 degrees for every cylinder.
- Cam ring at 1/6 of the crank, against it, within 0.05°; every tappet within 0.1 mm of the lift computed from those crank angles at every moment.
- Rollers and rocker pads in contact (gap within 0.13 mm) at every sample; the cam ring's spigot fit 0.04 to 0.12 mm; every valve at least 25 mm from its piston at every sample.
- Each piston's solved position at every moment within 0.1 mm of the closed-form two-circle intersection of the linkage.
- Master cylinder stroke equals 2 x crank radius within 0.05 mm; articulated cylinder strokes between 117.5 and 119 mm; compression ratio about 5.4 on the master cylinder and between 5.0 and 5.4 on the others.
- Pins with real radial clearance; no collisions at 121 moments of the motion, nor at the corners of the ranges.
- Loads in a few seconds, moves over the whole cycle of two turns without losing a branch.
