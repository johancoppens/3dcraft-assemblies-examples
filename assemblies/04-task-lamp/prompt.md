# Prompt: spring-balanced task lamp

The chat a person could paste, turn by turn, into an AI connected to 3DCraft to build the same assembly.

1. I want a desk lamp I would actually want on my desk, in the spirit of the classic spring-balanced task lamp but not
   any brand's design: a heavy round cast-iron base about 180 mm across and 44 mm tall, about 5.8 kg so the lamp cannot tip, enamelled black, with a raised boss in the
   middle. On the boss a brass turret that swivels on a stem held in by a screw from below, with two tall cheeks. Everything has rounded and broken
   edges; nothing looks like a CAD block.

2. Two arms of oak slats, each a parallelogram: two parallel bars, 15 mm wide and 9 mm thick, 330 mm between their
   pivot holes, 30 mm apart at the bottom and 34 mm apart in the upper arm, the two pivots of each pair side by side at the same height,
   one in front of the other. The lower arm goes from the turret to a
   brass triangular elbow plate, the upper arm from the elbow plate to a brass head block. Brass pins through the
   plates, with a real running clearance in the oak and brass cheeks either side of the bars. The parallelograms must
   keep the elbow and the head level whatever the arms do.

3. The head carries a ball on a short stem and the shade hangs from it on a free ball joint: a spun-steel bell about
   170 mm across, deep green enamel outside and cream inside, with a rolled rim, a brass cup around the ball, an E27
   holder and a bulb, the holder screwed into the cup so that it clamps the shade. The ball is a separate brass ball screwed onto the head's hollow stem and locked; the lamp flex (H03VV-F 2 x 0.5, about 5 to 5.9 mm across by its data sheets, flexing radius 7.5 times that) runs down the stem, through the ball and the cup, into the holder's hollow nipple, so it never bends tighter than its data sheet allows; it must go in from the top of the cup and be kept there by a screwed brass cap passed over the stem first. The shade must swivel by hand.

4. Balance it with real extension springs, two on each arm, one on either side of the bars, and do the statics on
   paper first: a spring anchored straight above the arm's pivot and pulling on a pin on the arm balances gravity in
   every pose when its force grows with its length. Use a real spring: music wire 1.6 mm, mean coil 17.6 mm, 26 coils,
   shear modulus 79.3 GPa, with an initial tension from the published range for that spring index, and work out the
   rate and the force from those numbers. It is not a zero-length spring: put the cross pin 180 mm from the pivot on the
   lower arm and 170 mm on the upper, and size the anchor height so the balance is exact at the arm's mean lean. Tell me what is left over against a perfect balance.

5. Draw the springs properly: real wire, the real number of coils, open end hooks that go on the shanks of screwed
   studs on the plates and of a cross pin pressed through the arm, and let each spring lengthen and turn as the arms move. Keep it light enough to play: round the drawn spring's length to a quarter millimetre so moments share it, no full
   helical sweep per frame if that is too slow, but it has to look like a coil and the count has to be right.

6. Make the timeline a sweep of poses: the lower arm from about 28 degrees back to 46 degrees forward of vertical, the
   upper arm between 44 and 108 degrees from vertical, each on a smooth cosine, closing on itself. Store the pose where
   the lamp looks its best at t = 0: the lower arm 10 degrees back, the upper arm at 78 degrees, head over the desk.

7. Give me sliders for the arm length (290 to 350 mm), the base diameter (180 to 220 mm), the shade diameter (150 to
   190 mm) and the base turn (170 degrees either way). The spring anchors have
   to follow by formula so the balance keeps working over those ranges.

8. Give each arm one friction pivot, at its lower main pivot (the turret for the lower arm, the elbow for the upper): a
   tension screw through the cheeks and a leather washer either side of the bar, 0.5 mm thick in a 0.4 mm space so it is
   squeezed, and work out its holding moment from a 100 N clamp and leather on oak at 0.3 (a published value), over two
   faces at the washer's mean radius, and the clamp the fitter must set. Weigh it: use the real masses of the parts in the model. Prove that the net torque about each arm stays within a
   stated pivot friction over the whole sweep, that the lamp does not tip over its base, that the springs stay in
   their stroke and the head stays level; run it over the motion and show me a picture from the side and one in the
   stored pose.

## Acceptance

- 15 parts; 35 instances; 3 degrees of freedom left, all three of the shade on its ball joint; 4 public parameters
  (arm length, base diameter, shade diameter, base turn).
- Measured net torque about each arm's pivots within the stated pivot friction (about 0.29 N m at a stated clamp of
  100 N and a published friction coefficient) at all 73 samples of the sweep, at the defaults and at the corners of the ranges.
- Spring span between its free length plus 50 mm and the span where its stress reaches 45 % of the wire's minimum
  tensile strength, at every sample.
- The head stays level within 0.05 degrees over the motion; the elbow height follows the lower arm's cosine within
  0.02 mm.
- Every pivot's running fits bounded from above and below, including the bar's side play in its slot; the leather
  washers measured to fill their space, squeezed 0.02 to 0.1 mm a side.
- The centre of mass of the lamp stays at least 10 mm inside the base rim, and the shade rim at least 20 mm above the
  desk, at every sample.
- No collisions over the motion other than any listed contacts.
