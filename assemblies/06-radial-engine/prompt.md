# Rebuild chat: seven-cylinder radial engine

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
H-section shank to the wrist pin at 235 mm, four crank radii. Six identical articulated rods, each the master rod's length less the knuckle radius (163 mm),
swing between the flange plates on those knuckle pins, closed by a lock plate on each face of the flange. Show polished steel H-section rods with rounded edges, real fits at every pin
and side clearance between rods and plates.

**3.** Make one piston, placed seven times, aluminium with four rings and a floating wrist pin with aluminium plugs, its crown
64 mm above the pin and its skirt only 32 mm below it, so neighbouring pistons clear each other near bottom dead centre, and one
finned cylinder unit, also placed seven times: a dark steel barrel with its fins machined in, held to its crankcase
seat by a flange with eight studs and nuts, and a darker finned aluminium head with a domed combustion chamber
41.7 mm deep, 3 mm of flat gap above the piston at top dead centre, and a copper spark plug. The cylinder seats
are 224 mm from the axis and the head's deck 360 mm. Open two cylinders at the front with a section cut so you can see a piston and its rings
inside. Pistons slide on a cylindrical joint in the bore, and the wrist pin stops their roll.

**4.** Drive the crank with one motion: a full turn over the timeline, closing on itself, with the crank turning
clockwise seen from the rear. Make every moving part a real joint, and leave no degrees of freedom. Check the
firing order 1-3-5-7-2-4-6 at a firing interval of 102.86 degrees against how the cylinders are placed.

**5.** Prove the kinematics. Every piston must follow, at every moment, the exact position you can calculate
yourself from the two rod lengths and the crank radius. Measure each cylinder's stroke and top dead centre: the
master cylinder should stroke exactly twice the crank radius, while the articulated cylinders stroke slightly
differently, and because of that each cylinder has its own compression ratio. State the compression ratio of the
master cylinder and how much the others differ. Also measure the clearances: side clearance of rods in the plates,
rods against the crankcase, neighbouring pistons, and show the fits at the pins from above and below.

**6.** Keep it light enough to open in a few seconds, with bore, stroke, rod ratio and crank start angle as the
public parameters. Check it for collisions over the whole motion, then play it and show me a picture with the
two opened cylinders toward the camera.

## Acceptance

- 39 instances (7 cylinders, 7 pistons, 7 wrist pins, 6 link rods, 6 knuckle pins, master rod, two crank halves, hub, two crankcase halves), one part placed many times; 0 degrees of freedom; `document.check` ok.
- Bore 130 mm and stroke 117.5 mm within 0.5 mm; master rod 4 crank radii; knuckle radius 72 mm; firing interval 102.86 degrees for every cylinder.
- Each piston's solved position at every moment within 0.1 mm of the closed-form two-circle intersection of the linkage.
- Master cylinder stroke equals 2 x crank radius within 0.05 mm; articulated cylinder strokes between 117.5 and 119 mm; compression ratio about 5.4 on the master cylinder and between 5.0 and 5.4 on the others.
- Pins with real radial clearance; no collisions at 121 moments of the motion, nor at the corners of the ranges.
- Loads in a few seconds, moves over the whole turn without losing a branch.
