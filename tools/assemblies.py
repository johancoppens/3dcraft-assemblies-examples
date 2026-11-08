#!/usr/bin/env python3
"""Build, render and check the 3DCraft example assemblies (AGENTS.md).

  tools/assemblies.py build    [ID ...]   parts/*.json and build.json -> ID.3dcraftasm (packed) and its exports;
                                          document.check; stats into meta.json
  tools/assemblies.py render   [ID ...]   ID.3dcraftasm -> preview.png in the gallery look
  tools/assemblies.py check    [ID ...]   rebuild in a scratch folder and check what AGENTS.md asks, at rest and
                                          over the motion (--quick skips the ranges and the corners)
  tools/assemblies.py coverage            the 3DCraft commands and joint kinds the assemblies use, and those none uses
  tools/assemblies.py readme              rewrite the gallery table in README.md from the meta.json files

Without an ID: every assembly under assemblies/. Every craft3d-cli run is capped in memory (systemd-run, when there
is one) and in time, and waits while the machine is short of memory. CRAFT3D_CLI names the binary (default:
craft3d-cli on PATH); it must be the 3DCraft commit pinned in tools/pin.json. CRAFT3D_SLICE names the shared slice
(default assemblies.slice). Exit code 0 when all passed.
"""

import argparse
import fnmatch
import itertools
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSEMBLIES = ROOT / "assemblies"
SCRATCH = ROOT / ".scratch"  # on disk: /tmp is held in memory on the developer's laptop
PIN = json.loads((ROOT / "tools" / "pin.json").read_text())

# The gallery look (AGENTS.md, The preview). meta.json "preview" may change only the framing keys below.
RENDER = {"width": 1600, "height": 1200, "view": "iso", "projection": "perspective", "zoom": 1,
          "renderer": "cpu"}
LOOK = {"mode": "studio", "environment": "workshop", "tonemap": "aces", "exposure": 0.5,
        "background": "plain", "accumulate": 8}
PREVIEW_KEYS = {"view", "zoom", "camera", "projection", "box"}
PREVIEW_LOOK_KEYS = {"light", "rotation", "reflections"}

TIERS = ("simple", "difficult", "complex")
BUDGET_LOAD_S = {"simple": 1.0, "difficult": 2.0, "complex": 4.0}
BUDGET_FACTOR = 3  # CPU time, a whole motion and the slowest range point: at most this times the load budget
BUDGET_BYTES = 1_000_000
STEP_GUIDE = {"simple": 120, "difficult": 300, "complex": 600}
BAKE_FRAMES = 120
COLLISION_MOMENTS = 120
CORNER_MOMENTS = 30
MIN_SAMPLES = 73
MAX_CORNERS = 8
MIN_ASSERTIONS = 3
MIN_AVAILABLE_GB = 1.5
LICENCES = ("CC-BY-4.0", "MIT")
REQUIRED_META = ("id", "title", "summary", "description", "domain", "process", "tier",
                 "difficulty", "standards", "materials", "motion", "contacts")
REQUIRED_FILES = ("build.json", "meta.json", "README.md", "prompt.md")
MATE_KINDS = ("fixed", "revolute", "slider", "cylindrical", "planar", "ball")
COUPLING_KINDS = ("gear", "rack", "screw", "linear")
EXPORT_COMMANDS = ("file.export", "cut.export")
# Session-only families, and commands that edit or query rather than build: a script has no use for them.
NOT_IN_SCOPE = ("jig.", "recovery.", "session.", "agent.", "select.", "history.", "edit.", "file.list",
                "file.activate", "file.close", "file.open", "file.new", "file.save", "file.import",
                "view.scrub", "view.pick", "param.", "font.", "ui.")
DEFAULT_NAME = re.compile(r"^[A-Za-z]+[0-9]+$")
AUTOMATIC_MATE = re.compile(r"^Mate[0-9]+$")
AUTOMATIC_COUPLING = re.compile(r"^Coupling[0-9]+$")
VARIABLE_NAME = re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]+)*$")
JOINT_VARIABLE = re.compile(r"^(?P<mate>.+)_(angle|distance|x|y)$")
GALLERY_START = "<!-- gallery:start -->"
GALLERY_END = "<!-- gallery:end -->"

_cli = None
MEASURED_AT_LOAD = 0.0  # the 1-minute load average when the last timings were taken


class CheckError(Exception):
    pass


