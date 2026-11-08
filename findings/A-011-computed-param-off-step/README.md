# Agent friction: an instance parameter from a formula is refused when off the part's step

Found while building `toggle-clamp` at 3DCraft 45233bdc.

A part publishes a length with a step of 0.1 mm for its own form; an assembly passes it a value computed by a formula
(`sqrt(2) * 7 mm`, here the closed-form position of a pivot). The instance fails: `its configuration failed: ... its value
9.899... mm is not on its step of 0.1 mm`. A step is what a form or slider offers; a value an assembly computes is not a
slider. Should: a step limits interactive input and `param.set`, not a value passed in `params` by a parent; or the
refusal says the step is what to remove. Workaround used: the parts' pivots are published without a step.
