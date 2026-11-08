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
<!-- gallery:end -->

## Licences

- The assemblies and their parts: **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**, in each document's
  information. Credit: *3DCraft assemblies*, with a link to this repository.
- The tools: MIT ([LICENSE](LICENSE)).
- Sources from elsewhere: [ATTRIBUTION.md](ATTRIBUTION.md).

Agents and contributors: read [`AGENTS.md`](AGENTS.md) first.
