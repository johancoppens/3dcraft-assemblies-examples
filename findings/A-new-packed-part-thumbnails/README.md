# A packed assembly carries a thumbnail for every part with public parameters

**Performance (file size). 3DCraft 45233bdc, found in 16-radial-engine-valves.** `assembly.pack` stores each source
document as it was saved, and a document with public parameters is saved with its 400 x 300 `thumb.png` (`file.save`
draws one for a Jig). Inside a packed assembly nobody shows those pictures, but they count against the size. Together
with pretty-printed manifests in an uncompressed ZIP (examples F-138, F-080), they take the radial engine with its valve
train over the 1 MB budget: of 1,007,330 bytes, about 216 KB were thumbnails (the assembly's own 37.6 KB, crankcase half
29.8, piston 28.7, barrel 23.6, master rod 21.1, head 19.2, articulated rod 17.2, crank halves 15.0 and 12.7, pushrod
11.2). A subassembly packs its own parts with theirs (the cylinder unit's barrel and head).

Reproduce: `craft3d-cli run --new '{"units":"mm"}' --script part.json --out part.3dcraft`, then
`craft3d-cli run --new '{"units":"mm"}' --script repro.json --cmd assembly.pack --out a.3dcraftasm`, and
`unzip -l a.3dcraftasm` and `unzip -l` of the blob inside: the packed part carries `thumb.png`.

**Should:** pack without the thumbnails of the packed documents (they can be drawn again when one is unpacked), or
compress the archive. **Impact:** workaround used: the barrel's sixteen fins were redrawn as a chained `sketch.pattern`
(48 KB less), which brought the file to 965 KB.
