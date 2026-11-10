# Missing capability: bendable has no one-stroke U-forming of two parallel bends

Found while building `toggle-clamp` at 3DCraft 150f0015.

A U-section (a narrow web with two legs bent the same way) is formed in one stroke of a punch into a U-die. `bendable`
accepts an `order` of strokes, but one stroke can only hold flanges on one line of one flat: `repro.json` builds a U
(web 1.4 mm, inner radius 2.5 mm, legs 50 mm) and asks for `"order": [[0, 1]]` with a mandrel-and-die; the answer is
"flanges 0 and 1 cannot be bent in one stroke: they are not on one line". Bent as two strokes on a press brake the tools
collide (the legs are too long for the second punch to reach), which is also what happens on a real brake.
Should: a stroke may hold parallel bends formed together by a punch and a die shaped for it (a U-die), or a named
"formed by a press tool" assertion that says what was not checked. Impact: the toggle clamp's U-bar carries no
`bendable` proof; the README says so.