def die(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(2)


def cli():
    """The craft3d-cli binary, checked once against the pinned commit."""
    global _cli
    if _cli is None:
        path = os.environ.get("CRAFT3D_CLI") or shutil.which("craft3d-cli")
        if not path or not os.access(path, os.X_OK):
            die("craft3d-cli not found: put it on PATH or set CRAFT3D_CLI")
        version = subprocess.run([path, "--version"], capture_output=True, text=True).stdout
        if PIN["commit"][:12] not in version or f"format {PIN['format_version']}" not in version:
            die(f"{path} is {version.strip()!r}, not 3DCraft {PIN['commit'][:12]} (tools/pin.json): install that "
                "build or ask the coordinator to move the pin")
        _cli = path
    return _cli


def available_gb():
    for line in Path("/proc/meminfo").read_text().splitlines():
        if line.startswith("MemAvailable:"):
            return int(line.split()[1]) / 1048576
    return float("inf")


def wait_for_memory(patience=1800):
    """Waits while the machine is short of memory: the laptop has crashed on runaway processes."""
    start = time.monotonic()
    while available_gb() < MIN_AVAILABLE_GB:
        if time.monotonic() - start > patience:
            raise CheckError(f"only {available_gb():.1f} GB available after waiting {patience} s: try again later")
        time.sleep(15)


def run_cli(args, cwd, memory="3G", timeout=900):
    """Runs craft3d-cli under a memory cap and a timeout; returns (result, seconds)."""
    wait_for_memory()
    command = [cli()] + [str(a) for a in args]
    if shutil.which("systemd-run") and not os.environ.get("CRAFT3D_NO_CAP"):
        slice_ = f"--slice={os.environ.get('CRAFT3D_SLICE', 'assemblies.slice')}"
        command = ["systemd-run", "--user", "--scope", "-q", slice_, "-p", f"MemoryMax={memory}",
                   "-p", "MemorySwapMax=0", "timeout", str(timeout)] + command
    elif shutil.which("timeout"):
        command = ["timeout", str(timeout)] + command
    start = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    # CPU time of the run (all threads): what a single-threaded host such as the web build pays.
    result.cpu_seconds = (after.ru_utime - before.ru_utime) + (after.ru_stime - before.ru_stime)
    return result, time.monotonic() - start


def explain_failure(result, what):
    code = result.returncode
    reason = {137: "killed at the memory cap", 124: "timed out"}.get(code, f"exit code {code}")
    tail = "\n".join((result.stdout.strip().splitlines() + result.stderr.strip().splitlines())[-8:])
    return f"{what}: {reason}\n{tail[:3000]}"


def json_lines(result):
    """The JSON objects a craft3d-cli run printed, one per command."""
    lines = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                lines.append(json.loads(line))
            except ValueError:
                pass
    return lines


def slug(folder):
    """An assembly's id: its folder's name without the leading number (`01-toggle-clamp`)."""
    return re.sub(r"^[0-9]{2}-", "", folder)


def assembly_ids(given):
    """The assemblies' folders, in their order; a given name may be the folder or the id."""
    folders = sorted(p.parent.name for p in ASSEMBLIES.glob("*/build.json")
                     if not p.parent.name.startswith("00-"))  # 00 is for local tool tests
    if not given:
        return folders
    chosen = []
    for name in given:
        match = [f for f in folders if name in (f, slug(f))]
        if not match:
            die(f"no assembly {name} (assemblies/<NN>-{name}/build.json)")
        chosen.append(match[0])
    return chosen


def read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as e:
        raise CheckError(f"{path}: {e}")


def write_meta(directory, meta):
    (directory / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")


def step_id(step):
    if isinstance(step, list) and step:
        return step[0]
    if isinstance(step, dict):
        return step.get("command", "?")
    return "?"


def step_params(step):
    if isinstance(step, list) and len(step) > 1:
        return step[1]
    if isinstance(step, dict):
        return step.get("params", {})
    return {}


def deflate_zip(path):
    """Rewrites a ZIP-based export (3MF) with deflate (3DCraft stores it uncompressed, F-080). Entries, order, names
    and dates stay as they are, so the result is as deterministic as the export."""
    with zipfile.ZipFile(path) as z:
        entries = [(info, z.read(info.filename)) for info in z.infolist()]
    temporary = path.with_suffix(path.suffix + ".deflating")
    with zipfile.ZipFile(temporary, "w") as z:
        for info, data in entries:
            copy = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            copy.external_attr = info.external_attr
            copy.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(copy, data, compresslevel=9)
    temporary.replace(path)


def manifest(path):
    with zipfile.ZipFile(path) as z:
        return json.loads(z.read("manifest.json"))


def check_report(lines, what):
    """The document.check answer that ends a script's output."""
    if not lines:
        raise CheckError(f"{what}: no document.check result in the output")
    report = lines[-1]
    if not report.get("ok"):
        raise CheckError(f"{what}: document.check is not ok:\n" + json.dumps(
            {k: report.get(k) for k in ("problems", "assertionSummary")}, indent=1)[:3000])
    return report


def count_of(value):
    """A count that assembly.inspect gives as a list or as a number."""
    return len(value) if isinstance(value, (list, dict)) else (value or 0)


def scripts_of(source):
    """(path, steps, is_subassembly) of every part script: plain parts first, then subassemblies, in name order."""
    found = []
    for path in sorted((source / "parts").glob("*.json")):
        steps = read_json(path)
        if not isinstance(steps, list) or not steps:
            raise CheckError(f"parts/{path.name} must be a non-empty JSON list of steps")
        if step_id(steps[-1]) != "document.check":
            raise CheckError(f"parts/{path.name} must end with document.check")
        found.append((path, steps, step_id(steps[0]) == "assembly.new"))
    if not found:
        raise CheckError("no parts/*.json")
    return sorted(found, key=lambda f: (f[2], f[0].name))


def export_step(export, target):
    params = {k: v for k, v in export.items() if k not in ("command", "values", "part")}
    command = export.get("command", "file.export")
    if command not in EXPORT_COMMANDS:
        raise CheckError(f"export command {command!r} must be one of {EXPORT_COMMANDS}")
    path = params.get("path", "")
    if not path.startswith("exports/"):
        raise CheckError(f"export path {path!r} must start with exports/")
    (target / path).parent.mkdir(parents=True, exist_ok=True)
    return ["--cmd", command, "--params", json.dumps(params)]


def build_exports(meta, final, target):
    """Exports at the defaults of one document share a run; an export with "values" gets a run of its own, so its
    values never leak into another export."""
    shared, separate = {}, []
    for export in meta.get("exports", []):
        step = export_step(export, target)
        document = final if "part" not in export else next(
            iter(sorted((target / "parts").glob(export["part"] + ".3dcraft*"))), None)
        if document is None:
            raise CheckError(f"export of part {export['part']!r}: no such part")
        if export.get("values"):
            separate.append(["run", document, "--cmd", "param.set",
                             "--params", json.dumps({"values": export["values"], "clamp": False})] + step)
        else:
            shared.setdefault(document, ["run", document])
            shared[document] += step
    for args in list(shared.values()) + separate:
        result, _ = run_cli(args, cwd=target)
        if result.returncode != 0:
            raise CheckError(explain_failure(result, "exports failed"))
    for export in meta.get("exports", []):
        if export.get("path", "").endswith(".3mf"):
            deflate_zip(target / export["path"])


def build_into(aid, target, meta):
    """Builds the assembly's sources in the scratch folder target. Returns (stats, documents, script)."""
    global MEASURED_AT_LOAD
    source = ASSEMBLIES / aid
    new = json.dumps({"units": meta.get("units", "mm")})
    (target / "parts").mkdir(parents=True, exist_ok=True)
    documents, steps, part_assertions = {}, 0, 0
    for path, part_steps, is_subassembly in scripts_of(source):
        out = Path("parts") / (path.stem + (".3dcraftasm" if is_subassembly else ".3dcraft"))
        result, _ = run_cli(["run", "--new", new, "--script", path, "--out", out], cwd=target)
        if result.returncode != 0:
            raise CheckError(explain_failure(result, f"parts/{path.name} failed"))
        report = check_report(json_lines(result), f"parts/{path.name}")
        part_assertions += (report.get("assertionSummary") or {}).get("count", 0)
        documents[path.stem] = (manifest(target / out), part_steps)
        steps += len(part_steps)

    script = read_json(source / "build.json")
    if not isinstance(script, list) or not script or step_id(script[0]) != "assembly.new":
        raise CheckError("build.json must be a list of steps starting with assembly.new")
    if step_id(script[-1]) != "document.check":
        raise CheckError("build.json must end with document.check")
    bad = sorted({step_id(s) for s in script if step_id(s).startswith("file.") or step_id(s) == "assembly.pack"})
    if bad:
        raise CheckError(f"build.json must not use {bad}: the tool saves and packs")
    building = target / f".{slug(aid)}.building.3dcraftasm"
    result, seconds = run_cli(["run", "--new", new, "--script", source / "build.json", "--cmd", "assembly.pack",
                               "--cmd", "document.check", "--out", building], cwd=target)
    if result.returncode != 0:
        building.unlink(missing_ok=True)
        raise CheckError(explain_failure(result, "build.json failed"))
    report = check_report(json_lines(result), "build.json")
    final = target / f"{slug(aid)}.3dcraftasm"
    building.replace(final)
    steps += len(script)
    build_exports(meta, final, target)

    # The least of two openings: other work on the machine only ever adds time.
    load_s = load_cpu_s = None
    for _ in range(2):
        result, opened = run_cli(["info", final], cwd=target)
        if result.returncode != 0:
            raise CheckError(explain_failure(result, "craft3d-cli info failed"))
        load_s = opened if load_s is None else min(load_s, opened)
        load_cpu_s = result.cpu_seconds if load_cpu_s is None else min(load_cpu_s, result.cpu_seconds)
    MEASURED_AT_LOAD = os.getloadavg()[0]

    result, _ = run_cli(["run", final, "--cmd", "assembly.solve", "--cmd", "assembly.inspect", "--cmd", "motion.bake",
                         "--params", json.dumps({"frames": BAKE_FRAMES})], cwd=target, timeout=1800)
    if result.returncode != 0:
        raise CheckError(explain_failure(result, "solve, inspect or bake failed"))
    solve, inspect, bake = json_lines(result)
    if not solve.get("ok") or solve.get("failed"):
        raise CheckError("assembly.solve is not ok:\n" + json.dumps(
            {k: solve.get(k) for k in ("error", "failed", "dof")}, indent=1)[:3000])
    if (bake.get("configurations") or {}).get("failed"):
        raise CheckError("the bake failed to build configurations: " + json.dumps(bake)[:1000])
    ids = Counter(step_id(s) for s in script)
    assertions = report.get("assertionSummary") or {}
    doc = manifest(final)
    documents[None] = (doc, script)
    return {
        "steps": steps,
        "parts": len(documents) - 1,
        "instances": count_of(inspect.get("instances")),
        "configurations": count_of(inspect.get("configurations")),
        "mates": count_of(inspect.get("mates")),
        "couplings": count_of(inspect.get("couplings")),
        "dof": solve.get("dof"),
        "parameters": ids["variable.publish"],
        "assertions": assertions.get("count", ids["assert.add"]),
        "part_assertions": part_assertions,
        "warnings": len(assertions.get("unproven", [])),
        "build_s": round(seconds, 2),
        "load_s": round(load_s, 2),
        "load_cpu_s": round(load_cpu_s, 2),
        "bake_s": round(bake.get("ms", 0) / 1000, 2),
        "bake_mb": bake.get("megabytes"),
        "file_bytes": final.stat().st_size,
    }, documents


def timing_sink(errors, warnings):
    """Timings taken while the machine is busy only warn: other work inflates them. Returns (list, note)."""
    busy = MEASURED_AT_LOAD > (os.cpu_count() or 1) / 2
    note = (f" (measured at load average {MEASURED_AT_LOAD:.1f} on {os.cpu_count()} CPUs: "
            "re-measure at a quiet moment)") if busy else ""
    return (warnings if busy else errors), note


def lint_document(label, doc, script, errors, warnings):
    """Names and document.info of one document, a part's or the assembly's."""
    body = doc.get("document", {})
    assembly = body.get("assembly") or {}
    tools = {f.get("kind", {}).get("tool") for f in body.get("features", [])
             if f.get("kind", {}).get("type") == "boolean"}
    for feature in body.get("features", []):
        name = feature.get("name", "")
        if DEFAULT_NAME.match(name):
            if feature.get("id") in tools:
                warnings.append(f"{label}: feature {name!r} keeps its automatic name (the tool of a boolean)")
            else:
                errors.append(f"{label}: feature {name!r} has an automatic name: name it for its intent")
    for assertion in body.get("assertions", []):
        if DEFAULT_NAME.match(assertion.get("name", "")):
            errors.append(f"{label}: assertion {assertion.get('name')!r} has an automatic name")
    mates = {m.get("name", "") for m in assembly.get("mates", [])}
    for mate in mates:
        if AUTOMATIC_MATE.match(mate):
            errors.append(f"{label}: mate {mate!r} has an automatic name")
    for coupling in assembly.get("couplings", []):
        if AUTOMATIC_COUPLING.match(coupling.get("name", "")):
            errors.append(f"{label}: coupling {coupling.get('name')!r} has an automatic name")
    for variable in body.get("variables", []):
        name = variable.get("name", "")
        joint = JOINT_VARIABLE.match(name)
        if name == "t" and assembly or joint and joint.group("mate") in mates:
            continue
        if not VARIABLE_NAME.match(name) or len(name) < 3:
            errors.append(f"{label}: variable {name!r}: use a descriptive snake_case name of 3+ letters")
    infos = [step_params(s) for s in script if step_id(s) == "document.info"]
    if not infos:
        errors.append(f"{label}: no document.info (title, description, author, licence)")
    elif infos[-1].get("licence") not in LICENCES:
        errors.append(f"{label}: licence {infos[-1].get('licence')!r} must be one of {LICENCES}")


def lint(aid, meta, documents, stats):
    """Returns (errors, warnings) for names, budgets and the meta.json fields."""
    errors, warnings = [], []
    for key in REQUIRED_META:
        if key not in meta or meta[key] in ("", None):
            errors.append(f"meta.json: missing {key}")
    if meta.get("id") != slug(aid):
        errors.append(f"meta.json: id is {meta.get('id')!r}, not {slug(aid)!r}")
    tier = meta.get("tier")
    if tier not in TIERS:
        errors.append(f"meta.json: tier must be one of {', '.join(TIERS)}")
        tier = "complex"
    for key in meta.get("preview", {}):
        if key == "look":
            if set(meta["preview"]["look"]) - PREVIEW_LOOK_KEYS:
                errors.append(f"meta.json: preview.look may only set {sorted(PREVIEW_LOOK_KEYS)}")
        elif key not in PREVIEW_KEYS:
            errors.append(f"meta.json: preview may only set {sorted(PREVIEW_KEYS)} and look")
    for part, (doc, script) in documents.items():
        lint_document(part if part else "build.json", doc, script, errors, warnings)
    expected_dof = (meta.get("motion") or {}).get("dof", 0)
    if stats["dof"] != expected_dof:
        errors.append(f"{stats['dof']} degrees of freedom left, meta.json motion.dof says {expected_dof}")
    timing, note = timing_sink(errors, warnings)
    exempt = meta.get("budget_exception")
    budget = BUDGET_LOAD_S[tier]
    if stats["load_s"] > budget and not exempt:
        timing.append(f"loads in {stats['load_s']} s, budget {budget} s for {tier}{note}")
    if stats["load_cpu_s"] > BUDGET_FACTOR * budget and not exempt:
        timing.append(f"loads in {stats['load_cpu_s']} s of CPU, budget {BUDGET_FACTOR * budget} s for {tier}{note}")
    if stats["bake_s"] > BUDGET_FACTOR * budget and not exempt:
        timing.append(f"a whole motion bakes in {stats['bake_s']} s, budget {BUDGET_FACTOR * budget} s for {tier}{note}")
    if stats["file_bytes"] > BUDGET_BYTES and not exempt:
        errors.append(f"{stats['file_bytes']} bytes, budget {BUDGET_BYTES}")
    if stats["steps"] > STEP_GUIDE[tier]:
        warnings.append(f"{stats['steps']} steps, guide {STEP_GUIDE[tier]} for {tier}")
    if not 2 <= stats["parameters"] <= 4:
        warnings.append(f"{stats['parameters']} public parameters (AGENTS.md asks 2 to 4)")
    if stats["assertions"] < MIN_ASSERTIONS:
        errors.append(f"{stats['assertions']} assertions on the assembly, at least {MIN_ASSERTIONS}")
    if stats["warnings"]:
        warnings.append(f"{stats['warnings']} assertion(s) not proven: explain in the README")
    return errors, warnings


def motion_problems(answer, where, allowed_dead):
    problems = []
    dead = answer.get("deadPoints") or []
    if len(dead) > allowed_dead:
        problems.append(f"{where}: dead points {json.dumps(dead)[:500]}")
    for assertion in answer.get("assertions", []):
        if assertion.get("status") != "passed":
            problems.append(f"{where}: assertion {assertion.get('name')!r} is {assertion.get('status')} over the "
                            f"motion: {json.dumps({k: assertion.get(k) for k in ('firstFailure', 'firstError', 'firstNotProven', 'min', 'max')})[:500]}")
    return problems


def range_corners(final, target):
    """Up to MAX_CORNERS corners of the public ranges, as param.set values (the even-parity half when there are more)."""
    result, _ = run_cli(["run", final, "--cmd", "param.list"], cwd=target)
    if result.returncode != 0:
        raise CheckError(explain_failure(result, "param.list failed"))
    axes = []
    for parameter in (json_lines(result) or [{}])[-1].get("parameters", []):
        name, kind = parameter["name"], parameter.get("kind", "number")
        if kind == "boolean":
            axes.append([(name, False), (name, True)])
        elif kind == "choice":
            choices = parameter.get("choices") or []
            if len(choices) > 1:
                axes.append([(name, choices[0]), (name, choices[-1])])
        elif (parameter.get("min") or {}).get("value") is not None and (parameter.get("max") or {}).get("value") is not None:
            axes.append([(name, parameter["min"]["value"]), (name, parameter["max"]["value"])])
    corners = list(itertools.product(*[range(2)] * len(axes)))
    if len(corners) > MAX_CORNERS:
        corners = [c for c in corners if sum(c) % 2 == 0][:MAX_CORNERS]
    return [{axes[i][bit][0]: axes[i][bit][1] for i, bit in enumerate(c)} for c in corners] if axes else []


def check_motion(final, meta, target, quick):
    """motion.check at the defaults and at the corners of the public ranges. Returns (problems, notes)."""
    motion = meta.get("motion") or {}
    samples = max(motion.get("samples", MIN_SAMPLES), MIN_SAMPLES)
    allowed = motion.get("dead_points", 0)
    check = json.dumps({"samples": samples})
    result, seconds = run_cli(["run", final, "--cmd", "motion.check", "--params", check], cwd=target, timeout=1800)
    if result.returncode != 0:
        return [explain_failure(result, "motion.check failed")], []
    problems = motion_problems(json_lines(result)[-1], "over the motion", allowed)
    notes = [f"motion.check passed at {samples} samples in {seconds:.0f} s"] if not problems else []
    if quick:
        return problems, notes
    corners = range_corners(final, target)
    for values in corners:
        result, _ = run_cli(["run", final, "--cmd", "param.set", "--params", json.dumps({"values": values, "clamp": True}),
                             "--cmd", "motion.check", "--params", check], cwd=target, timeout=1800)
        if result.returncode != 0:
            problems.append(explain_failure(result, f"motion.check failed at {values}"))
        else:
            problems += motion_problems(json_lines(result)[-1], f"over the motion at {values}", allowed)
    if corners:
        notes.append(f"motion.check at {len(corners)} corners of the ranges")
    return problems, notes


def contact_allowed(a, b, contacts):
    def matches(pattern, name):
        return fnmatch.fnmatchcase(name, pattern.replace("[", "[[]"))
    for contact in contacts:
        p, q = contact.get("pair", ("", ""))
        if (matches(p, a) and matches(q, b)) or (matches(p, b) and matches(q, a)):
            return True
    return False


def collisions_over(final, meta, target, where, moments, setup=()):
    """Runs the motion at moments + 1 moments with collisions on. Returns (problems, listed pairs, seconds)."""
    steps = list(setup) + [["view.motion", {"t": k / moments, "collisions": True}] for k in range(moments + 1)]
    script = target / "collisions.json"
    script.write_text(json.dumps(steps))
    result, seconds = run_cli(["run", final, "--script", script], cwd=target, memory="3G", timeout=3000)
    if result.returncode != 0:
        return [explain_failure(result, f"the collision run failed {where}")], 0, seconds
    pairs, unknown, dead = {}, {}, []
    for moment in json_lines(result):
        if moment.get("deadPoint") is not None:
            dead.append(moment.get("t"))
        for hit in moment.get("collisions") or []:
            key = tuple(sorted((hit.get("aName", "?"), hit.get("bName", "?"))))
            if "unknown" in hit or hit.get("volume") is None:
                unknown.setdefault(key, hit.get("unknown", ""))
            else:
                worst = pairs.setdefault(key, [0.0, moment.get("t")])
                if hit["volume"] > worst[0]:
                    worst[0], worst[1] = hit["volume"], moment.get("t")
    contacts = meta.get("contacts") or []
    problems = [f"{a} and {b} collide {where}, up to {v:.3g} mm³ (t = {t:.3f}): clear them or list them in meta.json contacts"
                for (a, b), (v, t) in sorted(pairs.items()) if not contact_allowed(a, b, contacts)]
    problems += [f"{a} and {b}: collision unknown {where} ({why})" for (a, b), why in sorted(unknown.items())
                 if not contact_allowed(a, b, contacts)]
    if dead and not (meta.get("motion") or {}).get("dead_points"):
        problems.append(f"a dead point in the motion {where} at t = {dead[:5]}")
    return problems, sum(1 for (a, b) in pairs if contact_allowed(a, b, contacts)), seconds


def check_collisions(final, meta, target, quick):
    """Named collisions over the motion at the defaults and at the corners of the public ranges. Returns (problems, notes)."""
    problems, allowed, seconds = collisions_over(final, meta, target, "at the defaults", COLLISION_MOMENTS)
    notes = [f"collisions at {COLLISION_MOMENTS + 1} moments in {seconds:.0f} s: {allowed} listed contact pair(s)"]
    if not quick:
        corners = range_corners(final, target)
        for values in corners:
            setup = [["param.set", {"values": values, "clamp": True}]]
            found, _, _ = collisions_over(final, meta, target, f"at {values}", CORNER_MOMENTS, setup)
            problems += found
        if corners:
            notes.append(f"collisions at {len(corners)} corners of the ranges, {CORNER_MOMENTS + 1} moments each")
    return problems, notes


def scratch_folder(aid):
    SCRATCH.mkdir(exist_ok=True)
    return tempfile.TemporaryDirectory(prefix=f"check-{aid}-", dir=SCRATCH)


def copy_results(aid, meta, target, directory):
    shutil.copy2(target / f"{slug(aid)}.3dcraftasm", directory)
    for export in meta.get("exports", []):
        destination = directory / export["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(target / export["path"], destination)


def cmd_build(ids):
    failed = 0
    for aid in ids:
        directory = ASSEMBLIES / aid
        try:
            meta = read_json(directory / "meta.json")
            with scratch_folder(aid) as scratch:
                target = Path(scratch)
                stats, documents = build_into(aid, target, meta)
                copy_results(aid, meta, target, directory)
            kept = (meta.get("stats") or {}).get("range_worst_s")
            meta["stats"] = stats | ({"range_worst_s": kept} if kept is not None else {})
            meta["craft3d"] = {"commit": PIN["commit"][:12], "format_version": documents[None][0].get("format_version")}
            write_meta(directory, meta)
            errors, warnings = lint(aid, meta, documents, stats)
            for w in warnings:
                print(f"{aid}: warning: {w}")
            for e in errors:
                print(f"{aid}: ERROR: {e}")
            print(f"{aid}: built, {stats['parts']} parts, {stats['instances']} instances, {stats['mates']} mates, "
                  f"{stats['couplings']} couplings, {stats['dof']} dof, {stats['steps']} steps, load {stats['load_s']} s, "
                  f"bake {stats['bake_s']} s, {stats['file_bytes']} bytes")
            failed += bool(errors)
        except CheckError as e:
            print(f"{aid}: FAILED: {e}")
            failed += 1
    return failed


def cmd_render(ids):
    failed = 0
    for aid in ids:
        directory = ASSEMBLIES / aid
        try:
            meta = read_json(directory / "meta.json")
            document = directory / f"{slug(aid)}.3dcraftasm"
            if not document.is_file():
                raise CheckError(f"no {slug(aid)}.3dcraftasm: run build first")
            params = dict(RENDER)
            look = dict(LOOK)
            for key, value in meta.get("preview", {}).items():
                if key == "look":
                    look.update({k: v for k, v in value.items() if k in PREVIEW_LOOK_KEYS})
                elif key in PREVIEW_KEYS:
                    params[key] = value
            if "camera" in params:
                # A camera is the whole framing: view, zoom and projection would contradict it.
                for key in ("view", "zoom", "projection", "box"):
                    params.pop(key, None)
            params["look"] = look
            params["path"] = "preview.png"
            result, seconds = run_cli(["run", document.name, "--cmd", "view.render", "--params", json.dumps(params)],
                                      cwd=directory, memory="3G", timeout=1800)
            if result.returncode != 0:
                raise CheckError(explain_failure(result, "view.render failed"))
            print(f"{aid}: preview.png, {(directory / 'preview.png').stat().st_size} bytes, {seconds:.0f} s")
        except CheckError as e:
            print(f"{aid}: FAILED: {e}")
            failed += 1
    return failed


def range_worst(output):
    match = re.search(r"max ([0-9.]+) (ms|s)", output)
    if not match:
        return None
    return round(float(match.group(1)) / (1000 if match.group(2) == "ms" else 1), 3)


def cmd_check(ids, quick):
    failed = 0
    for aid in ids:
        directory = ASSEMBLIES / aid
        problems, notes = [], []
        try:
            for name in REQUIRED_FILES + (f"{slug(aid)}.3dcraftasm", "preview.png"):
                if not (directory / name).is_file():
                    problems.append(f"missing {name}")
            meta = read_json(directory / "meta.json")
            with scratch_folder(aid) as scratch:
                target = Path(scratch)
                stats, documents = build_into(aid, target, meta)
                errors, warnings = lint(aid, meta, documents, stats)
                problems += errors
                notes += warnings
                name = f"{slug(aid)}.3dcraftasm"
                committed, rebuilt = directory / name, target / name
                if committed.is_file() and committed.read_bytes() != rebuilt.read_bytes():
                    problems.append(f"{name} is stale: run build")
                for export in meta.get("exports", []):
                    mine, fresh = directory / export["path"], target / export["path"]
                    if not mine.is_file():
                        problems.append(f"missing {export['path']}: run build")
                    elif fresh.is_file() and mine.read_bytes() != fresh.read_bytes():
                        problems.append(f"{export['path']} is stale: run build")
                found, said = check_motion(rebuilt, meta, target, quick)
                problems += found
                notes += said
                found, said = check_collisions(rebuilt, meta, target, quick)
                problems += found
                notes += said
                if not quick:
                    if stats["parameters"]:
                        result, seconds = run_cli(["check-range", rebuilt, "--samples", 8, "--seed", 1], cwd=target,
                                                  timeout=3600)
                        if result.returncode != 0:
                            problems.append(explain_failure(result, "check-range failed"))
                        else:
                            notes.append(f"check-range passed in {seconds:.0f} s")
                            worst = range_worst(result.stdout + result.stderr)
                            if worst is not None:
                                meta.setdefault("stats", {})["range_worst_s"] = worst
                                write_meta(directory, meta)
                                budget = BUDGET_FACTOR * BUDGET_LOAD_S.get(meta.get("tier"), 4.0)
                                sink, note = timing_sink(problems, notes)
                                if worst > budget and not meta.get("budget_exception"):
                                    sink.append(f"slowest range point {worst} s, budget {budget} s{note}")
                    for part, (_, script) in documents.items():
                        # An unpacked subassembly cannot be checked over its range (A-001); its parent's ranges cover it.
                        if part is None or step_id(script[0]) == "assembly.new" or not any(
                                step_id(s) == "variable.publish" for s in script):
                            continue
                        document = next(iter(sorted((target / "parts").glob(part + ".3dcraft*"))))
                        result, _ = run_cli(["check-range", document, "--samples", 4, "--seed", 1], cwd=target,
                                            timeout=3600)
                        if result.returncode != 0:
                            problems.append(explain_failure(result, f"check-range of part {part} failed"))
            if (meta.get("difficulty") or {}).get("score") is None:
                notes.append("no difficulty score yet (the reviewer gives it)")
            if not (meta.get("prompt_test") or {}).get("result"):
                notes.append("prompt not tested yet")
        except CheckError as e:
            problems.append(str(e))
        for n in notes:
            print(f"{aid}: note: {n}")
        for p in problems:
            print(f"{aid}: PROBLEM: {p}")
        print(f"{aid}: {'FAILED' if problems else 'ok'}")
        failed += bool(problems)
    return failed


def cmd_coverage():
    result, _ = run_cli(["commands"], cwd=ROOT)
    if result.returncode != 0:
        die(explain_failure(result, "craft3d-cli commands failed"))
    every = [line.strip() for line in result.stdout.splitlines()
             if line and not line[0].isspace() and re.match(r"^[a-z]+(\.[a-zA-Z]+)+$", line.strip())]
    families = ("assembly.", "instance.", "mate.", "joint.", "coupling.", "motion.", "view.motion", "view.trace",
                "view.drive", "measure.joint", "measure.pose")
    relevant = [c for c in every if c.startswith(families) and not c.startswith(NOT_IN_SCOPE)]
    used, mates, couplings = Counter(), Counter(), Counter()
    for aid in assembly_ids([]):
        directory = ASSEMBLIES / aid
        scripts = [read_json(directory / "build.json")] + [read_json(p) for p in sorted((directory / "parts").glob("*.json"))]
        ids = set()
        for script in scripts:
            ids |= {step_id(s) for s in script}
            for s in script:
                if step_id(s) == "mate.add":
                    mates[step_params(s).get("kind")] += 1
                elif step_id(s) == "coupling.add":
                    couplings[step_params(s).get("kind")] += 1
        for c in ids:
            used[c] += 1
    print(f"{len([c for c in relevant if used[c]])} of {len(relevant)} assembly commands used")
    for c in relevant:
        print(f"  {c:24s} {used[c] if used[c] else 'UNUSED'}")
    print("mate kinds:     " + ", ".join(f"{k} {mates[k]}" for k in MATE_KINDS))
    print("coupling kinds: " + ", ".join(f"{k} {couplings[k]}" for k in COUPLING_KINDS))
    return 0


def cmd_readme():
    rows = []
    for aid in assembly_ids([]):
        try:
            meta = read_json(ASSEMBLIES / aid / "meta.json")
        except CheckError:
            continue
        score = (meta.get("difficulty") or {}).get("score")
        if score is not None:  # the gallery shows reviewed assemblies only
            rows.append((aid, score, meta.get("title", aid), meta))
    lines = ["| | Assembly | Domain | Difficulty |", "|---|---|---|---|"]
    for aid, score, title, meta in rows:
        picture = (f'<img src="assemblies/{aid}/preview.png" width="240" alt="{title}">'
                   if (ASSEMBLIES / aid / "preview.png").is_file() else "")
        lines.append(f"| {picture} | **[{title}](assemblies/{aid}/)**<br>{meta.get('description', '')}"
                     f" | {meta.get('domain', '')} | {score}/10 |")
    readme = ROOT / "README.md"
    text = readme.read_text()
    if GALLERY_START not in text or GALLERY_END not in text:
        die("README.md lacks the gallery markers")
    head, rest = text.split(GALLERY_START, 1)
    _, tail = rest.split(GALLERY_END, 1)
    readme.write_text(head + GALLERY_START + "\n" + "\n".join(lines) + "\n" + GALLERY_END + tail)
    print(f"README.md: {len(rows)} assemblies")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("action", choices=("build", "render", "check", "coverage", "readme"))
    parser.add_argument("ids", nargs="*")
    parser.add_argument("--quick", action="store_true", help="check: skip the ranges and the corners")
    args = parser.parse_args()
    if args.action == "build":
        failed = cmd_build(assembly_ids(args.ids))
    elif args.action == "render":
        failed = cmd_render(assembly_ids(args.ids))
    elif args.action == "check":
        failed = cmd_check(assembly_ids(args.ids), args.quick)
    elif args.action == "coverage":
        failed = cmd_coverage()
    else:
        failed = cmd_readme()
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
