# Catalogue: the six assemblies

The brief for every assembly: what the real thing is, how it moves, what it must show of 3DCraft, its line of the
palette, its public parameters, what it must prove, and its risks. The order runs from simple to complex. Sizes named
here are starting points: the builder verifies every number against the standard or source and cites it.

A builder may improve a brief (a better standard, a better parameter), but changes its domain, its main techniques or
its palette line only with the coordinator.

## Simple

### 1. Horizontal toggle clamp · `toggle-clamp` · workshop, sheet metal
- **Real thing:** a horizontal hold-down toggle clamp of the common 100 to 200 kgf class, stamped and formed from
  zinc-plated steel sheet: a base of two mirrored L-halves, a U-bar clamp arm carrying an M6 spindle with a rubber
  pressure cap and two lock nuts, a stamped handle with a red PVC grip, a stamped link, and rivet pivots. A real clamp's
  proportions, cited. The steel parts are real sheet metal in 3DCraft (`feature.sheetMetal`, flat patterns as DXF).
- **Motion:** a four-bar: base, clamp arm, handle, link. `t` drives the link's joint from open, through the strekpunt
  (the line through the three toggle pivots), to the stop just past it, and back.
- **Shows:** one closed loop, `limits` on a joint, the over-centre position, one pivot part in several configurations,
  a joint value as an output (`variable.measure`) for the mechanical advantage.
- **Look:** bright zinc, red grip, black rubber.
- **Parameters:** workpiece height (sets the spindle), handle opening at rest; a third if it earns its place.
- **Proves:** the clamped pose is past the toggle line by a stated small angle (assert the joint angle: a dead point is
  not reported between frames); the spindle tip reaches the workpiece at the clamped pose (closed form); the handle
  rests on its stop; the arm opens wide enough to load a workpiece; pivots have real fits.
- **Risks:** the toggle geometry decides everything: work it out first, on paper, against a real clamp.

## Difficult and complex

### 2. Jansen linkage walker · `jansen-walker` · kinetic art, laser cutting · complex (reviewer's score 7)
- **Real thing:** a hand-cranked walking model in laser-cut 4 mm birch plywood with brass pins, after the linkage of
  Theo Jansen, from his published proportions (the eleven "holy numbers"), credited. Twelve legs on one crankshaft. The
  title says "Jansen linkage": "Strandbeest" is his name for his works.
- **Motion:** `t` is one crank turn. It should visibly walk: a floor of boards that moves back under the feet by exactly
  one board per turn loops without a jump, and the feet stand still on it during the stance.
- **Shows:** a leg as a flexible subassembly placed many times, undriven, on one real crankshaft of keyed segments that
  sets the phases; one bar part in several configurations; many closed loops in one solve; the foot's path as a trace.
  (A phase through `params` works but rebuilds the leg at every moment: A-012.)
- **Look:** birch plywood bars, walnut triangles, brass pins, a dark floor.
- **Parameters:** overall scale, crank start angle; a third if it earns its place.
- **Proves:** a foot's position at a key moment against the linkage's own circle intersections; stride and lift; at
  every sample enough feet are on the floor and the centre of mass stands inside them; the feet's slip in the stance
  within a stated bound; no collisions over the motion, so bars sit in real layers with real spacers.
- **Risks:** the layering of the bars; instance count against the budget; only the real plywood stack makes it makeable.

### 3. Scissor car jack · `scissor-jack` · automotive, sheet metal
- **Real thing:** the compact pressed-steel scissor jack carried in a car: base, saddle, four pressed U-section arms with
  gear-tooth ends, two trunnions (one a nut, one a bearing with a thrust washer), a lead screw and a folding crank.
  Candidate standard: EN 1494; rated load about 1 t, verified or stated as not proven.
- **Motion:** `t` turns the screw from the lowest position to the highest and back. The gear teeth keep the saddle level.
- **Shows:** a screw coupling and gear couplings inside a closed loop; pressed sheet-metal parts with their flat patterns;
  one arm part mirrored by placement; a measured output that follows the motion (the screw force).
- **Look:** safety-yellow powder coat, zinc-plated screw, black crank.
- **Parameters:** arm length, screw lead; a pose if it earns its place.
- **Proves:** lift height against the rhombus closed form at several moments; saddle level over the whole motion; screw
  self-locking (lead angle below friction angle, with its assumptions stated); screw force over the stroke; arms clear
  of each other and of the screw over the motion.
- **Risks:** teeth as geometry against a gear coupling that only knows the ratio; mating threads (F-014).

### 4. Spring-balanced task lamp · `task-lamp` · product design, lighting
- **Real thing:** an original two-arm desk lamp balanced by extension springs: oak arms in parallelograms, brass pivots, a
  heavy painted base, an enamelled spun-steel shade and an E27 lamp. A generic type, not any brand's design.
- **Motion:** `t` moves the lamp through a sweep of poses. The shade swivels by hand on a ball joint.
- **Shows:** parallelogram loops; springs that are configurations following `t`; a ball mate left free; mass from materials;
  the balance of forces as a check over the motion.
