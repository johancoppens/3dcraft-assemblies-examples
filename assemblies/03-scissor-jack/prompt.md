# Scissor car jack: rebuild chat

Paste these turns, one by one, into an AI connected to 3DCraft over MCP.

1. I want a compact pressed-steel scissor car jack sized after jacks sold as 1 t, the kind that ships in a car's boot. Four
   U-section steel arms of 3 mm cold-rolled sheet, 165 mm from pivot to pivot, make a rhombus. At the bottom the two
   lower arms pivot in a pressed U-channel base welded to a rounded foot plate; at the top the two upper arms pivot in
   a pressed saddle with a rubber pad grooved for a car's pinch weld. Lower arms are wider than the upper ones so the
   upper arms (34 mm inside) nest inside them with 0.75 mm of side clearance when the jack closes. The base's pivots
   stand 31 mm above the ground and the pad's top 41 mm above the saddle's pivots. Yellow powder coat on everything pressed.

2. At the base and at the saddle the two arms must gear together so the saddle stays level. Blank a sector of involute
   teeth into both flanges of each arm around its pivot, ten teeth to the full circle on a 20 mm pitch radius, so the two pivots of a pair stand 40 mm
   apart, 25 degrees pressure angle, stub teeth with an addendum of 0.8 module, 0.4 mm of backlash. Mesh them with real clearance: the two arms of a pair are mirror images, so
   give one of them a half-pitch offset, and make the arm one part in four configurations (lower or upper width, the
   two tooth hands), not four files. Pressed sheet metal with the bend radius and hole-to-bend distances a press tool
   allows, a bend relief wherever a flange runs on past its web, and flat patterns of every configuration I can send to
   the laser.

3. The outer ends of each side's arms meet on a trunnion block carried on headed pins pressed in from outside. One
   trunnion is tapped as the nut, the other is a plain bearing with a brass thrust washer and the screw's collar
   against it. Make the screw 14 mm with 3 mm lead, bright zinc, with a hexagon end; the tail is peened after assembly
   so the nut can't run off. Keep at least 2.5 mm of metal between the pin holes and the screw bore. Add a black folding
   crank: a socket yoke on the hexagon, a real Hooke joint with a cross, a rod tilted 20 degrees and a hinged 110 mm handle with a rubber
   grip, tilted so the handle clears the floor all the way round at the lowest position. Use Ø10 riveted pivots and Ø12 trunnion pins in holes 0.4 mm larger,
   real running clearances everywhere; nothing line-on-line except a thread and press fits, and tell me where those are.

4. Now make it move as a closed mechanism: the screw turns and everything follows through gears, trunnions and
   thread, there and back over t, from the lowest position to the highest with the arms 8.7 degrees above level
   at the bottom and 68 degrees at the top. Nothing placed by formulas of the motion: mates and couplings only, zero
   degrees of freedom left, and the crank's rod through the Hooke joint by its own closed loop. A saddle load of 1000 kg
   as an input the maker can change. Compute the screw tension over the stroke, the thread root stresses, the lead
   angle against the friction angle of a thread friction of 0.15 for self-locking (say what that assumes), with 400 MPa as the assumed yield, the crank torque and the hand force.

5. Prove it: the saddle height against the rhombus closed form at every sample, the saddle level, the trunnion span
   equal to the lead times the turns, the Hooke joint against its own closed form, the handle's lowest point above the
   ground on every turn, teeth that stay clear and engaged, arms clear of each other and of the screw, the pin and shank
   fits two-sided, nothing colliding over the whole motion except the contacts you list and why. Tell me honestly what
   the model does not prove: the load rating, the strength, what the standard requires, and who must verify those. Then
   show me the check, play the motion and render it from a good angle in the raised position.

## Acceptance

The jack solves with 0 degrees of freedom. Arm length 165 mm (arm pivot to pivot), lowest saddle height 121.9 mm ±
0.5, highest 378.0 mm ± 0.5 (arms from 8.7° to 68° above level) with the saddle staying within 0.02° of level and on
the centreline at every sample. The screw advances lead times turns within 0.02 mm. 4 arms, 1 part in 4 configurations,
teeth that mesh with a stated backlash and never overlap, motion over 73 samples with no dead point and no collision
but the listed contacts. Screw lead 3 mm, self-locking with a stated friction assumption. The crank's rod follows a
Hooke joint within 0.001 rad of its closed form and the handle's lowest point stands at least 10 mm above the ground on
every turn at every sample.
