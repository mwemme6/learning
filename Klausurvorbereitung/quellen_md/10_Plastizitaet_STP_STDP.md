# 10 · Plastizität & Lernen: STP, LTP/LTD, STDP

<p class="sub">Brain-Inspired Computing · Vorlesung 10 · ausführliche Zusammenfassung</p>

## 1 · Wo sitzt das Gedächtnis?

Lernen und Gedächtnis werden überwiegend in **Synapsen** gespeichert — durch Anpassung
ihrer **Effizienz** (Gewicht). Daneben gibt es weitere plastische Mechanismen auf
unterschiedlichen Zeitskalen:

- **Strukturelle Plastizität:** Wachstum/Rückbildung von Dendriten, Zellwanderung,
  **Neubildung/Elimination** von Synapsen (Tage bis länger).
- **Intrinsische / homöostatische Plastizität:** Regulierung der **Erregbarkeit** über
  Leitwerte, um die eigene Aktivität um einen **Zielwert** (target rate) zu **stabilisieren**
  — verhindert Weglaufen der Aktivität (Runaway) und ergänzt die Hebb'sche Plastizität.
- **Synaptische Plastizität:** kurzzeitig (**STP**, ms–s, reversibel) und langzeitig
  (**LTP/LTD**, **STDP**, Stunden–dauerhaft).

**Illustration der Macht der Plastizität:** Leitet man auditorische Fasern früh in den
visuellen Cortex um (Sharma et al., 2000), bilden sich dort **orientierungsselektive**
Cluster wie in V1 → **funktionale Reorganisation** allein durch die Eingangsstatistik.

::: ref
**Verweise:** Folie L10 „learning", „intrinsic/homeostatic plasticity", „STP (Tsodyks-
Markram)", „LTP/LTD", „STDP", „NMDA as coincidence detector". Literatur: Gerstner et al.,
*Neuronal Dynamics*, Kap. 19 (Hebbian), Kap. 20 (STDP); Dayan & Abbott, Kap. 8.
:::

## 2 · Kurzzeitplastizität (STP) — Tsodyks-Markram-Modell

Synapsen ändern ihre Stärke abhängig von der **jüngsten Aktivität** (ms–s), **reversibel**.
Markram et al. (1998) zeigten: **dieselbe** Präsynapse kann je nach Zielzelle **Facilitation**
oder **Depression** zeigen.

**Modell über drei Transmitter-Pools** (Summe konstant = 1):

<p class="formula">R (recovered) + E (effective) + I (inactive) = 1</p>

- **Bei einem Spike** wird ein Anteil **U·R** der verfügbaren Ressourcen freigesetzt:
  R → E. Die effektive Größe **E** ist proportional zur synaptischen Leitfähigkeit / zum PSP.
- **E zerfällt** mit τ<sub>inact</sub> nach I; **I erholt sich** mit τ<sub>rec</sub> zurück
  nach R.
- **„Ground state"** nach langer Ruhe: (R, E, I) = (1, 0, 0).

**Depression:** Bei **hoher** Eingangsrate ist R zwischen den Spikes noch nicht erholt
(τ<sub>rec</sub> zu langsam) → jeder Spike setzt weniger frei → PSPs werden **kleiner**
(**short-term depression**). Funktion: Anpassung an die Eingangsrate (Gain-Control).

**Facilitation:** Ein **adaptiver** Freisetzungsparameter **U(t)** (Ca²⁺-abhängig, folgt
einer eigenen ODE 0 ≤ U ≤ 1) **steigt** mit jedem Spike → PSPs werden **größer**. Funktion:
Betonung von **Bursts / hochfrequenten** Eingängen.

## 3 · Langzeitplastizität: LTP & LTD

**Dauerhafte** Änderungen der synaptischen Stärke — das Substrat des Langzeitgedächtnisses
(klassisch am Hippocampus untersucht: Reiz-/Ableitelektrode am Schaffer-Kollateral).

**Rate-Experiment (Frequenzabhängigkeit):**
- **Hochfrequente** präsynaptische Stimulation (z. B. 100 Hz, 1 s) → **erhöhtes EPSP** →
  **Long-Term Potentiation (LTP)**.
- **Niederfrequente** Stimulation (z. B. 1 Hz, 900 s) → **verringertes EPSP** →
  **Long-Term Depression (LTD)**.
  (Postsynaptische Aktivität wird hier nicht kontrolliert.)

**Voltage-Clamp-Experiment (Spannungsabhängigkeit):** Klemmt man das postsynaptische
Potential fest, entscheidet die **Depolarisation**: **starke** Depolarisation → LTP,
**schwache** → LTD.

- **LTD ist nicht** einfach „negatives LTP": LTP und LTD werden (zumindest teilweise) über
  **verschiedene biochemische Signalwege** implementiert (O'Connor et al., 2005 — Trennung
  durch selektive Inhibitoren).

