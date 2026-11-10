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

From simple to complex, each with the difficulty its reviewer scored out of 10. The reviewer was an AI agent in the
role of a professional of the assembly's trade (a toolmaker, an automotive engineer, a lighting designer, a machine
builder, an engine builder) and of the fitter who must put it together, working apart from the agent that built it;
every assembly passed that review, and its prompt was tested by a second AI model. [`AGENTS.md`](AGENTS.md) §8 names
the models and effort levels, and the briefs the assemblies were built from are in [`CATALOGUE.md`](CATALOGUE.md).

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

## Rebuild and check

The committed `<id>.3dcraftasm` files and `exports/` are the finished assemblies: open one in 3DCraft, in the app
or with `craft3d-cli`, and play its motion, without rebuilding anything. Each carries its parts.

The tool that made and checked them, `tools/assemblies.py` (Python 3, standard library only, on Linux or macOS),
builds every part, then the assembly, packs it and checks it at rest and over its motion. It needs the exact 3DCraft
build this repository is pinned to, the commit and file format in [`tools/pin.json`](tools/pin.json) as
`craft3d-cli --version` reports them, and refuses any other: it compares what it rebuilds byte for byte with the
committed files, which only that build reproduces. When the repository is released the pin is the 3DCraft 0.1.0
release itself, so the `craft3d-cli` that its installer puts on your `PATH` runs it (or name the binary in
`CRAFT3D_CLI`).

```sh
tools/assemblies.py build toggle-clamp          # parts and build.json -> .3dcraftasm and exports; rewrites meta.json
tools/assemblies.py check --quick toggle-clamp  # rebuild in a scratch folder (.scratch/) and check at rest and over the motion
tools/assemblies.py check toggle-clamp          # the same, plus the public ranges and their corners
tools/assemblies.py render toggle-clamp         # preview.png
```

`build` rewrites the `stats` (timings measured on your machine) and `craft3d` fields of the assembly's `meta.json`.
Give `check` an id: without one it rebuilds and checks all six, which takes hours. Where `systemd-run` exists,
every run is capped in memory (in the slice named by `CRAFT3D_SLICE`, default `assemblies.slice`), and on Linux the
tool waits while less than 1.5 GB of memory is free.

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
