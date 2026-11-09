# Seven-cylinder radial engine

A generic seven-cylinder four-stroke air-cooled radial of the 220 hp class, drawn at full size: a two-piece cast-grey
crankcase cut away at the front, a built-up single-throw crankshaft in two clamped halves with integral counterweights
and a copper propeller hub on the taper of its nose, a one-piece master rod whose flange carries six articulated rods
on knuckle pins, seven pistons with rings on floating wrist pins with plugs, and seven finned cylinders, each held to
its seat by eight studs and nuts, two of them opened to show a piston. One crank turn of `t` drives everything
through mates; the seven piston-and-rod loops are solved as one mechanism, which no simple formula gives, and the
model measures the difference between the cylinders that the master-and-articulated rod system really has.

![The radial engine with its crankcase cut away and two cylinders opened](preview.png)

## What it shows

- **Seven closed loops on one master rod** (`mate.add` `cylindrical` and `revolute`, a variable `Crank_drive_angle` driving the crank).
  Six articulated rods hinge on knuckle pins in the master rod's flange (`Knuckle_2` … `Knuckle_7` fixed,
  `Link_2` … `Link_7` revolute); each piston slides in its bore on a `cylindrical` mate and its roll is stopped by
  the wrist pin revolute, as in the real thing. `assembly.solve` leaves 0 degrees of freedom. The motion is one
  driver: the variable `Crank_drive_angle`, a formula of `t`.
- **A rigid subassembly placed seven times** (`parts/cylinder.json`, an `assembly.new` script): the barrel and head
  are one unit, placed by `instance.add` with its bore and deck height in `params` and mated by name through the
  subassembly (`Cylinder[3]/Barrel/Mount`).
- **One source placed twice:** the crankcase is drawn as a half with its parting plane at the cylinder centre line;
  placed twice (the front half turned about the cylinder 1 axis), a `section_cut` parameter cuts the front half open
  and carries the through-bolts.
- **Configurations by `params`:** two opened cylinders (`open_section`) are configurations of the same source
  (a `when` on the section cut); the piston, barrel and head follow `bore`, the rods follow `rod_ratio`, the crank
  follows `stroke`.
- **A measured difference between cylinders.** `jointDistance` of each piston's cylindrical mate is asserted
  against an independently derived closed form at every sample (`assert.add`, `motion.check`); each cylinder's top
  and bottom dead centre and compression ratio come out different from the master cylinder's. This is the real
  thing's behaviour, not a model artefact: see *The motion*.
- **Firing order as a check of the model.** The cylinders' placement is measured (`rotation`) against the table of
  the firing sequence 1-3-5-7-2-4-6 at intervals of 720°/7.

## The real thing

**References read** (and what each gave):

| Source | What was read | Used for |
|---|---|---|
| Wikipedia, *Continental R-670* (fetched 2026-11-08) | 5 1/8 in (130.2 mm) bore, 4 5/8 in (117.5 mm) stroke, 668 cu in, 5.4:1 compression, 42.5 in (1079.5 mm) diameter, 450 lb, 225 hp at 2175 rpm, seven cylinders, enclosed valve gear | The class: bore, stroke, compression ratio, overall diameter |
| *Continental's Radial Aircraft Engines*, enginehistory.org | The R-670's forged barrels, "machined all over with integral cooling fins", screwed and shrunk into cast aluminium heads; a one-piece master rod with a steel-shelled white-metal bearing and six link rods on knuckle pins with lock plates, H-section rods; a built-up crank with a bolted clamp; a double-track cam ring | The construction of the cylinders, rods and crank |
| FAA-H-8083-32B *Aviation Maintenance Technician Handbook — Powerplant*, chapter 1 | Master-and-articulated rods, knuckle pins (pressed or full-floating, lock plates), "the knuckle pin holes … are not equidistant from the center of the crankpin" to compensate for the elliptical knuckle paths; cooling fins 0.090–0.060 in; cylinder numbering (clockwise from the rear, No. 1 at the top); firing order 1-3-5-7-2-4-6; figure 1-27: a three-lobe cam for seven cylinders turns at 1/6 of the crank, against it | Fits, fin proportions, cylinder numbering, firing order; the cam ring ratio for stage 2 |
| G. D. Angle, *Positioning of Link Rod Wrist Pins in Articulated Connecting Rods*, Aviation Engineering, January 1932 | L/R "3.2 to 4.4"; the link radius kept small to limit bending of the master rod; strokes of link cylinders come out longer and differ with the link radius and its angle to the rod axis, and equal strokes need a different link radius per cylinder | The rod ratio of this model (L/R = 4), and the reason its cylinders differ |

