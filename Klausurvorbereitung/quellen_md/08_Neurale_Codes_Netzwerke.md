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

## 2 · Rate-basierte Netzwerkmodelle

Spikende Neuronen sind **rechenaufwändig** und **analytisch schwierig**. Man ersetzt sie
daher durch **firing-rate units**: **+** analytisch handhabbar, **−** verliert
spike-timing-Codes.

### 2.1 · Rate-based input integration (Herleitung)

Man ersetzt den präsynaptischen Spike-Train durch seinen Erwartungswert (die Rate
x<sub>i</sub>(τ)). Der synaptische Strom eines exponentiellen CUBA-Kernels wird dann zur
Faltung, deren Ableitung eine einfache **lineare DGL** ergibt:

<p class="formula">τ<sub>syn</sub> dI/dt = −I + τ<sub>syn</sub> <b>w</b>·<b>x</b> &nbsp;&nbsp;⟹&nbsp;&nbsp; Steady state: I = τ<sub>syn</sub> <b>w</b>·<b>x</b></p>

Der Strom folgt der gewichteten Eingangssumme **w**·**x** also wie ein **Tiefpass** mit
τ<sub>syn</sub>. w<sub>i</sub> > 0 = Erregung, w<sub>i</sub> < 0 = Hemmung.

### 2.2 · Rate-based response & Aktivierungsfunktionen

Bei konstantem Input läuft die Ausgangsrate gegen z → **F(w·x)**; bei zeitvariablem Input
folgt sie verzögert:

<p class="formula">τ dz/dt = −z + F( <b>w</b>·<b>x</b> )</p>

**F(I)** ist die **f-I-Kurve** (Rate über Input) — zugleich die **Aktivierungsfunktion**
künstlicher Netze. Gängige Formen: **Softplus** log(1+e<sup>I</sup>), **Sigmoid**
z<sub>max</sub>/(1+e<sup>−I</sup>), **ReLU** [I]<sub>+</sub> = max(0, I), **Exponentiell**
e<sup>I</sup>.

### 2.3 · Rekurrentes Netz (Populationsdynamik)

Allgemein koppeln Feed-Forward-Input (v<sub>ki</sub>x<sub>i</sub>), Rückkopplung
(w<sub>kj</sub>z<sub>j</sub>, Konvention w<sub>post,pre</sub>) und ein Bias b<sub>k</sub>:

<p class="formula">τ dz<sub>k</sub>/dt = −z<sub>k</sub> + F( Σ<sub>j</sub> w<sub>kj</sub> z<sub>j</sub> + Σ<sub>i</sub> v<sub>ki</sub> x<sub>i</sub> + b<sub>k</sub> )</p>

Das ist die Grundgleichung eines **rekurrenten neuronalen Netzes** und die **Brücke** zu
Perzeptron/Deep Learning (L11). Für w<sub>kj</sub> = 0 erhält man ein reines
**Feed-Forward-Netz**.

## 3 · Binäre Logik & Turing-Vollständigkeit (rate-based)

Mit **ReLU**-Units [V<sub>k</sub>+b<sub>k</sub>]<sub>+</sub> und binären Inputs
x<sub>i</sub> ∈ {L, H} (0 ≤ L < H) baut man stationäre Logik:

- **NOT(x):** ein **einzelnes** Neuron, Gewicht −1, Bias H+L → z = [−x + H + L]<sub>+</sub>
  liefert H für x=L und L für x=H.
- **NAND(x₁,x₂):** ein **zweistufiges** Netz — x₁,x₂ mit Gewicht +1 auf z₁ (Bias −(H+L)),
  dann z₁ mit Gewicht −1 auf z₂ (Bias H). Die **Nichtlinearität** von [·]<sub>+</sub> an z₁
  ist entscheidend (nur für H,H bleibt 2H−(H+L)=H−L > 0 übrig).

Warum das mächtig ist:

- **NAND ist funktional vollständig** — jede boolesche Funktion folgt aus NANDs, z. B.
  **NOT(x) = NAND(x, x)**; auch Addition und Multiplikation sind realisierbar.
- Daraus folgt: rate-basierte neuronale Netze können **jede CPU-Instruktion emulieren** →
  **Turing-vollständig**. „Rule-based" (regelbasiertes) Rechnen ist also **möglich**, aber
  **nicht** der natürliche/effiziente Betriebsmodus des Gehirns (das rechnet eher verteilt,
  plastisch, analog).

## 4 · Winner-Takes-All (WTA) — Einstieg

Konkurrierende Neuronen/Populationen, die über eine **gemeinsame Hemmung** konkurrieren:
Das am stärksten getriebene Neuron unterdrückt die anderen und „gewinnt". Das realisiert
**Selektion / Klassifikation** (die Ausgabe ist ein Place-Code: „welches Neuron gewinnt").
Dynamik, Phasenraum-Analyse und Stabilität folgen in **L9**.

<div class="keybox">
<strong>Kernbotschaften L8:</strong> Vier Codes: **Rate** (Tuning-Kurven, rezeptive
Felder/DoG, Kontrast), **Place** (Ortszellen), **Temporal** (Delay-Line + Koinzidenz,
µs-Präzision, Jeffress), **Phase** (rel. zu Oszillation). Rate-Modell: Input-Integration
τ<sub>syn</sub>İ = −I + τ<sub>syn</sub>**w**·**x**; Response τż = −z + F(**w**·**x**) mit
Aktivierungsfunktion F (Softplus/Sigmoid/ReLU/exp); rekurrent τż<sub>k</sub> = −z<sub>k</sub>
+ F(Σw<sub>kj</sub>z<sub>j</sub> + Σv<sub>ki</sub>x<sub>i</sub> + b<sub>k</sub>) = Brücke zu
Deep Learning. ReLU-Logik: NOT = 1 Unit, NAND = 2-stufiges Netz; NAND funktional vollständig
→ Netze **Turing-vollständig** (aber nicht der natürliche Modus). WTA = Konkurrenz über
gemeinsame Hemmung → Selektion (Details L9).
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
**MC 8.3** — Warum sind rate-basierte neuronale Netze prinzipiell Turing-vollständig?

A) Weil ein kleines Rate-Netz NAND realisiert und NAND funktional vollständig ist.
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

::: mc
**MC 8.11** — In der rate-basierten ReLU-Logik der Vorlesung gilt …

A) NOT braucht zwei Schichten, NAND nur eine.
B) NOT = ein einzelnes Neuron (Gewicht −1, Bias H+L); NAND = zweistufiges Netz (Nichtlinearität an z₁).
C) weder NOT noch NAND sind realisierbar.
D) NAND ist linear und braucht keine Aktivierungsfunktion.
:::

::: mc
**MC 8.12** — Die Populationsdynamik τ dz<sub>k</sub>/dt = −z<sub>k</sub> + F(Σ w<sub>kj</sub>z<sub>j</sub> + Σ v<sub>ki</sub>x<sub>i</sub> + b<sub>k</sub>) …

A) beschreibt ein rekurrentes Rate-Netz; F ist die Aktivierungsfunktion, b<sub>k</sub> der Bias.
B) gilt nur für einen einzelnen Spike.
C) ist die ISI-Verteilung.
D) enthält keine Rückkopplung.
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
