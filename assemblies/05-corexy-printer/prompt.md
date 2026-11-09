# Prompt: CoreXY 3D printer

The chat a person could paste, turn by turn, into an AI connected to 3DCraft to build the same assembly.

1. I want a working model of a desktop CoreXY 3D printer with a 250 mm square build area. Put the origin at the frame's centre on the floor, z up, y to the rear. Build the frame first: a cube
   of 30 mm black anodised T-slot profile, frame size build size plus 250 mm, held together by printed orange corner
   cubes, one size of profile between the cubes, twelve edges and one extra upright in the middle of each side. Make the
   build size a slider from 200 to 300 mm that resizes the whole frame.

2. Add the moving parts of XY on real rails, sized from the HIWIN catalogue: an MGN12 rail on top of each side rail,
   with an MGN12H block on each; a 3030 beam spanning them with printed ends; an MGN12 rail on the front of the beam
   with a third block carrying a printed toolhead that holds a V6-class hot end by its groove neck (16 mm collars, 12 mm groove) in a
   two-piece clamp, 22 mm heat sink, 23 x 16 x 11.5 mm heater block, brass nozzle, 62 mm overall. The toolhead reaches over
   the beam to four printed belt clamps with a 2 mm serration, and a 30 mm fan sits on the clamp's cap, its air on the fins.

3. Drive it CoreXY, as two belts on two levels 10 mm apart: belt A on the upper level from motor A at the rear left, belt B
   on the lower level from motor B at the rear right, so that R·θA = X − Y and R·θB = X + Y with R the pulley's pitch
   radius. Two NEMA 17 motors (42.3 mm square) at the rear corners, 5 mm shafts, 20-tooth
   GT2 pulleys on them from the Gates tables (pitch diameter 12.73 mm, outside 12.22 mm). A smooth idler made of two
   F695 bearings where the belt's back runs, toothed 20-tooth idlers where the teeth run. Route each belt in the
   standard way, so the belts add up to X and Y. Model the belts as flat GT2 6 mm straight runs along their pitch line
   that lengthen and shorten with the motion and fixed quarter and half wraps at the pulleys. Tie the two motors to the
   carriage and gantry with couplings that come from the CoreXY equations, so the motors are what drives it and the
   carriage only follows.

4. Now Z: a bed on a printed yoke on two MGN12 rails on the side uprights, lifted by two motors with integrated T8 x 8
   right-hand lead screws placed on opposite corners of the frame's sides (front left and rear right), both driven, each with a brass flange nut on a printed plate
   that floats in the bed's nut seat, the way an Oldham coupler does, so a screw standing 0.3 mm off its nominal axis
   pushes the bed only up. The float has to be a real planar joint in the assembly, not a formula.

5. Print a spiral vase on the bed as the timeline plays: a body of revolution, foot radius 36 mm, belly about 34 mm
   wider, a lip that flares at the top, 180 mm tall, wall 0.8 mm. It grows with the timeline from a first ring to full
   height, cut off flat at the printed height. The nozzle runs its rim, one layer of 0.2 mm above the printed height, at
   the wall's centre radius, for six turns, while the bed drops by the height printed. Say clearly it is a time-lapse.

6. Prove it: both motor angles against the CoreXY equations computed from where the carriage and gantry actually are;
   each belt's length constant over the motion, summed from measured positions, and each motor's angle against what
   the belt pays out on its side; the drawn spans reach the pulleys and clamps; the nozzle over the vase's rim at every
   moment, measured against the vase itself; the bed's drop against the screw lead; the floating nuts against the
   misalignment; every carriage clear of its rail with a stated running clearance; and nothing colliding. Sliders for
   build size (200 to 300 mm), vase height (120 to 220 mm), vase belly (20 to 34 mm) and the number of spiral turns (2 to 10).

7. Check it over the whole motion and at the extremes of the sliders, play it, and show me a picture with the print half
   finished.

## Acceptance

- `assembly.solve` is ok with 0 degrees of freedom left; X and Y are sliders on rails, two motors tied by two linear
  couplings of the CoreXY equations; Z is a screw coupling on two lead screws.
- The vase's height follows the timeline; the nozzle's radial distance from the vase axis equals the rim's within 0.02 mm
  and the nozzle is one 0.2 mm layer above the rim within 0.02 mm at every sample of the motion.
- Each belt's measured moving length is constant within 0.02 mm over the motion, and a closed-form total length is stated
  in the README.
- The bed's drop equals the screw lead times its turns within 0.02 mm; each float's measured offset matches the set
  misalignment within 0.02 mm.
- No collisions over the motion at 121 moments, and at the corners of the four sliders, except the listed contacts.
- Black anodised frame, orange printed parts, a blue vase.
