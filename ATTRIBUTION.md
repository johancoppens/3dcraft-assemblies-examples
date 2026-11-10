# Attribution

Designs, parts and data from elsewhere used by the assemblies, with their licences (AGENTS.md §1). Every row is added
in the same change as what it credits.

| Used in | What | Source | Licence |
|---|---|---|---|
| `jansen-walker` | The Jansen linkage's proportions, the "holy numbers" | Theo Jansen; read in Wang, arXiv:2606.22129, Wikipedia's ratio table and the OpenSCAD Wikibooks code | Credited; "Strandbeest" is his name for his works |
| `corexy-printer` | T-slot aluminium profile 30x30 (`parts/t-slot-profile.json`), copied at the pin with its finish changed to black anodised and six datum planes added | [`3dcraft-examples/examples/02-t-slot-profile`](https://github.com/johancoppens/3dcraft-examples/tree/8db6bab/examples/02-t-slot-profile) (commit `8db6bab`), © 2026 Johan Coppens | MIT |

## Products, makers and catalogues

Product and company names belong to their owners. They are used here only to say what a part fits, is sized after
or was compared with; no assembly is affiliated with or endorsed by any of them. The rows below say which values
came from which maker's catalogue, data sheet or guide; each page cites the document, mostly with its address.
Dimensions from standards are according to the standard the page names (no text or figure of a standard is
reproduced); papers, handbooks and encyclopedias are cited on the pages and not listed here.

| Assembly | Maker and document | Values taken |
|---|---|---|
| `toggle-clamp` | DESTACO 217-U, catalogue sheet *217 Series*; DESTACO 215-U and 225-U data sheets; OSH Cut (A1008 steel); Five Flute, *Sheet Metal DFM Design Guidelines*; Firgelli Automations, *De-sta-co Toggle Clamp Mechanism* | The clamp's openings, M6 spindle, overall length and height, bar tip, base, mounting pattern, slots and holes, height under the bar, the bar pivot and the pivot centres read off its side view, the 2.5 mm stock and the 900 N class (217-U); the class check (215-U, 225-U); the 12 gauge comparison (OSH Cut); bend radius, hole and relief rules (Five Flute); the 3° over-centre (Firgelli) |
| `jansen-walker` | Fabory and Westfield Fasteners listings | The M4 DIN 125-1 A washer, 4.3 × 9 × 0.8 mm |
| `scissor-jack` | Draper 69252 data sheet and 69251 product page; Eufab 21032 instruction manual | The 1 t load and lift range class (69251, Eufab); the saddle pad, the foot's size class and the crank's length class (69252); the folded length class (Eufab) |
| `task-lamp` | Gibbs Wire & Steel data sheet No. 1004; Master Spring & Wire Form Co., *Properties of materials*; Firgelli Automations' and RoyMech's spring pages; Autodesk Inventor's extension-spring help; Caledonian, RR Kabel and Nexans H03VV-F data sheets; Engineering Toolbox | Music wire's tensile strength; the shear modulus and design stress; the spring rate, Wahl factor and initial stress; the extension spring's length and index rules; the cord's diameter and bend radius; leather-on-wood friction. The lamp is not sized after any maker's lamp |
| `corexy-printer` | HIWIN MGN/MGW catalogue GW-11-5-EN-2207-K; Songyang SY42STH38-1684A drawing (via Pololu 2267); Gates *Light Power & Precision Drive Design Manual* and a Rubix listing of Gates 2MGT; NMB and NSK F695ZZ data sheets; Handson Technology MCH1178 flanged T8 nut; E3D V6 heater block drawing, with 3dprint.wiki and a reseller's description; Makerstore 17HD40005-300N; Misumi HFS6-3030 (through the copied T-slot profile) | The MGN12H block and MGN12 rail; the NEMA 17 motor's square, bolt spacing, boss, shaft and body; the 20-groove pulley's pitch and outside diameters, the belt's pitch, tooth and thickness, flanges, idler minimums and wrap; the F695ZZ idler bearing; the lead-screw nut's flange, holes and body; the hot end's block, nozzle thread, cartridge bore, heat sink and length; that a NEMA 17 with an integrated lead screw exists; the profile's catalogue area and moment of inertia, asserted |
| `radial-engine` | Continental R-670 (through Wikipedia's *Continental R-670*); *Continental's Radial Aircraft Engines* (enginehistory.org) | The R-670's bore (130.2 mm; the model's default is 130 mm), stroke 117.5 mm and compression 5.4:1, its overall diameter and 225 hp as a comparison; the construction of cylinders, rods and crank, the valve gear's layout and the cam ring's 1/6 ratio (the A-70 and W670) |