Everything else (crank pin 70 mm, knuckle pin 26 mm, wrist pin 34 mm, flange and web sizes, the fit values, the fin
pitch and the counterweights) is my own judgement of the class, stated here and not proven to any manufacturer's
drawing. The enginehistory.org details are of the A-70, the R-670's predecessor, whose layout the R-670 kept. The
model's overall diameter across the cylinder heads is about 945 mm, against the 1079.5 mm quoted for the R-670 with
its rocker gear. **This model is a demonstration: it is not a design and carries no load calculations.**

**Fits as drawn** (each measured as a radial gap): knuckle pin in the master flange 0.01 mm (drawn as the pressed fit,
FAA's first case: a nominal gap in place of interference, so it reports no overlap, and the pin is fixed to the rod);
knuckle pin in its rod 0.02 mm; wrist pin in the piston bosses 0.015 mm and in the rods 0.02 mm; big end on the crank
pin 0.05 mm; main journals in their bearings 0.05 mm; piston in the bore 0.16 mm; rings in the bore 0.05 mm. Bearings
are drawn as plain bores of the stated gap, where the R-670 has roller main bearings (enginehistory.org, of the A-70).

**Materials and processes.** The crankcase is a two-piece casting split on the centre line of the cylinders, cast grey:
a rounded heptagon whose seven flats are the machined seats of the cylinders, the corners cast with a 16 mm radius, the
rear wall drafted into its ring and bearing boss (asserted with `draft`) and rounded into the boss, seven ribs on the
rear wall. **There is no fillet at a pad junction, because there are no pads:** round pads on a round ring with a 3.5 mm
rolling-ball fillet at the junction cost 12 to 27 s of CPU for that one part (`findings/A-033-fillet-cost-pad-junction/`;
the budget for the whole engine is 12 s), so the crankcase became a heptagon whose flats need none. The heptagon's sides
and corners and the ribs are drafted 1.2° and 1.5° from the parting plane (`feature.draft`), and one patterned cut
machines the seven seats flat again so the flanges sit square; the cut covers the flange, the rest of each side stays
drafted. Draft is asserted on a cast corner of the heptagon, a face that runs along the pull (1 to 1.4°). Core prints,
machining allowances and wall sections are not modelled, and it is not a foundry pattern. The cast heads have no draft
or fillets beyond their fin profile. The crank webs are rounded into the journals (2 mm) and the front web into the crank
pin (1.5 mm), by arcs in the turned profiles; the webs' own edges are sharp.
Crank halves, rods, knuckle pins and wrist pins are alloy steel forgings, ground and polished (one-piece master rod, as
on the R-670's predecessor A-70, so the crankshaft is built up). Pistons are forged aluminium with cast-iron rings, four
to a piston, drawn alike; the wrist pin is full-floating with an aluminium plug in each end against the bore. Barrels
are alloy steel forgings machined with integral fins, nitrided in the bore; heads are cast aluminium with a
spherical-cap chamber (a 41.7 mm cap of R 71.5), screwed and shrunk on (this model shows the barrel and head meeting at
a single seat). Fins taper from 2.3 to 1.5 mm, FAA-H-8083-32B's 0.090–0.060 in. The propeller hub is a copper-plated
forged steel hub on the taper of the crank nose, held by a retaining nut on the threaded end (the thread is not drawn,
nor is the hub's key).

**The counterweights are integral with the crank webs** and are not sized to balance: the two webs' sectors put about
350 kg·mm about the crank axis (computed from the drawn outline at 7.85 g/cm³), against a rough 900 kg·mm that a reviewer estimated for this class (an estimate, not a sourced figure; the reciprocating
and rotating masses are not modelled, and no balance is claimed). Larger sectors would
reach the piston skirts at bottom dead centre.

## Parts and assembly order

| Part | Instances | Process |
|---|---|---|
| Crankcase half | 2 (rear whole, front cut away) | Casting, machined seats, through-bolted on the parting plane |
| Crank, front half (nose, journal, web with counterweight, crank pin with spigot) | 1 | Forging, machined |
| Crank, rear half (tail, journal, web with counterweight, clamp around the spigot, clamp bolt and nut; the halves are drawn without a key) | 1 | Forging, machined |
| Propeller hub with retaining nut | 1 | Forging, machining, copper plate |
| Master rod with lock plates (drawn without their screws) | 1 | Forging, machining |
| Articulated rod | 6 | Forging, machining |
| Knuckle pin | 6 | Turning, hardening |
| Piston (with rings) | 7 | Forged aluminium, turned; cast-iron rings |
| Wrist pin with plugs | 7 | Turning, hardening |
| Cylinder (barrel with eight studs and nuts + head, rigid subassembly) | 7 | Forged barrel with machined fins; cast head; screwed and shrunk |

Assembly order, part by part, each step reachable from the side the next part leaves open:

1. On the bench, the six articulated rods go between the plates of the master rod's flange with their knuckle pins
   pressed in, and the lock plates close the pins' ends on both sides.
2. The rod group's Ø200 flange and Ø70.1 eye go over the crank pin of the front crank half, where it stands free,
   since the rear web is not on it yet. Then the rear crank half is put on the spigot and clamped by its bolt.
3. The crank's rear journal is put into the rear crankcase half, then the front half is closed on the front journal, and
   the two halves are bolted through the ring by the seven through-bolts, each with a head on one side and a nut on the other.
4. The studs are screwed into the seats, seven times eight; each cylinder's skirt enters its seat and its flange goes over
   the studs. Before a cylinder goes on, its piston is put on its rod with the wrist pin and plugs (the pistons are
   reached through the open seat), and the rings are compressed into the barrel as it comes down.
5. The hub goes on the taper of the nose and is held by its nut.

## The motion

`t` is one full turn of the crankshaft: `Crank_drive_angle = start_angle + 360 deg * t`. The crank pin carries the
master rod; the master rod's piston (cylinder 1) moves as a plain slider-crank. The six articulated rods swing on
their knuckle pins, whose paths are not circles, and drive pistons 2 to 7. There is no free degree of freedom; the
crank turns clockwise seen from the rear, and the cylinders are numbered the same way, No. 1 at the top.

Because all six knuckle pins sit at one radius, the cylinders do not all behave alike. The table below gives the
piston's distance from the crank axis at top and bottom dead centre, from a separate numerical solution of the
linkage with no 3DCraft in it (a Newton iteration on the loop equations, 72,000 steps per turn). The model agrees: at
one sample per degree of crank `motion.check` of the pistons' `jointDistance` reads strokes of 117.50, 117.56,
118.61 and 118.26 mm (the small differences from the table are the sampling: an extreme falls between samples).

| Cylinder | TDC distance, mm | BDC distance, mm | Stroke, mm (independent) | Crank angle at TDC | Compression ratio |
|---|---|---|---|---|---|
| 1 (master) | 293.75 | 176.25 | 117.50 | 0.0° | 5.40 |
| 2 and 7 | 291.78 | 174.21 | 117.56 | 53.0° / 307.1° | 5.10 |
| 3 and 6 | 291.02 | 172.41 | 118.61 | 108.6° / 251.4° | 5.03 |
| 4 and 5 | 293.29 | 175.02 | 118.27 | 157.5° / 202.5° | 5.35 |

An articulated cylinder's top dead centre is off the master's by up to 2.7 mm and off its nominal crank angle by up to
6°; its stroke is up to 1.1 mm longer. With one combustion chamber per cylinder that gives compression ratios from
5.03 to 5.40. This is uncorrected on purpose: the difference is the point of this model, and it is what a real radial
designs out, by giving each knuckle pin its own radius from the crank pin (Angle, 1932; FAA-H-8083-32B). The firing
order and the 102.86° firing interval are part of the model, at the *nominal placement of the cylinders only*. The
pistons' own top-dead-centre intervals are uneven (108.6, 94.0, 104.5, 105.9, 104.5, 94.0, 108.6°, from the table
above); this engine compensates nothing, neither in the rod geometry nor with a compensated magneto as FAA-H-8083-32B
describes, and fires at nominal placement.

## Parameters

Public parameters (`variable.publish`): **bore** (126–134 mm), **stroke** (116–122 mm), **rod ratio** (3.95–4.20, the
master rod length over the crank radius), and **start angle** (0–355°, where the crank stands at `t` = 0). The ranges
are limited by the pistons of neighbouring cylinders: their skirts come close near the bottom of the stroke (the
clearance is asserted over the motion at every corner of these ranges). A short stroke with a short rod would collide. The piston, barrel and
head follow `bore`; the crank, the rods and the deck height follow `stroke` and `rod ratio`.

## Checks

At rest (`document.check`): every mate solved, 0 degrees of freedom; the fits of a representative set of pins (the
knuckle pin in the master flange and in its rod, wrist pins in the bosses and rods, the big end) and of the two main
bearings, the crank-pin spigot and the hub on its taper, measured from above and below; every piston's and ring pack's diameter against the bore, and the barrels by volume (barrel 1 against an independent
integration of its profile, the others against barrel 1); the firing order against the measured placement of
every cylinder; and the master cylinder's compression ratio. **That ratio is not an independent measurement of the
chamber:** the head's measured volume is subtracted from a constant calibrated from this same head (its measured volume
at the defaults plus the design cap volume), so it detects a head that has changed, and away from the nominal sizes it
falls back to the formula and its bound (2 to 12) cannot fail. A direct measure of the dome depth is not available:
`measure.ray` is a command, not something an assertion or an output can use. Barrel 1's volume is checked against an
independent Pappus integration of its drawn profile (754,706.9 mm³, at the default sizes); barrels and heads of
cylinders 4 to 7 against cylinder 1, those of the opened 2 and 3 against the share that the section cut leaves. The rear
half carries the casting's `draft` check on a corner that runs along the pull.

Over the motion (`motion.check` at 73 samples; all of it *at the samples*):

- every piston's solved `jointDistance` against an independent closed form of the linkage (the master rod's triangle
  and the two-circle intersection for each articulated rod), to 0.02 mm;
