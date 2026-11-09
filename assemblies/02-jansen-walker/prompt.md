# Rebuilding the Jansen linkage walker

Paste these turns, one by one, into an AI connected to 3DCraft.

**Turn 1.** I want a walking machine after the linkage Theo Jansen published for his beach animals: a leg of four
plain bars and two triangles that turns a crank's rotation into a long, flat stride and a lift. Use his proportions,
the thirteen numbers a = 38, b = 41.5, c = 39.3, d = 40.1, e = 55.8, f = 39.4, g = 36.7, h = 65.7, i = 49, j = 50,
k = 61.9, l = 7.8, m = 15, with m the crank and the fixed pivot a to the side and l below the axle. One unit is 2 mm,
so the crank is 30 mm; make that scale one parameter. The joints: the crank pin A carries bars j (to C) and k (to the
knee E); the fixed pivot P carries the hip triangle (P to C is b, P to D is d, C to D is e) and bar c (to E); bar f joins D
to F; the foot triangle has E to F = g, E to the foot = i, F to the foot = h. Credit Jansen; call it a Jansen linkage, not a Strandbeest.

**Turn 2.** Everything is laser-cut from 4 mm sheet: birch plywood for the bars, walnut for the two triangles, with
rounded ends and a small chamfer on every edge. Bars are 12 mm wide, pins 4 mm brass rod in 4.2 mm holes, and M4 DIN 125
washers separate the layers. A leg needs three layers so nothing crosses: the bar k alone, then the bars j, c and f, then
the two triangles. Measured from the middle of a throw along the shaft: bar k at 0.5 to 4.5 mm, the bars j, c, f at 5.5
to 9.5, the triangles at 10.5 to 14.5, the crank web at 15.5 to 19.5, the frame rib at 20.5 to 24.5; pairs of legs 100 mm apart.
Work out the pin lengths so every pin is long enough for its stack and no pin passes
through a bar it does not carry.

**Turn 3.** Twelve legs, in six pairs: in each pair the same leg twice, the second turned half a turn about the vertical,
so one leg steps forward of the crank and one behind. A leg should be one part I place twelve times. The legs of a pair
share one crank throw: a crank pin held between two birch webs, with the bars of both legs on it and washers between
them. The throws sit on one crankshaft: six identical throws, each two webs and a crank pin, joined by brass journal rods with
a filed flat at each end that fits a D-shaped hole in the webs; the turn between a rod's two flats is the phase between
its two throws, in 60 degree steps, in the order that keeps the most feet on the floor. One hand crank drives the shaft at one end,
keyed to its last rod the same way.

**Turn 4.** The frame is a row of birch ribs, one for each leg, joined by two walnut dowels along the top, above
everything that moves. Each rib carries the bearing for the journal and a glued-in brass hip pin for its leg. Check that
the dowels and the ribs stay clear of every leg over a whole turn.

**Turn 5.** It walks on a floor: dark boards, each as wide as the distance the floor must travel in one turn so that a foot in
its stance stays still on the boards (280 mm, 140 units), with fixed dark platforms at both ends that hide where the moving boards end, so the
motion loops without a jump. The timeline is one crank turn and the floor moves exactly one board in that time.

**Turn 6.** Now check that it really is a machine. One crank turn, no degrees of freedom left, nothing collides at
121 moments of the turn, the foot of one leg sits exactly where the circle intersections of the numbers put it at every
sample, and over the turn at least four feet are within 0.75 mm of the floor, the feet slip at most 3.8 mm on the boards while
they carry the machine, and the centre of mass stands inside the feet that are down. Then play one turn and give me a picture in
mid-stride from a low three-quarter view.

## Acceptance

- Twelve legs in six mirrored pairs on one rigid crankshaft of six throws at 60 degree phases, the phase fixed by a real key
  (a flat on the journal rods in D-shaped web holes), a hand crank on one end, no degrees of freedom left, one driver (`t` is one crank turn).
- Jansen's thirteen numbers (m = 15 is the crank) at a scale parameter, credited in the model's description.
- Bars 4 mm birch, triangles 4 mm walnut; 4 mm brass pins in 4.2 mm holes; washers between the layers; pins long
  enough for their stacks; no collisions at 121 moments of the motion.
- At every sample of a turn (73 or more): the reference foot within 0.01 mm of the circle intersections of the
  numbers; at least 4 feet within 0.75 mm of the floor; the centre of mass inside the feet on the floor; slip
  at most 3.8 mm; the floor travels exactly one board per turn and loops.
- A dark floor of boards with fixed end platforms; birch, walnut and brass in the picture, mid-stride.
