# AGENTS.md: guide for AI agents working on the 3DCraft assemblies

> **About this file.** This is the working brief that the AI agents followed while they built and
> reviewed these six assemblies in November 2026. It is published as it was used, so you can see how
> each mechanism was made and proven. It is addressed to those agents: "the developer" is 3DCraft's
> author, "the coordinator" is the agent session that briefed the others and made every commit,
> and §8 names the AI models and effort levels that did the work. The memory caps and the timings
> "on a reference machine" describe that workshop, and `log/`, `plan/` and `.scratch/` were local
> folders that are not in this repository. To open, change or rebuild an assembly you need only
> [README.md](README.md); the bar in §4 is also the bar a contribution is held to.

This repository holds **six example assemblies** for [3DCraft](https://github.com/johancoppens/3dcraft), the
parametric CAD modeller built for AI. An assembly places instances of parts, joins them with mates and couplings, and
plays over the timeline `t`. Together the six show what that can do, from a simple clamp to a machine. Each one must
be **a real mechanism: real, makeable, beautiful, light and proven at rest and over its whole motion**.

It follows the method of [3dcraft-examples](https://github.com/johancoppens/3dcraft-examples) and
[3dcraft-jigs](https://github.com/johancoppens/3dcraft-jigs), at the same bar.

Read this file, then [`CATALOGUE.md`](CATALOGUE.md) (what each assembly must be), then the assembly you work on.

## 1. Ground rules

- **Language.** The developer writes in Dutch: answer in Dutch. Everything that lands in this
  repository is English: files, names inside the models, commit messages.
- **3DCraft is pinned.** Every assembly is built and checked with one 3DCraft commit, recorded in
  [`tools/pin.json`](tools/pin.json): the installed `craft3d-cli`. `tools/assemblies.py`
  refuses any other build. Only the coordinator moves the pin, after rebuilding and checking all six.
- **Do not change 3DCraft from here.** What 3DCraft gets wrong or lacks is *collected* in
  [`3DCRAFT-FEEDBACK.md`](3DCRAFT-FEEDBACK.md) (§7); the developer takes it to 3DCraft in one go. Do not build
  around a limit in silence.
- **Six, no more.** The list is `CATALOGUE.md`'s. Each is one `.3dcraftasm`. A new idea replaces one of the six or
  goes to the developer.
- **Mechanisms move through the assembly.** Mates, couplings and `t` do the moving. Placing bodies by formulas of a
  drive parameter is how a Jig moves ([`3dcraft-jigs`](https://github.com/johancoppens/3dcraft-jigs)); here it is
  wrong wherever a mate can do it.
- **The start screen is not a concern here.** The assemblies will be integrated into 3DCraft's start screen later,
  and that work happens in 3DCraft itself. Do not shape an assembly around it.
- **Original designs.** Generic types (a toggle clamp, a scissor jack, a CoreXY motion system, a Jansen linkage) are
  fine and are credited; a brand's specific design, logo or name is not. "Strandbeest" is Theo Jansen's name for his
  works: the title says "Jansen linkage". Text uses 3DCraft's bundled fonts; never commit font files.
- **Parts from the sister repositories** may be reused, as a copy of their `build.json` in `parts/` taken at this
  repository's pin, with a row in [`ATTRIBUTION.md`](ATTRIBUTION.md). A reused part meets this repository's budgets
  (§4.5) like any other: its load time counts in full, for each configuration used.
- **Licence.** The assemblies and their parts (documents, sources, READMEs, pictures) are **CC-BY-4.0**, in
  `document.info` of `build.json` and of every part, and so are the other texts
  ([`LICENSE-CC-BY-4.0.md`](LICENSE-CC-BY-4.0.md)); the code, the tools and the reproducers under `findings/`, is MIT
  ([`LICENSE`](LICENSE)). A part copied from
  `3dcraft-examples` keeps its MIT and its copyright notice in `ATTRIBUTION.md`; a Jig is CC-BY-4.0 unless it says
  otherwise. **No share-alike source** enters this repository (`gt2-pulley` is CC-BY-SA-4.0, for a tooth outline taken
  from a CC-BY-SA design): draw the part here from published facts. Data from elsewhere needs a licence that allows it
  and a row in `ATTRIBUTION.md`.

## 2. Layout

```text
AGENTS.md README.md CATALOGUE.md 3DCRAFT-FEEDBACK.md ATTRIBUTION.md LICENSE
tools/assemblies.py     build, render, check, coverage, readme (python3, standard library only)
tools/pin.json          the pinned 3DCraft commit and file format
findings/<A-nnn>-<slug>/  minimal reproducers for 3DCRAFT-FEEDBACK.md
assemblies/NN-<id>/     one directory per assembly: NN its place in CATALOGUE.md, <id> kebab-case
log/ plan/              local only (gitignored): dev log, plans
```

| File in `assemblies/NN-<id>/` | What it is | Made by |
|---|---|---|
| `parts/<part>.json` | **The source of one part**: a JSON list of `[command, params]` steps run in a new document, ending with `document.check`. A script that starts with `assembly.new` is a **subassembly**: it is built after the plain parts, in name order, and placed as `parts/<part>.3dcraftasm`. | hand |
| `build.json` | **The source of the assembly**: starts with `assembly.new`, places `parts/<part>.3dcraft` with `instance.add`, ends with `document.check`. No `file.*` or `assembly.pack` steps: the tool saves and packs. | hand |
| `meta.json` | title, card summary, domain, tier, difficulty, standards, materials, motion, intended contacts, preview framing, exports | hand; `stats` and `craft3d` written by the tool |
| `README.md`, `prompt.md` | the assembly's page and its AI rebuild chat (§6) | hand |
| `<id>.3dcraftasm` | the packed assembly: one file that carries its parts and opens anywhere | `tools/assemblies.py build` |
| `exports/` | the STEP of the assembly with its structure, plus only what the processes need (3MF, DXF, SVG, STEP per part: an entry with `"part": "<part>"` is exported from that part's document); listed in `meta.json` `exports` | `tools/assemblies.py build` |
| `preview.png` | the picture (§5) | `tools/assemblies.py render` |
| `make.py`, `data/` | only for input from outside (§3) | hand |

## 3. Working with 3DCraft

- **Build headless.** Edit the sources, then `tools/assemblies.py build <id>`: it builds every part in a scratch
  folder, runs `build.json` beside them, packs, refuses to save when `document.check` is not ok, writes the exports,
  measures, and lints names and budgets. To look around: `craft3d-cli run assemblies/NN-<id>/<id>.3dcraftasm --cmd
  assembly.inspect` (or `assembly.solve`). To learn a command: `craft3d-cli commands --filter <id>`. The
  [user guide](https://3dcraft.dev/guide/)'s chapters on assemblies and on the window (its timeline), and the method
  and limits in 3DCraft's
  [`docs/design/assemblies.md`](https://github.com/johancoppens/3dcraft/blob/main/docs/design/assemblies.md) and
  [`motion.md`](https://github.com/johancoppens/3dcraft/blob/main/docs/design/motion.md); read them, never edit them.
- **Never use the session's 3DCraft MCP tools** (`mcp__craft3d__*`): they drive the developer's own window. Work
  through `craft3d-cli`; its commands are the same ones MCP runs.
- **Memory and time.** Runaway processes have crashed the reference machine. `tools/assemblies.py` caps every run;
  by hand, always `systemd-run --user --scope -q -p MemoryMax=3G -p MemorySwapMax=0 timeout 900 craft3d-cli …`. Exit
  137 means the cap was hit: that is a finding, never a reason to raise the cap. When several agents work at once, the
  coordinator sets a shared slice sized to what the machine has free (`systemctl --user set-property --runtime
  assemblies.slice MemoryMax=3G MemorySwapMax=0`, since other sessions run beside this one): the tool uses that slice
  and waits while memory is short; add `--slice=assemblies.slice` to every `systemd-run` you type. Scratch files go in
  `.scratch/` (gitignored, on disk): `/tmp` is held in memory on the reference machine. One render, bake or `check-range` at a time per agent.
  No cargo builds are needed here; never build 3DCraft from this repo. A 3DCraft window you start gets
  `--recovery-dir none`.
- **Python.** Everything an assembly decides lives in its documents: variables, tables, formulas, mates, couplings,
  outputs, assertions. `parts/*.json` and `build.json` are the source; no `gen.py` is committed. There is no pattern of
  instances, so seven pistons are seven `instance.add` steps and their mates: that repetition is expected, and it is
  feedback (§7). A `make.py` is only for outside data: it runs offline from committed inputs, is deterministic, and
  writes steps into the source. Python that computes geometry or motion 3DCraft should compute is a workaround: log the
  missing capability first, use it only when the assembly cannot exist otherwise, and say so in its README.
- **Mates and motion, what is known at the pin:**
  - Mate on **named datums** of the part (`Piston[1]/Wrist`), named for their function. A face name changes when a
    profile changes; a datum does not.
  - The second frame is put facing the first. Two axes drawn the same way need `"flip": true`.
  - Do not rely on the roll of a datum axis. Where the roll matters use a plane or a flat face; a piston in a bore is
    `cylindrical`, and the next joint stops its roll, as in the real thing.
  - A loop is solved from where its parts start and stays on that branch. Give `position` and `rotation` close to the
    intended pose.
  - The solver sees frames, not geometry: a cam or a gear's flanks are not mates. A follower is driven by a formula of
    the same law that draws the cam, and contact is proven by measure (§4.7). Gears, racks and screws are couplings.
  - A `ball` mate has no variables: it cannot be driven, limited or coupled.
  - A dead point is reported only when a frame lands on it. To prove an over-centre position, assert the joint angle.
  - A limit, once passed, stays held for the rest of that solve.
  - A joint driven by a formula of `t` cannot be published (`variable.publish` takes values only). Publish a variable
    the formula uses: `Drive_angle = start_angle + 360 deg * t`, with `start_angle` public, gives both a slider and
    a play.
  - The timeline is a variable `t` that is a plain number. The value stored is the pose everything but the motion
    sees: the preview, the checks at rest, the exports.
  - An instance whose parameters are formulas of `t` (a spring, a belt) is a new configuration at every moment. Make
    those parts cheap: they count in the bake (§4.5).
  - A part's own assertions are not checked per configuration. Whatever values the assembly passes, the part's own
    `check-range` must cover them.
  - `overlap` takes `of` and `to`; `clearance` takes `from` and `to`.
  - A mate's name becomes a variable (`Wrist3_angle`): keep it a plain identifier (`Wrist3`, not `Wrist[3]`).
  - A trace is view state and is not saved in the file.
  - A measure reaches an instance inside a subassembly by its path (`Leg/Knee bar`); the subassembly's own name is
    not a subject.
  - A flexible subassembly's joints are free in the parent unless it publishes what drives them and the parent gives
    that in `params`: to play a leg's own motion in a machine, publish its `t` and pass `"params": {"t": "t + phase"}`.
  - Mating threads cannot be shown clear ([F-014](https://github.com/johancoppens/3dcraft-examples/blob/main/3DCRAFT-FEEDBACK.md#f-014)):
    give the pair a real radial clearance or keep the thread on one side, and list the pair as a contact (§6).
- **Lessons paid for by the examples and Jigs, for every part:**
  - Face names come from the sketch's entity ids (`F2:side(e13)`): a point added to a profile renumbers its lines.
    Read them from `document.inspect` (`faceNames`) after every change to a profile.
  - A measure's face subject is a query: `{"kind": "face", "where": {"name": "*F6:side(e7)"}}` (a glob: later features
    prefix the names).
  - A feature's body cannot be measured once a later feature has taken it: measure the final body, and split it with
    planes (`volumeBelow`) or outputs (`variable.measure`) for closed-form checks.
  - Units in `tol` are expressions: `0.01 mm^3` means (0.01 mm)³; write the plain number `0.01` (the document's unit).
  - `body.appearance` changes only the fields it is given; `material.preset` sets them all.
  - Coatings (black oxide, paint, powder coat, anodising) render best as a dielectric layer (`metallic` 0).
  - Every measure on a complex body runs at every regeneration. Measure what proves something.
  - Standard values written from memory are often wrong: verify every value against a source and cite it.
  - Every number in the README is the model's (`output.list`, `assert.list`), and every claim is one the checks prove.
  - Look at the full-size preview for renderer artefacts: smears (`look.reflections`), stepped shadow bands
    (`look.light`), blotches in cavities. Fix them with the framing keys of §5 and say so in the README.
  - Under the Workshop environment at rotation 0 the warm key light makes polished steel read as brass: render at
    `look.rotation` 0, 90, 180 and 270 and keep the one where neutral metals read neutral (often 180).
  - The body is named after its last feature: name that feature for the part ("Piston", "Crank").
  - In a sketch a circle is entity `e2` (its centre is `e1`): `sketch.pattern` wants the `e2`.
  - `face.appearance` must follow its extrude: later on, source names are refused.
  - A sketch on the zx plane takes points as `[z, x]`.
  - A distance to a notched body can come back unproven: measure between plane faces.
- **Prefer 3DCraft's own means**: configurations through `params`, one part placed many times, `"body"` to place one
  body of a multi-body part, subassemblies (rigid, or flexible with their own couplings), `coupling.add` with a formula
  of the real ratio, `variable.measure` of a joint for outputs, variables and tables, `sketch.curve`, `feature.pattern`.

## 4. The quality bar

### 4.1 A real assembly
This is what separates an assembly from an example. A reviewer rejects an assembly that fails any of these:
- **It moves as the real thing moves**, by joints of the kinds the real thing has, and its ratios and strokes are the
  real ones.
- **`t` plays something worth watching.** From 0 to 1 it runs the working cycle. A cycle that repeats closes on itself
  (a crank's full turn); one that does not goes there and back or says so in `meta.json` `motion`.
- **Its degrees of freedom are deliberate.** `assembly.solve` is ok, with 0 degrees of freedom left, or with every free
  motion named in the README and meant (a shade you swivel by hand).
- **One part, many instances.** What is the same in the real thing is one source; what differs in size is a
  configuration of it. No copies of a part under other names.
- **It can be put together.** Every part reaches its seat, every screw its tool, in an order the README gives.
- **Moving parts have real fits.** A pin is smaller than its bore by a stated fit; nothing is modelled line-on-line
  and nothing overlaps except the contacts listed in `meta.json`.

### 4.2 Real
Sizes follow the named standard (number, part, table) or a stated real reference, cited in the README. Proportions a
professional of the trade would accept, at every pose and at every point of the public ranges. Real units and
tolerances where they matter.

### 4.3 Makeable
Name the process of every part; prove with assertions what can be proven, in the part's own document:
- **FDM printing:** walls ≥ 1.2 mm (`measure.thickness`); no overhang below 45° from the bed unless the README says
  where supports go (`measure.draft`, pull = the build direction); a first-layer chamfer; clearances for fits; 3MF
  export in the print orientation.
- **Sheet metal:** inner bend radius ≥ the material's minimum; `bendable`; holes ≥ 2.5 t + r from a bend; reliefs;
  flat pattern as DXF.
- **Laser, plasma, waterjet:** smallest slot and hole ≥ the thickness; kerf stated; cut and engrave apart.
- **CNC milling:** inside corners ≥ the tool radius; pockets ≤ 4 × the tool diameter deep.
- **Turning, casting, welding, woodworking:** casting draft ≥ 1° and fillets on every cast edge; weld access and joint
  preparation; boards of stock thickness, grain stated, joints in proportion.

### 4.4 Beautiful
- Fillets and chamfers wherever the real object has them (the developer asks this explicitly): no blocky, untouched
  edges. That holds for every part, also the small ones.
- Materials from `material.preset`, tuned with `body.appearance` (colour, roughness). Keep to your assembly's line of
  the palette in `CATALOGUE.md`, and let materials tell the parts apart at a glance.
- The stored pose shows the assembly at its best: in use, assembled and upright, never its parts laid out. Where the
  interest is inside, the housing is cut away in its part's own history.
- Look at the preview at full size, from two more angles, and at two other moments of the motion, before you hand in.

### 4.5 Light
Loading means opening the packed `.3dcraftasm` and regenerating it; the tool measures it (`stats.load_s`, `craft3d-cli
info`, the least of two openings). Budgets on a reference machine: **simple ≤ 1 s, difficult ≤ 2 s, complex ≤ 4 s**,
file ≤ 1 MB, CPU time (all threads, `stats.load_cpu_s`) at most 3 × the load budget, since the web build is
single-threaded. **A whole motion is at most 3 × the load budget**: `motion.bake` at 120 frames (`stats.bake_s`), with
every configuration `t` asks for. The slowest point of the public ranges is at most 3 × the load budget too
(`stats.range_worst_s`). A timing taken while the machine is busy (load average over half its CPUs) only warns; the
coordinator re-measures at a quiet moment. Over budget, simplify (fewer, larger features; one part placed more often;
a cheaper part behind a formula of `t`); only the coordinator grants an exception (`meta.json` `budget_exception` with
the reason).

### 4.6 Parametric, named, minimal
- Every size a maker might change is a variable; everything derived is a formula. No magic numbers in feature params
  or mates (0, 1 and angles of symmetry aside). A size two parts share is one assembly variable, passed to both by
  `params`.
- **Names.** Variables in descriptive `snake_case` with the unit in the expression (`wall_thickness` = `2 mm`, not
  `t`, which is the timeline); features, sketches, datums, sets, assertions, instances (`Piston[3]`), mates and
  couplings named for their intent in plain English. No automatic names (`Extrude2`, `Mate3`): the tool rejects them.
- **2 to 4 public parameters** on the assembly (`variable.publish` with label, group, range and step): the knobs a
  maker would really turn, a pose among them where the mechanism is posed by hand. No more: a configurator is a Jig.
- **A minimal history.** Every step contributes to the final model: no dead, suppressed, trial or undone steps. Guide
  for parts and assembly together: simple ≤ 120 steps, difficult ≤ 300, complex ≤ 600 (variables and assertions
  included). In a part: variables, sketches and features, materials, assertions, `document.info`, `document.check`. In
  `build.json`: variables with `t` first, instances, mates, couplings, joints, outputs, assertions, `variable.publish`,
  `document.info` (title, description, author `3DCraft assemblies`, licence), `document.check`.

### 4.7 Proven at rest and over the motion
End with assertions that make the assembly prove itself; never fewer than three, and at least one closed-form or
independently computed:
- **At rest:** `document.check` is `ok` (every mate and coupling solved, every part valid, no broken assertion). An
  assertion that is not proven neither passes nor fails, so it cannot catch a mutation: make it decide, or name it in
  `meta.json` `unproven` with why and explain it in the README. The tool fails any other. For a fit, assert the
  `clearance`'s `min` (its lower bound is proven) and the `max` on an output of the same clearance with a `value`
  assertion: the gap found is a real pair of points, so that passes when the clearance's own `max` would and fails
  where that one only reads not proven ([A-041](3DCRAFT-FEEDBACK.md#a-041)). Where that output is unknown (a small
  pressed gap), measure the fit face to face with `distance`. The check over the public ranges is `check-range`.
- **Over the motion:** `motion.check` at no fewer than 73 samples, at the defaults and at the corners of the public
  ranges. A joint's solved value against a closed form (`jointAngle`, `jointDistance`, `position`, `rotation`); the
  ratio you see is the ratio asked; the extremes that matter (stroke, height, reach); `clearance` where a gap is the
  point. No dead point unless the README says why.
- **No collisions:** over 121 moments at the defaults and 31 at each corner of the public ranges, none but the contacts
  in `meta.json` (`view.motion` with `collisions`, which names the pairs; `tools/assemblies.py check` runs it).
- **Formula-driven contact is measured:** a follower driven by a formula is shown to touch and not to penetrate.
- **It holds for the model, not the formula.** An assertion that compares a formula with itself proves nothing: remove
  it. Do a mutation test in a scratch copy: a moved pivot, a wrong ratio, a loosened fit must fail something.

Everything over the motion holds **at the samples**; a README says so and claims no more. Keep assertions cheap: each
runs at every sample.

## 5. The preview

`tools/assemblies.py render <id>`: 1600 × 1200, studio look, **Workshop** environment, **ACES** tone curve, **+0.5
stop**, plain background, CPU renderer, 8 frames accumulated: the same look as the examples and Jigs. It draws the
stored pose, so choose the stored `t` for the picture. `meta.json` `preview` may set only the framing (`view`, `zoom`,
`camera`, `projection`, `box`, and `look.light`, `look.rotation`; `look.reflections: false` only where the renderer's
reflections smear a surface, said in the README). It takes about a minute.

## 6. README, meta.json and prompt

**`README.md`** of an assembly, in this order: title and a one-paragraph pitch; the preview; *What it shows* (the
3DCraft techniques, command ids in backticks); *The real thing* (standards, processes, materials, how to make each
part); *Parts and assembly order* (the parts with their counts and how they go together); *The motion* (what `t` plays,
what is free, what drives what); *Parameters*; *Checks* (at rest, over the motion, what the samples do not cover);
*Files*; *Rebuild*; *Difficulty* (the reviewer's score out of 10 and one line why); *Platform notes* (links to
`3DCRAFT-FEEDBACK.md` entries, if any); *Licence*. Every claim must be true of the model.

**`meta.json`**:

```json
{
  "id": "scissor-jack",
  "title": "Scissor car jack",
  "summary": "screw, gear teeth, closed loop",
  "description": "A pressed-steel scissor jack that lifts as its screw turns.",
  "domain": "Automotive, sheet metal",
  "process": "Pressing, thread rolling",
  "tier": "difficult",
  "difficulty": {"score": null, "rationale": ""},
  "standards": [],
  "materials": ["Pressed steel, painted"],
  "licence": "CC-BY-4.0",
  "units": "mm",
  "motion": {"cycle": "there and back", "samples": 73, "dof": 0},
  "contacts": [{"pair": ["Spindle", "Nut"], "why": "the thread is the joint (F-014)"}],
  "preview": {"zoom": 1.1, "look": {"light": [200, 70]}},
  "exports": [{"path": "exports/scissor-jack.step"}],
  "prompt_test": {"date": null, "model": null, "result": null}
}
```

`summary` is the card's line (a few words). `motion.dof` is the degrees of freedom `assembly.solve` must report; each
is named in the README. `contacts` lists every pair that may overlap, each with its reason (`*` matches any text in a
name); everything else must be clear. `unproven` (only when needed) lists `{"name", "why"}` for each assertion
that reads not proven at rest (a part's as `"<part>: <name>"`). `stats` (load, bake, file, steps, parts, instances, degrees of freedom) and
`craft3d` are written by the tool.

**`prompt.md`**: the chat a person could paste, turn by turn, into an AI connected to 3DCraft over MCP to build the
same assembly. Only the person's turns, in a designer's words (intent, sizes, standards, finish, how it moves); no
command ids, no JSON; 3 to 8 turns, the last asking for a check, a play of the motion and a picture. Below the turns,
*Acceptance*: what the result must meet (counts, strokes and ratios within a stated tolerance, no collisions over the
motion). A prompt counts as done once tested (§8): `meta.json` `prompt_test` records the date, model and result.

## 7. 3DCraft feedback

Collect, never fix. [`3DCRAFT-FEEDBACK.md`](3DCRAFT-FEEDBACK.md) has four kinds:
- **Bug**: a wrong result, a crash, a valid request refused. With a minimal reproducer in
  `findings/<A-nnn>-<slug>/repro.json` and the parts it needs.
- **Missing capability**: phrased generally, for any mechanism and anyone who designs with 3DCraft (3DCraft is a
  platform: never "a CoreXY command", but "a motion tied to the sum of two others").
- **Performance**: too slow or too heavy, with numbers.
- **Agent friction**: what made building through commands slow or error-prone.

Each entry: id (`A-001` …, so as not to clash with the examples' `F-nnn` and the Jigs' `J-nnn`), kind, title, the
assembly it was found in, the 3DCraft commit, what happens and what should happen, the reproducer, the impact on the
assembly (blocked, workaround used, cosmetic) and the workaround. Check the examples'
[`3DCRAFT-FEEDBACK.md`](https://github.com/johancoppens/3dcraft-examples/blob/main/3DCRAFT-FEEDBACK.md) and the
Jigs' [`3DCRAFT-FEEDBACK.md`](https://github.com/johancoppens/3dcraft-jigs/blob/main/3DCRAFT-FEEDBACK.md) first and cite an entry that already covers it. An assembly that works
around something links its entry from its README, so it can be improved once 3DCraft is fixed. Builders propose
entries in their report and write the reproducer; the coordinator numbers them and edits `3DCRAFT-FEEDBACK.md`.

## 8. Roles and the review loop

| Role | Model, effort | Does |
|---|---|---|
| **Coordinator** (main session) | Opus 5.5, xhigh | Owns this file, `CATALOGUE.md`, `README.md`, `3DCRAFT-FEEDBACK.md`, `tools/`; briefs agents; runs the review loop; commits (the only one who does); reports to the developer in Dutch. |
| **Feasibility probe** | Opus 5.5, medium | Answers "can 3DCraft do X at the pin" with a minimal script, before a risky assembly is built: the loop closes, the coupling holds, the configurations are cheap enough. |
| **Builder** | Opus 5.5; high (simple), xhigh (difficult, complex) | Owns `assemblies/NN-<id>/` only. Writes the sources, `meta.json`, `README.md`, `prompt.md`; builds, renders, checks itself against §4 and looks at the pictures before handing in; writes reproducers in `findings/`. Never commits. |
| **Reviewer** | Opus 5.5; high, xhigh for complex | Fresh, and reads the files, not the builder's report. Plays the trade's professional (toolmaker, automotive engineer, lighting designer, machine builder, engine builder) **and** the fitter who must put it together. Rebuilds, plays the motion, renders two more views and two more moments, checks §4 point by point, gives the difficulty score. |
| **Prompt tester** | Sonnet 5.5, medium (once Opus 5.5 if Sonnet fails, to tell a weak prompt from a weak model) | Fresh, gets only `prompt.md` and 3DCraft through `craft3d-cli` (its commands are the ones MCP runs; never the developer's window); builds; the coordinator compares the result with the *Acceptance*. |

**Review verdict**: `PASS` or `REVISE`, with findings marked **MUST** (wrong, unmakeable, ugly, over budget, untrue
README, not a real assembly by §4.1), **SHOULD** or **NIT**, each with its evidence (a measure, a picture, a moment of
the motion, a clause of a standard), and the difficulty score with one line why. Builder and reviewer loop until no
MUST is open; the same reviewer is continued for the re-review.

**What reviews keep finding** (from the examples and Jigs; look for these yourself before handing in, it saves a
round):
- An assertion that restates a formula instead of measuring the model.
- A failure inside the published range that sampling missed. For a mechanism: a linkage that locks, jumps branch or
  collides only at a far point of a range.
- Parts that cannot be assembled or made: a bearing that cannot reach its seat, a groove that ends in a flange, a shaft
  longer than its bore. Walk the assembly and the machine's path step by step.
- Exports: a part drawn twice, a helper body in the file, a layout that does not fit the bed.
- README claims the model does not bear out, and sources cited but not read (a value from memory that is cited is a
  MUST): say what was read, what is from a secondary source, what is your own judgement.
- Safety: a jack, a lamp over a desk, a load limit. The README states only what the model proves and says who must
  verify the rest.
- Real use, not only the drawing: will it be gripped, driven, will it tip, does it fit the tool that makes it?

**Difficulty** (1 to 10, scored by the reviewer): what it takes to build this assembly from scratch in 3DCraft, by hand
or with an agent, its parts and its motion included.

| Score | Typical content |
|---|---|
| 1–2 | a few simple parts, serial joints, a driven angle |
| 3–4 | one closed loop or one coupling, limits, parts with fillets, patterns and fits |
| 5–6 | several closed loops or couplings, configurations, sheet-metal or printed parts, checks over the motion |
| 7–8 | many coupled loops, subassemblies, configurations that follow `t`, process checks across parts, kernel or solver limits to navigate |
| 9–10 | large coupled machines, freeform parts, expert domain knowledge |

Tiers roughly: simple 1–3, difficult 4–6, complex 7–10. The folders are numbered in `CATALOGUE.md`'s order (simple to
complex). The id (and the file names) never carry the number, so ids stay stable.

**Done, for one assembly:** `tools/assemblies.py check <id>` passes · the preview is rendered at the pin and looked at ·
README, meta.json and prompt.md are complete and true · reviewer PASS, score in `meta.json` · prompt tested · feedback
entries filed · committed by the coordinator and `tools/assemblies.py readme` run.

## 9. Before a session ends

Append to `log/devlog.md` (local): what landed, the numbers (load time, bake time, steps, score), what is open. Keep
`tools/assemblies.py check` green for every committed assembly: a session can end abruptly, and the dev log plus a
clean tree is how the next one picks up.
