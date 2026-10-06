# B77_STATE_CURRENT

STATE: v1.7.9.4
CORE: v1.7.9.6
PROJECT: Б77 / «Что приготовить»
BRANCH: Stage14
WP: stage14.html
WP_STATUS: frozen / immutable
WP_SHA: 6d9038eb0b37f53698074be7ea1a0dc3b1eb77eb
SNAPSHOT: 4a1f68b795bfeaa26bb869473250db64fcfa8292
BACKUP: 6d9038eb0b37f53698074be7ea1a0dc3b1eb77eb

CURRENT: Scanner-Core bridge / E3-unverified
PREV: camera input verified; decode→handler failed
NEXT: computed after VERIFY; current dependency is Android barcode decode→existing handler
UNVERIFIED: Android camera decode runtime; full UI contour; full RC/RD after bridge
QUARANTINE: none

MATRIX: scanner/UI/DB/regression — not closed; Stage14 not completed

TASK:
Scanner-Core bridge verification and resolution of Android barcode decode→existing handler.

CANDIDATE:
branch: core35-scanner-v21-bridge
base: d5a77c141e268bd2275af8748c2c4e5db2fec27a
latest: 9b8b83b5924ed0649f53a528375e17cf9d4718be
diff: 1 file / stage14.html / +149 -4
status: NOT WP / NOT MERGED / runtime camera not verified

REGRESSION:
RC-01 Scanner | camera→decode→result→handler
RC-02 Products/Shopping/QR | contexts do not mix
RC-03 Recipe/DB | recipe list, add from DB, delete, KBJU
RC-04 Ingredients | normalization and product matching
RD-01 Core data | Core/DB source of truth checked against artifact

MECHANICS:
M1 Scanner: camera = input only; result → existing Core/common handler
M2 Products: code != product != purchase; one product may have multiple codes
M3 Shopping: scanning must not perform uncontrolled write; confirmation required
M4 QR: result/history must not mix with Products/Shopping mode
M5 WP cannot be replaced by a new solution without E3 and command to rewrite

MEMORY_PATH:
SCANNER → BARCODE → barcode_db → products → FIX6 → Stage14 → RC-01/02

TRANSFER:
⚑NEW CHAT → TRANSFER → VERIFY → rolling challenge → COMPUTED CONTINUE

SOURCE ROLES:
STATE = current project state
WP = working control point
MAP = architecture/dependencies
FIX6 = existing implementation source
V20 = visual/functional reference
AUDIT = proven gaps/defects
REGRESSION = control scenarios
CANDIDATE = unverified
SNAPSHOT/BACKUP = restore points
GitHub = backup/state recovery source

NOTE:
CORE v1.7.9.6 is active. The STATE version remains v1.7.9.4 until a new STATE is explicitly generated/approved; CORE version must not be silently substituted for STATE version.