## 4 · Spike-Timing-Dependent Plasticity (STDP)

Mit Einzelzell-Messungen wurde die Abhängigkeit vom **relativen Timing** prä- und
postsynaptischer Spikes messbar (Bi & Poo, 1998; Markram et al.):

<p class="formula">Δt = t<sub>post</sub> − t<sub>pre</sub></p>

- **Kausal** (pre **vor** post, Δt &gt; 0) → **LTP** (Verstärkung).
- **Anti-kausal** (post **vor** pre, Δt &lt; 0) → **LTD** (Abschwächung).
- Der Effekt fällt mit **|Δt|** ab (typisches Fenster ~10–20 ms) → charakteristische
  **asymmetrische STDP-Kurve**.

Das ist die zeitlich präzisierte Fassung von **Hebbs Postulat** (1949): *„When an axon of
cell A … repeatedly or persistently takes part in firing cell B, … A's efficiency … is
increased"* — populär: **„Neurons that fire together, wire together"**, hier ergänzt um die
**Kausalität** (A muss B mitverursachen, nicht nur gleichzeitig feuern).

**Wichtig — STDP ist nicht universell:** Es gibt verschiedene Formen (klassisch
asymmetrisch, symmetrisch, invertiert), **Nichtlinearität** bei mehreren Spike-Paaren
(nicht einfach additiv), sowie Abhängigkeit von **Ort** (dendritische Position) und
**Frequenz**. Zu simple Modelle können ein falsches Bild erzeugen.

## 5 · Biophysik: NMDA-Rezeptor als Koinzidenzdetektor

Der **NMDA-Rezeptor (NMDAR)** ist der zentrale molekulare Mechanismus für LTP/LTD:

- steuert den **Ca²⁺-Einstrom** und wirkt als **Koinzidenzdetektor** von
  (1) **präsynaptischer** Glutamat-Freisetzung **und** (2) **postsynaptischer**
  Depolarisation (Spannungsabhängigkeit über den **Mg²⁺-Block**, L4).
- Die resultierende **[Ca²⁺]** entscheidet über die Richtung: **hohe** [Ca²⁺] → LTP
  (Einbau/Synthese neuer **AMPA-Rezeptoren**), **moderate** [Ca²⁺] → LTD.
- Die nötige postsynaptische Depolarisation kann durch **rückwärtslaufende
  Aktionspotentiale (back-propagating AP, bAP)** nach somatischem Feuern geliefert werden →
  verbindet STDP **mechanistisch** mit dem Spike-Timing (bAP kommt „nach" pre → Δt &gt; 0 →
  hohe [Ca²⁺] → LTP). Die bAP-Amplitude **nimmt mit dem Abstand vom Soma ab** (dendritische
  Position beeinflusst die Regel).
- **Präsynaptische LTD** kann über **retrograde Botenstoffe** (Endocannabinoide, von der
  Postsynapse freigesetzt, präsynaptisch über CB1-Rezeptoren detektiert) laufen →
  homosynaptische vs. heterosynaptische Anordnungen.

**Merksatz der Vorlesung (Warnung):** Reale Plastizität umfasst **viele parallele**
biochemische Pfade an jeder Synapse; vereinfachte Modelle sind nützlich, aber „gefährlich",
wenn man sie für die ganze Wahrheit hält.

<div class="keybox">
<strong>Kernbotschaften L10:</strong> Gedächtnis v. a. in Synapsen; dazu strukturelle &
homöostatische Plastizität. **STP (Tsodyks-Markram):** R+E+I=1, Depression (R nicht erholt,
hohe Rate) vs. Facilitation (adaptives U, Bursts). **LTP** (hohe Freq./starke Depol.) vs.
**LTD** (niedrige Freq./schwache Depol.) — verschiedene Signalwege. **STDP:** pre→post
(Δt&gt;0)=LTP, post→pre (Δt&lt;0)=LTD (Bi & Poo), zeitpräzisiertes Hebb, nicht universell.
**NMDAR** = Ca²⁺-Koinzidenzdetektor; [Ca²⁺] hoch→LTP, moderat→LTD; bAP liefert das
postsyn. Timing-Signal.
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 10.1** — Im Tsodyks-Markram-Modell gilt für die Pools …

A) R = E = I
B) E + I = 0
C) R + E = 1
D) R + E + I = 1
:::

::: mc
**MC 10.2** — Short-Term **Depression** entsteht, weil …

A) bei hoher Rate R zwischen den Spikes nicht vollständig regeneriert → PSPs schrumpfen.
B) der Freisetzungsparameter U mit jedem Spike steigt.
C) NMDA-Rezeptoren blockiert sind.
D) die Membranzeitkonstante steigt.
:::