- **Look:** oak and brass, deep green enamel, cast-iron black base.
- **Parameters:** arm length, shade weight or spring rate, base diameter; at most four.
- **Proves:** the net torque about each arm pivot stays within the pivots' friction in every pose (the lamp stays where
  you leave it); the centre of mass stays over the base in every pose, so it does not tip; springs stay within their
  stroke; nothing collides. The balance is computed from measured masses and joint angles, not assumed.
- **Risks:** a helical spring rebuilt per frame against the bake budget: probe it first, and find the cheapest honest
  spring; a ball mate's free turns.

## Complex

### 5. CoreXY 3D printer · `corexy-printer` · 3D printing, machine building
- **Real thing:** a desktop CoreXY printer about 250 mm cubed: a T-slot frame, linear rails, NEMA 17 motors, GT2 belts,
  a Z bed on lead screws, a hot end. Standards and data sheets for the rail, motor and belt sizes.
- **Motion:** `t` plays a spiral-vase print: the nozzle runs the rim of a vase that grows with `t`, the bed drops, the
  motors turn, the belts follow. A time-lapse, and the README says so.
- **Shows:** linear couplings for CoreXY; a screw coupling for Z; one T-slot part placed with a length per instance
  (copied from `3dcraft-examples`' `t-slot-profile`, at the pin, credited); configurations following `t` (belts, the
  vase); subassemblies; a planar mate for the Oldham coupling on the lead screw; a nozzle trace.
- **Look:** black anodised frame, orange printed parts, a blue vase.
- **Parameters:** build size, vase shape or height; at most four.
- **Proves:** each motor angle against the CoreXY equations; the length of each belt constant over the motion; the nozzle
  on the vase's rim at every sample; the bed's travel; nothing collides. The GT2 pulley is drawn here from Gates' published
  tooth data; no share-alike source (AGENTS.md §1).
- **Risks:** instance and configuration count against the budget; the Jigs' drag chain is not at the new bar, so draw a
  simple cable chain only if it earns its cost.

### 6. Seven-cylinder radial engine · `radial-engine` · aviation, engines
- **Real thing:** a generic seven-cylinder four-stroke air-cooled radial, not any maker's engine: a crankcase cut away to
  show the master rod, six articulated rods on knuckle pins, pistons with rings, finned cylinders, a single-throw crankshaft
  with counterweight and a propeller hub. Proportions from a stated real class of engine.
- **Motion:** `t` is a full crank turn. The firing order and its 102.86° interval are part of the model.
- **Shows:** seven closed loops on one master rod, which no simple formula gives; `cylindrical` pistons; a cylinder placed
  seven times; a measured stroke per cylinder over the motion; a rigid subassembly for a cylinder.
- **Stage 2, the valve train:** a cam ring turning at 1/6 of the crank speed against it, with tappets, pushrods, rockers and
  poppet valves, driven by formulas of the same law that draws the cam (a cam is not a mate). Built after stage 1 passes;
  kept only if it passes every check and stays within the budget, and reported either way.
- **Look:** cast-grey crankcase, dark finned steel cylinders, bright rods and pistons, a copper accent.
- **Parameters:** bore and stroke, rod ratio, start angle; at most four.
- **Proves:** the master cylinder's stroke against 2 × the crank radius; each articulated cylinder's measured stroke, and the
  compression ratio per cylinder from it (a real difference between cylinders); rods clear of each other and of the crankcase
  at every sample; the firing interval. With stage 2: piston-to-valve clearance, and lift against the law.
- **Risks:** the master rod's flange against the knuckle pins and rods; load time of the finned cylinder and the crankcase.

## Palette

| # | Assembly | Line |
|---|---|---|
| 1 | Toggle clamp | bright zinc, red grip |
| 2 | Jansen walker | birch, walnut, brass |
| 3 | Scissor jack | safety yellow, zinc |
| 4 | Task lamp | oak, brass, deep green enamel |
| 5 | CoreXY printer | black anodised, orange, blue |
| 6 | Radial engine | cast grey, dark steel, copper |

## Coverage

What each assembly must carry, so that the six together show what assemblies can do:

| | 1 Clamp | 2 Walker | 3 Jack | 4 Lamp | 5 Printer | 6 Engine |
|---|---|---|---|---|---|---|
| Closed loops | one | many | yes | yes | | seven |
| Couplings | | | screw, gear | | linear, screw | stage 2: gear |
| Limits | yes | | yes | yes | yes | |
| Configurations by `params` | pins | bars | | arms | T-slot lengths | |
| Parameters following `t` | | | | springs | belts, vase | |
| Subassemblies | | flexible | | | rigid | rigid |
| Other mates | | | | ball | planar | cylindrical |
| Formula-driven contact | | | | | | stage 2: cam |
| Trace | | foot | | | nozzle | |
| Forces from the model | advantage | balance | screw force | spring balance | | |
| Sheet metal with flat patterns | base, U-bar, stampings | | arms | | | |
