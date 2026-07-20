# 08 · Neuronale Codes & Feed-Forward-Netze

<p class="sub">Brain-Inspired Computing · Vorlesung 8 · ausführliche Zusammenfassung</p>

## 1 · Wie kodieren Neuronen Information?

Neuronen können Information auf mehrere Weisen tragen. Die **Codes koexistieren** und
schließen sich nicht aus. Man unterscheidet vier Grundtypen.

### 1.1 · Rate-Code
Information steckt in der **Feuerrate** (Spikes/s), gemittelt über ein Zeitfenster.
- Klassisches Beispiel: **Tuning-Kurven** — die Rate eines V1-Neurons als Funktion der
  Reizorientierung (Hubel & Wiesel, 1968): maximale Antwort bei der **bevorzugten
  Orientierung**, Abfall zu beiden Seiten.
- **Rezeptives Feld:** Region/Reizmuster, das ein Neuron „sieht". Retinale Ganglienzellen
  haben **On-Center/Off-Surround** (oder umgekehrt): Ein Lichtpunkt im Zentrum erregt
  (On-Center), im Umfeld hemmt er. Gut modelliert durch **Difference of Gaussians (DoG)**.
  Diffuse (Ganzfeld-)Beleuchtung erregt kaum, weil Zentrum und Umfeld sich aufheben →
  **Kontrast-/Kantendetektion**.
- **Nachteil:** niedrige zeitliche Auflösung — Mitteln braucht Zeit.

### 1.2 · Place-Code
Information steckt in **welches** Neuron feuert (Identität/Ort im Netz).
- Beispiel: **Ortszellen (place cells)** im Hippocampus (O'Keefe; Nobelpreis 2014, mit
  Moser & Moser für **grid cells**). Jede Zelle feuert an einem bestimmten Ort im Raum →
  eine zuverlässige, topografische **Karte**.

### 1.3 · Temporal-Code
Information in der **präzisen relativen Zeit** der Spikes → **sehr hohe** Auflösung.
- Beispiel: **Schallquellen-Lokalisation** über **Delay-Line + Koinzidenzdetektor**
  (Jeffress-Modell): interaurale Laufzeitdifferenzen werden im **µs-Bereich** ausgewertet
  (obwohl τ<sub>m</sub> ~ ms), Winkelauflösung ~1–2°.

### 1.4 · Phase-Code
Information **relativ zu einem oszillatorischen Referenzsignal** (z. B. Theta-Rhythmus).
- Beispiel: **Phase Precession** von Hippocampus-Ortszellen — der Feuerzeitpunkt relativ
  zur Theta-Oszillation kodiert die Position innerhalb des Feldes zusätzlich zur Rate.

::: ref
**Verweise:** Folie L8 „Rate/Place/Temporal/Phase code", „tuning curves", „receptive
fields (DoG)", „sound localization". Hubel & Wiesel 1968; Nobelpreis 2014. Literatur:
Dayan & Abbott, Kap. 1–2 (neural code, tuning, receptive fields); Gerstner et al.,
*Neuronal Dynamics*, Kap. 7 & 12.
:::

## 2 · Rate-basierte Antwortfunktion

Für konstanten Input mit Rate ν<sub>in</sub> ergibt sich eine stationäre Ausgangsrate über
eine **Antwort-/Aktivierungsfunktion F**:

<p class="formula">ν<sub>out</sub> = F( Σ<sub>j</sub> w<sub>j</sub> ν<sub>j</sub> )</p>

Bei zeitlich veränderlichem Input folgt der Ausgang F(t) **verzögert** (die Membran ist ein
Tiefpass mit Zeitkonstante τ, s. L9). Diese Gleichung ist die **Brücke** zwischen spike-
basierten Modellen und **abstrakten Raten-Netzen** (Perzeptron/Deep Learning, L11): w<sub>j</sub>
sind die synaptischen Gewichte, F entspricht der Aktivierungsfunktion (z. B. sigmoid, ReLU).

## 3 · Feed-Forward-Netze aus LIF-Neuronen

Ein LIF-Neuron mit exzitatorischen (COBA, L5) Synapsen bildet einen präsynaptischen
Spike-Train linear-gewichtet ab (Σ w<sub>j</sub> x<sub>j</sub>) und erzeugt bei
Schwellenüberschreitung Ausgabespikes. Mit passenden Gewichten und Schwellen lassen sich
so **logische Funktionen** realisieren — das Neuron wirkt als **Schwellenlogik-Gatter**.

## 4 · Turing-Vollständigkeit / Rule-based Computing

