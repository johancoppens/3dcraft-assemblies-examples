# Missing capability: a mesh export cannot be turned into the print orientation

Provisional finding from `assemblies/05-corexy-printer` at 3DCraft `150f0015`.

`file.export` of a part to 3MF writes the body in the part's own axes (no `orientation`, `axis` or `rotation`
parameter). A printed part is drawn in the frame in which it mates, which is rarely the frame in which it prints best
(forks with their open side up, for example). The repository's rule for printed parts asks for a 3MF in the print
orientation. **Should:** `file.export` takes an orientation (a rotation vector, or a face to lay on the bed), so the
print orientation is part of the export command, in the part's own history or in the exporter's call.

**Impact.** The printed parts' 3MFs are exported in the mating orientation (`meta.json` `exports`); the README says so
and says how each part is oriented and where supports go.