- every cylinder stays within its top and bottom dead centre from the independent table and reaches them within
  0.15 mm at the sample nearest (the table is for the default sizes; it is switched off away from them, while the
  closed form holds everywhere);
- master cylinder TDC and BDC exactly rod plus and minus crank radius (R ± L);
- clearances: a rod's side clearance to the master flange, rods to the crankcase, adjacent rods (a constant 20.5 mm that
  only states the flange spacing), neighbouring pistons, piston to crankcase, master rod small end to the piston bosses.

No collision at 121 moments at the defaults and 31 at each corner of the ranges (`view.motion` with `collisions`,
`tools/assemblies.py check`); no contacts need listing.

What the samples do not cover: between samples, and sizes between the defaults and the corners (the closed form
still holds there, the independent table does not apply). The compression ratios above come from the independent table of TDC
and BDC distances (`motion.check` confirms that table to 0.15 mm near each extreme) with one common chamber volume: a real
engine's cylinders are not identical.

## Files

`parts/*.json` and `build.json` are the sources; the packed `radial-engine.3dcraftasm` and `exports/radial-engine.step` are
written by `tools/assemblies.py build`. `preview.png` by `tools/assemblies.py render`.

## Rebuild

`tools/assemblies.py build radial-engine`, then `tools/assemblies.py check radial-engine`.