Ein einzelnes LIF-Neuron kann ein **NAND**-Gatter realisieren (z. B. über „leak over
threshold" mit geeigneter Gewichtung/Schwelle):

<p class="formula">NAND(a, b) = ¬(a ∧ b): feuert immer, außer wenn a UND b beide aktiv sind</p>

Warum das mächtig ist:
- **NAND ist ein universelles Gatter** — jede boolesche Funktion lässt sich allein aus
  NANDs aufbauen, z. B. **NOT(x) = NAND(x, x)**, **AND(a,b) = NOT(NAND(a,b))** usw.
- Mit Rückkopplung/Speicher folgt: **Neuronen-Netze sind Turing-vollständig** — im Prinzip
  so mächtig wie jede CPU. „Rule-based" (regelbasiertes) Rechnen mit Neuronen ist also
  **möglich** — aber es ist **nicht** der natürliche/effiziente Betriebsmodus des Gehirns
  (das nutzt eher verteilte, plastische, analoge Berechnung).

## 5 · Winner-Takes-All (WTA) — Einstieg

Konkurrierende Neuronen mit **lateraler Hemmung**: Das am stärksten getriebene Neuron
unterdrückt die anderen und „gewinnt". Das realisiert **Selektion / Klassifikation** (die
Ausgabe ist ein Place-Code: „welches Neuron gewinnt"). Dynamik, Phasenraum-Analyse und
Stabilität folgen in **L9**.

<div class="keybox">
<strong>Kernbotschaften L8:</strong> Vier Codes: **Rate** (Tuning-Kurven, rezeptive
Felder/DoG, Kontrast), **Place** (Ortszellen), **Temporal** (Delay-Line + Koinzidenz,
µs-Präzision), **Phase** (rel. zu Oszillation). Rate-Antwort ν<sub>out</sub> =
F(Σ w<sub>j</sub>ν<sub>j</sub>) = Brücke zu Perzeptron/Deep Learning. LIF realisiert NAND →
NAND universell → Netze **Turing-vollständig** (aber nicht der natürliche Modus). WTA =
laterale Hemmung → Selektion (Details L9).
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 8.1** — Welcher Code nutzt die **Identität** des feuernden Neurons?

A) Rate-Code
B) Place-Code
C) Temporal-Code
D) Phase-Code
:::

::: mc
**MC 8.2** — Rezeptive Felder retinaler Ganglienzellen (On-Center) werden gut beschrieben durch …

A) das Wiener-Chintschin-Theorem
B) eine reine Exponentialfunktion
C) eine einzelne Gaußkurve
D) Difference of Gaussians (DoG)
:::

::: mc
**MC 8.3** — Warum sind Netze aus LIF-Neuronen prinzipiell Turing-vollständig?

A) Weil ein LIF ein NAND realisieren kann und NAND ein universelles Gatter ist.
B) Weil sie kontinuierliche Zeit nutzen.
C) Weil sie eine Refraktärzeit besitzen.
D) Weil sie Poisson-Statistik haben.
:::

::: mc
**MC 8.4** — Die Schallquellen-Lokalisation über Delay-Line + Koinzidenzdetektor ist ein
Beispiel für …

A) Temporal-Code
B) Rate-Code
C) reine Ratenkodierung
D) Place-Code
:::

::: mc
**MC 8.5** — Die rate-basierte Antwortfunktion ν<sub>out</sub> = F(Σ w<sub>j</sub>ν<sub>j</sub>) …

A) gilt nur für einen einzelnen Spike.
B) ist unabhängig von den Gewichten.
C) verbindet Spike-Modelle mit abstrakten Raten-/Perzeptron-Netzen; F ist die Aktivierungsfunktion.
D) beschreibt die ISI-Verteilung.
:::

::: mc
**MC 8.6** — Wie realisiert man NOT(x) allein aus NAND?

A) NAND(x, 0)
B) NAND(x, 1)
C) gar nicht — dafür braucht man OR
D) NAND(x, x)
:::

::: mc
**MC 8.7** — Warum antwortet eine On-Center-Ganglienzelle kaum auf **diffuse**
(Ganzfeld-)Beleuchtung?

A) weil sie ein Phase-Code-Neuron ist.
B) weil die Refraktärzeit zu lang ist.
C) weil erregendes Zentrum und hemmendes Umfeld sich gegenseitig aufheben.
D) weil sie nur Farbe kodiert.
:::

::: mc
**MC 8.8** — Welcher Code hat die **höchste zeitliche Auflösung**?

A) Place-Code
B) alle gleich
C) Rate-Code
D) Temporal-Code
:::

::: mc
**MC 8.9** — Die **Phase Precession** von Ortszellen ist ein Beispiel für …

A) rein zufälliges Feuern
B) Place-Code
C) Phase-Code
D) Rate-Code
:::

::: mc
**MC 8.10** — Welche Aussage über regelbasiertes (rule-based) Rechnen mit Neuronen ist
korrekt?

A) Es benötigt zwingend elektrische Synapsen.
B) Es ist prinzipiell möglich (Turing-vollständig), aber nicht der natürliche/effiziente Modus des Gehirns.
C) Es ist unmöglich mit LIF-Neuronen.
D) Es funktioniert nur mit Hodgkin-Huxley-Neuronen.
:::

## Freitext-Fragen (zum Besprechen)

1. Stelle die vier Codes (Rate, Place, Temporal, Phase) mit je einem biologischen Beispiel
   gegenüber. Welcher hat die höchste zeitliche Auflösung und warum ist das trotz
   ms-Membranzeitkonstante möglich?
2. Erkläre das rezeptive Feld einer On-Center-Ganglienzelle und wie DoG es modelliert.
   Warum ist das ein Kanten-/Kontrastdetektor?
3. Zeige konstruktiv, wie man aus einem NAND-fähigen LIF-Neuron NOT, AND und OR aufbaut.
   Was folgt daraus für die Rechenmächtigkeit von Netzen?
4. Wie hängt die rate-basierte Antwortfunktion mit dem Perzeptron/Deep Learning (L11)
   zusammen? Worin unterscheidet sie sich vom spike-basierten Modell?
5. Erkläre das Jeffress-Modell (Delay-Line + Koinzidenz) für die Schall-Lokalisation.
   Wieso ist µs-Präzision trotz ms-τ<sub>m</sub> erreichbar?
6. Diskutiere: Warum ist Turing-Vollständigkeit ein interessantes, aber nur begrenzt
   nützliches Argument für das Verständnis des Gehirns?
