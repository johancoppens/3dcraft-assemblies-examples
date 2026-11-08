# Prompt: horizontal toggle clamp

The chat a person could paste, turn by turn, into an AI connected to 3DCraft to build the same assembly.

1. I want a working model of a horizontal hold-down toggle clamp, the small kind for a jig or a bench, sized like a
   900 N, M6 catalogue clamp, with every steel part real sheet metal of 2.5 mm low-carbon steel, inner bend radius one
   thickness, zinc plated. Measure every position back from the base's front edge and up from the bench, with the
   bar horizontal at the clamped pose. Start with the base: two mirrored formed L halves, each a flange and an upright ear, 37 mm
   long, 39.8 mm wide over both flanges, with mounting slots on a 26.2 by 28.4 mm pattern and a round hole in each
   flange. One source with a left/right parameter that mirrors it, placed twice. Export each flat pattern as DXF.

2. Make the U-bar from one blank: a narrow web at the tip with two legs bent back from it, 6.4 mm apart for an M6
   spindle, 12.5 mm high, the underside 23.4 mm above the bench, the bend's outside 58.4 mm ahead of the base. Each leg
   carries a bore 13.5 mm back from the base's front at 30.6 mm height, and rises at the back to a boss with a second
   bore 13.9 mm from the first, and has a stop pad on its rear edge. Cut the two bores and shape everything in the flat.

3. Make the handle of two stamped halves of 2.5 mm that joggle together under a red PVC grip whose end is 108.8 mm back
   from the base's front, and the link of two flat stamped plates joined by a staked spacer. The handle's lever from its
   pivot on the bar to the knee is 21.1 mm, the link is 15.8 mm, the link's lower pivot, in the base, 30.92 mm back and 9.6 mm up.

4. Put it together as a real four-bar with rivet pivots, a 4 mm pin in a 4.3 mm bore at each of the four pivots, layered
   plates with real side clearance, and solve it as one closed loop with no degrees of freedom once I drive the joint where
   the link pivots on the base. Work out the toggle first: the knee sits 3 degrees past the straight line through the handle and link pivots
   at the clamped pose, where the link's joint reads zero, and the bar's stop pad stops the link there with a hair of
   gap. The handle opens about 41 degrees, a slider from 30 to 42, and the bar then opens about 91 degrees. Drive the
   link there and back over the timeline, open at the ends, clamped in the middle, stopping short of the dead point
   where the bar and handle come into line (about one degree of link rotation short at the default).

5. Add the M6 spindle with a black rubber cap and two ISO 4032 lock nuts, width 10 mm across flats, height 5.2 mm, one
   above and one below the bar, a beech block for the workpiece, a slider for the workpiece height from 3 to 8 mm that
   sets the spindle so the cap just touches the block when clamped, and a slider for the spindle's reach along the
   slot, measured from the bar's pivot on the base, 28.6 to 66 mm, default 28.6.

6. Give me a live output for the mechanical advantage at the spindle from the solved positions, with the hand force
   74.5 mm behind the handle pivot, and prove the toggle: the knee's joint angle at the clamped pose, the cap's face
   against the top of the block, the link on its stop, the fit of every pivot, and the advantage against an independent
   closed form. Bright zinc, red grip, black rubber.

7. Check it over the whole motion, play it, and show me a picture with the clamp closed on the block, and tell me the
   blank size of each sheet part.

## Acceptance

- 8 parts, 13 instances (two base halves, bar, handle, link, four rivets, spindle, two nuts, workpiece), 14 mates, 0
  degrees of freedom with the link driven, 3 public parameters.
- The knee's joint angle at the clamped pose is 3° past the toggle line (within 0.1°) and passes through 0 between the
  open and clamped poses.
- The rubber cap's face is at the top of the block at the clamped pose (within 0.05 mm); at the open pose it is at
  least 30 mm above it.
- The link clears the bar's stop pad by 0.02 to 0.12 mm at the clamped pose; every pivot has a clearance fit between
  0.02 and 0.18 mm.
- The bar opens about 91° at a handle opening of about 41° (each within 3°).
- Base, U-bar and handle halves are real sheet-metal features with an inner bend radius of the thickness and flat
  patterns exported as DXF.
- The mechanical advantage output agrees with a closed form within 0.1 %, about 21:1 at the stop at the 28.6 mm reach.
- No collisions over the motion other than the listed contacts: the nuts on the bar, the nut threads on the spindle,
  and the cap on the workpiece.