## Difficulty

7 out of 10 (reviewer): seven closed loops on one master rod solved as one, a rigid cylinder subassembly placed
seven times, a built-up crank and a halved case placed twice by configuration, and closed-form proofs over the motion;
no couplings or configurations that follow `t`.

## Platform notes

`clearance` between coaxial cylinders with a small gap comes back not proven (piston and rings in the bore, found 0.16 and
0.05 mm, "at least 0 mm"), so the piston and ring diameters are asserted by `extent` along the crank axis instead, and the
barrels are compared by volume. Pose measures (`rotation`, `position`) refuse an instance inside a rigid subassembly while clearance reaches the same
path by its body name: `findings/A-031-pose-measure-rigid-subassembly/`; the firing-order assertions measure the
subassembly itself as a workaround. The barrel and head set their material on their last feature as well (`findings/A-024-instance-material-before-boolean/`: a material set before a later feature is lost to an instance, here even when that feature is switched off by `when`). There is no way to assert a measure's minimum or maximum over the motion; the stroke of
each articulated cylinder (an extreme that falls between crank angles nothing can name) is therefore bounded by
per-cylinder values from the independent calculation, and read from `motion.check` for the README.

**The valve train of the brief's stage 2 (a cam ring at 1/6 of the crank speed against it, with tappets, pushrods,
rockers and valves) is not part of this model.**
