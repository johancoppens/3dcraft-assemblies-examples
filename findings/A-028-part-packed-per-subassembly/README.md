# File size: a part shared by several subassemblies is packed once inside each of them

Found while building `corexy-printer` at 3DCraft `150f0015`.

**What happens.** `assembly.pack` packs each subassembly first, its own parts inside it, and the parent then packs the
subassemblies. A part used by two subassemblies and by the parent is stored three times in the packed file: inside each
subassembly's own document and once at the top. Build `part.json` (`.3dcraft`), `sub1.json` and `sub2.json`
(`.3dcraftasm`) and `top.json` with `assembly.pack`, then look at the entries of the packed file (`unzip -lv`): a 1.7 KB part gives a 1.7 KB entry and two 3.1 KB
subassembly entries that each hold their own copy of it. In the printer, one 66 KB T-slot profile is packed three times
(top level through `frame` and `gantry` and once directly would be three; `frame` alone holds its own copy), which is
how a 1 MB file budget is spent: packing is `blobs/<sha256>.3dcraft` entries, each one once, but a subassembly's own
packed content sits *inside* its blob, so the deduplication across subassemblies never sees it.

**Should.** Pack the subassemblies' own parts as entries of the top-level file, deduplicated by their hash, so a part
shared across several subassemblies is stored once.

**Impact on the assembly.** Workaround: the printer's bed uses a separate simple box section instead of the T-slot
profile for its arms and cross beam, to keep the packed size under 1 MB (960 KB).
