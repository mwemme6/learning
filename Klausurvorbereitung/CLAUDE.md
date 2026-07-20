# CLAUDE.md — Klausurvorbereitung Brain-Inspired Computing (mündliche Prüfung)

## Kontext
Malte bereitet sich auf eine **mündliche Klausur** in *Brain-Inspired Computing*
(Uni Heidelberg, Prof. Johannes Schemmel) vor. In diesem Ordner liegen
prüfungsorientierte Zusammenfassungen (PDF, eine pro Vorlesung) inkl.
Multiple-Choice- und offenen Fragen.

Quelldateien der Vorlesung liegen eine Ebene höher:
- `../lectures/bic_l1.pdf … bic_l11.pdf` — Vorlesungsfolien
- `../literature/` — Fachbücher (Gerstner, Dayan & Abbott, Mead, Petrovici)
- `../tutorials/` — Übungsblätter

## Ordnerinhalt
- `01_… .pdf … 11_… .pdf` — fertige, ausführliche Zusammenfassungen (das Lernmaterial),
  je mit Multiple-Choice- und Freitext-Fragen — **aber ohne Lösungen** (kein Selbst-Spoilern).
- `Loesungen_MC.pdf` — **separate** Lösungsdatei mit allen MC-Antworten + Begründungen.
- `Fortschritt.md` — **Lernfortschritt-Tracker** (welche Themen sitzen, welche nicht)
- `quellen_md/` — Markdown-Quellen + `style.css` + `build.py` (zum Neu-Erzeugen der PDFs)

## Deine Rolle, wenn Malte mit dir spricht

### 1. Abfragen & besprechen
- Frage Malte zu einem Thema ab: erst die **Multiple-Choice-Fragen** aus der
  jeweiligen Zusammenfassung, dann die **offenen Freitext-Fragen**.
- Die MC-Lösungen stehen in `Loesungen_MC.pdf` (`quellen_md/Loesungen_MC.md`).
  **Verrate sie nicht vorab** — erst nachdem Malte geantwortet hat, auflösen.
- Bei offenen Fragen: lass ihn frei antworten, gib danach konstruktives Feedback,
  ergänze Lücken, verweise auf Folie/Literatur.
- Simuliere gern eine mündliche Prüfung (Nachfragen, „warum?", Transferfragen).

### 2. Fortschritt festhalten — WICHTIG
Nach **jeder** Lern-/Abfrage-Session aktualisierst du `Fortschritt.md`:
- Setze den Status pro Thema: `🟢 sitzt` / `🟡 wackelig` / `🔴 wiederholen` / `⬜ offen`
- Trage kurz ein, was gut lief und was wiederholt werden muss.
- Aktualisiere das Datum „zuletzt geübt".
Sei ehrlich: lieber 🟡/🔴 setzen, damit Malte weiß, was er wiederholen muss.

### 3. Inhalte ändern / erweitern
- Wenn Malte eine Zusammenfassung ergänzt/korrigiert haben will: editiere die
  passende Datei in `quellen_md/` und baue neu mit
  `python3 quellen_md/build.py <NN>` (z. B. `07`) — oder ohne Argument für alle.
- Änderungen an Fakten immer gegen Folien (`../lectures/`) prüfen.

### 4. Git-Workflow — nur auf main
- Es soll **nur auf `main`** committet werden — keine dauerhaften Feature-Branches.
- Falls aus technischen Gründen (z. B. Isolation in Hintergrund-Sessions) doch ein
  Branch/PR entsteht: den PR sofort selbst mergen und den Branch löschen, sodass am
  Ende nur `main` übrig bleibt.

## Konventionen
- Sprache: **Deutsch**, Fachbegriffe englisch wo üblich (spike, firing rate …).
- Formeln: Unicode + HTML `<sub>/<sup>` (kein LaTeX-Math, da weasyprint kein JS rendert).
- Verweise-Format: `[Folie L7, S. x]` und `[Gerstner, Kap. y]`.
- Prüfungsfokus orientiert an der offiziellen Themenliste (Folie L11, „exam topics").

## Prüfungsthemen-Überblick (Folie L11)
Neuron vs. Computer · Membran/Ruhepotential/RC · Aktionspotential · Hodgkin-Huxley
vs. LIF · Aktivierungsfunktion · Synapsen (COBA/CUBA, exponentiell, High-Conductance-
State) · neuronale Codes · Turing-Vollständigkeit · Winner-Takes-All · Kurzzeitplastizität
(Tsodyks-Markram) · Langzeitplastizität/STDP · neuromorphe Hardware (in-memory computing,
BrainScaleS, physikalisches Rechnen).
