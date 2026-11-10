# 3DCraft assemblies

Six mechanisms built in [3DCraft](https://github.com/johancoppens/3dcraft), the open-source parametric CAD modeller
built for AI, from a simple clamp to a machine. Every one is real (sized to the standards of its trade), makeable (its
process checks are part of the model), proven (at rest and over its whole motion) and light (it opens in seconds).

Each assembly lives in its own numbered folder under [`assemblies/`](assemblies/), with:

- **`<id>.3dcraftasm`**: the assembly, with its parts packed inside; open it in 3DCraft and play its motion.
- **`parts/*.json` and `build.json`**: the 3DCraft commands that build it, ending with the checks that prove it.
- **`README.md`**: what it shows, the real thing behind it, how it goes together.
- **`prompt.md`**: a conversation you can have with an AI connected to 3DCraft to build it yourself.
- **`exports/`**: files for the workshop where they make sense.

## Gallery

From simple to complex, each with the difficulty an independent reviewer scored out of 10. The briefs they were built
from are in [`CATALOGUE.md`](CATALOGUE.md).

<!-- gallery:start -->
| | Assembly | Domain | Difficulty |
|---|---|---|---|
| <img src="assemblies/01-toggle-clamp/preview.png" width="240" alt="Horizontal toggle clamp"> | **[Horizontal toggle clamp](assemblies/01-toggle-clamp/)**<br>A horizontal hold-down toggle clamp of the M6, 900 N class: a formed base in two mirrored L halves held by the pivot rivets, a formed U-bar with an M6 spindle and rubber cap, a stamped link and handle with a red PVC grip, all on rivet pivots. | Workshop, sheet metal | 5/10 |
| <img src="assemblies/02-jansen-walker/preview.png" width="240" alt="Jansen linkage walker"> | **[Jansen linkage walker](assemblies/02-jansen-walker/)**<br>A hand-cranked twelve-legged walking machine after Theo Jansen's linkage: laser-cut birch bars and frame ribs, walnut triangles, brass pins and a keyed brass crankshaft, walking on a floor of boards that rolls one board per turn. | Kinetic art, laser cutting | 8/10 |
| <img src="assemblies/03-scissor-jack/preview.png" width="240" alt="Scissor car jack"> | **[Scissor car jack](assemblies/03-scissor-jack/)**<br>A pressed-steel scissor jack sized after jacks sold as 1 t: four U-section arms with gear-tooth ends, a screw between a nut trunnion and a bearing trunnion, a saddle held level by the gears, and a tilted folding crank on a Hooke joint. | Automotive, sheet metal | 6/10 |
| <img src="assemblies/04-task-lamp/preview.png" width="240" alt="Spring-balanced task lamp"> | **[Spring-balanced task lamp](assemblies/04-task-lamp/)**<br>A two-arm desk lamp in oak and brass on a cast-iron base, balanced by four real extension springs. The torque about each arm's pivot, from the measured masses and the real springs, stays within a stated pivot friction over a sweep of poses. | Product design, lighting | 6/10 |
| <img src="assemblies/05-corexy-printer/preview.png" width="240" alt="CoreXY 3D printer"> | **[CoreXY 3D printer](assemblies/05-corexy-printer/)**<br>A desktop CoreXY FDM printer with a 250 mm build area: a black T-slot frame, MGN12 rails, NEMA 17 motors on two GT2 belts, a bed on two T8 lead screws with floating nuts, and a blue spiral vase printed as a time-lapse while the nozzle runs its rim. | 3D printing, machine building | 8/10 |
| <img src="assemblies/06-radial-engine/preview.png" width="240" alt="Seven-cylinder radial engine with its valve train"> | **[Seven-cylinder radial engine with its valve train](assemblies/06-radial-engine/)**<br>The seven-cylinder radial with its valve train: a double-track cam ring turned at one sixth of the crank speed through reduction gears, roller tappets, pushrods, rockers and poppet valves in a cut-away crankcase and opened cylinders. | Aviation, engines | 8/10 |
<!-- gallery:end -->

## Licence

The assemblies, their parts and what is written and drawn about them (the pages, previews, `AGENTS.md`,
`CATALOGUE.md`, the feedback) are under **CC BY 4.0** ([`LICENSE-CC-BY-4.0.md`](LICENSE-CC-BY-4.0.md)), as each
document's information says; the code, the tool under `tools/` and the reproducers under `findings/`, is MIT
([`LICENSE`](LICENSE)). One part is MIT too: the CoreXY printer's T-slot profile, copied from the
[3DCraft examples](https://github.com/johancoppens/3dcraft-examples). Every page and every `meta.json` states its
licence. Credit an assembly as:

> "Scissor car jack" by Johan Coppens, from the 3DCraft assemblies (CC BY 4.0),
> https://github.com/johancoppens/3dcraft-assemblies-examples

with its title. Sources from elsewhere, and the products parts are sized after: [`ATTRIBUTION.md`](ATTRIBUTION.md).

Agents and contributors: read [`AGENTS.md`](AGENTS.md) first.