::: mc
**MC 10.3** — Bei klassischer STDP führt „pre vor post" (Δt &gt; 0) zu …

A) LTD
B) Depression der Refraktärzeit
C) LTP
D) keiner Änderung
:::

::: mc
**MC 10.4** — Warum ist der NMDA-Rezeptor für LTP entscheidend?

A) Er ist die schnellste inhibitorische Synapse.
B) Er sitzt nur an elektrischen Synapsen.
C) Er ist spannungsunabhängig.
D) Er detektiert die Koinzidenz von präsyn. Glutamat und postsyn. Depolarisation und steuert den Ca²⁺-Einstrom.
:::

::: mc
**MC 10.5** — Welche Aussage zu LTP/LTD ist korrekt?

A) LTP und LTD laufen (zumindest teils) über verschiedene biochemische Pfade.
B) LTP entsteht nur bei niederfrequenter Stimulation.
C) Langzeitplastizität ist innerhalb von Millisekunden reversibel.
D) LTD ist exakt das negative LTP über denselben Signalweg.
:::

::: mc
**MC 10.6** — Short-Term **Facilitation** entsteht durch …

A) eine Erhöhung der Refraktärzeit.
B) Blockade der AMPA-Rezeptoren.
C) einen adaptiven, mit jedem Spike steigenden Freisetzungsparameter U(t) (Ca²⁺-abhängig).
D) das Erschöpfen des R-Pools.
:::

::: mc
**MC 10.7** — Im Rate-Experiment führt **hochfrequente** präsynaptische Stimulation
(z. B. 100 Hz) typischerweise zu …

A) keiner Änderung
B) LTD
C) Facilitation nur
D) LTP
:::

::: mc
**MC 10.8** — Welche Rolle spielt die **[Ca²⁺]**-Konzentration bei NMDAR-abhängiger
Plastizität?

A) sie ist irrelevant
B) hohe [Ca²⁺] → LTD, niedrige → LTP
C) hohe [Ca²⁺] → LTP, moderate [Ca²⁺] → LTD
D) sie bestimmt nur die Refraktärzeit
:::

::: mc
**MC 10.9** — Wodurch kann das postsynaptische Timing-Signal für STDP mechanistisch
geliefert werden?

A) durch die Myelinscheide
B) durch rückwärtslaufende Aktionspotentiale (bAP)
C) durch die Na⁺/K⁺-Pumpe
D) durch elektrische Synapsen
:::

::: mc
**MC 10.10** — Was besagt Hebbs Postulat (präzisiert durch STDP)?

A) Jede Verbindung wird mit der Zeit schwächer.
B) Wenn A wiederholt am Feuern von B kausal beteiligt ist, wird die Verbindung A→B verstärkt.
C) Nur inhibitorische Synapsen sind plastisch.
D) Neuronen, die gleichzeitig ruhen, verlieren ihre Verbindung.
:::

::: mc
**MC 10.11** — Welche Aussage über STDP ist korrekt?

A) STDP tritt nur bei elektrischen Synapsen auf.
B) STDP hat verschiedene Formen und ist nichtlinear/orts-/frequenzabhängig — nicht universell.
C) STDP kennt kein Zeitfenster.
D) STDP ist universell und immer gleich (asymmetrisch, additiv).
:::

## Freitext-Fragen (zum Besprechen)

1. Erkläre das Tsodyks-Markram-Modell (R/E/I, Freisetzung U·R, τ<sub>rec</sub>). Wie
   entstehen Depression bzw. Facilitation, und welche Rechenfunktion hat STP?
2. Vergleiche das Rate- und das Voltage-Clamp-Experiment zu LTP/LTD. Welche Größe ist
   jeweils die entscheidende (Frequenz vs. postsyn. Depolarisation)?
3. Skizziere die STDP-Kurve (Δt-Achse) und verknüpfe sie mit Hebbs Postulat. Warum betont
   STDP die Kausalität, nicht nur die Gleichzeitigkeit?
4. Warum ist STDP „nicht universell"? Nenne konkrete Abweichungen (Formen, Nichtlinearität,
   Ort, Frequenz).
5. Wie realisiert der NMDA-Rezeptor (Mg²⁺-Block, Ca²⁺, bAP) mechanistisch die Timing-Regel
   der STDP? Erkläre die Ca²⁺-Schwellen für LTP vs. LTD.
6. Grenze STP, LTP/LTD, strukturelle und homöostatische Plastizität nach Zeitskala und
   Funktion voneinander ab. Warum braucht ein lernendes Netz auch Homöostase?
7. Diskutiere die Warnung der Vorlesung: Wann sind vereinfachte Plastizitätsmodelle
   nützlich, wann irreführend?
