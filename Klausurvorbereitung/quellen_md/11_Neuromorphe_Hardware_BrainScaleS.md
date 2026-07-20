# 11 · Neuromorphes Rechnen & die BrainScaleS-Hardware

<p class="sub">Brain-Inspired Computing · Vorlesung 11 · ausführliche Zusammenfassung</p>

## 1 · Der von-Neumann-Flaschenhals

Klassische Computer folgen Turings Konzept der **universellen Maschine**; von Neumann
ersetzte das Band durch **Random-Access-Memory (RAM)**. Der Algorithmus wird **sequenziell**
durch Lesen/Schreiben im Speicher ausgeführt → **ständiger Datentransport** zwischen CPU und
Speicher = **von-Neumann-Flaschenhals**. Trotz **Moore'schem Gesetz** (Transistordichte
verdoppelt sich ~alle 2 Jahre; Beispiel Nvidia H100: ~8·10¹⁰ Transistoren, 4 nm, 350 W)
bleibt dieser Engpass die zentrale Grenze für datenintensive KI.

## 2 · In-Memory-Computing & der „neuromorphe Algorithmus"

**Neuromorphes Rechnen** überwindet den Flaschenhals durch **Aufheben der Trennung** von
Speicher und Rechenwerk:

- **In-Memory-Computing:** synaptische **Gewichte** liegen **lokal** am Rechenort
  (multiply-and-accumulate direkt an der Synapse); kein separater Speicherzugriff.
- **Neuronen** ersetzen die CPU als Recheneinheiten.
- **Kein Trennung von Algorithmus und Substrat** auf Netzwerkebene: **der Algorithmus ist
  im Substrat verkörpert** (embodied).

Ein **neuromorpher Algorithmus** legt fest: **(a)** die **Dynamik der Neuronen**, **(b)** die
**Netztopologie/Verbindungen**, **(c)** etwaige **Plastizitätsregeln**, die (a) und (b) im
Betrieb ändern.

## 3 · Zwei Klassen neuromorpher Algorithmen

| | **Deep Learning (KI)** | **Lokale Plastizität (Biologie)** |
|---|---|---|
| Modell | **Perzeptron** (Vektor-Matrix-Mult. + f) | **spike-basiert**, zeitkontinuierlich, rekurrent |
| Aktivierung | graded (≈ Feuerrate), z. B. ReLU | binärer **Spike**-Output, komplexe Nichtlinearität |
| Training | **Backpropagation / SGD** (Loss minimieren) | lokale, biologische Regeln (STDP, Homöostase) |
| Beispiel-HW | digitale Beschleuniger | HAGEN (2001), Spikey (2004), BrainScaleS |

Deep Neural Networks sind eine (einfache) Klasse neuromorpher Algorithmen: **SGD**
minimiert den **Loss** (Differenz „cat" vs. Netzausgabe „maybe a cat"); Gradienten via
**Backprop**. Für **spike-basierte** Netze existieren Gradientenschätzungen — **Surrogate
Gradients** und **Backprop-through-time** —, sodass auch sie trainierbar sind.

::: ref
**Verweise:** Folie L11 „von-Neumann bottleneck", „in-memory computing", „neuromorphic
algorithm", „Perceptron vs. spike-based", „Physical Model". Literatur: Mead, *Analog VLSI
and Neural Systems* (physikalisches Rechnen); Petrovici, *Form Versus Function*.
:::

## 4 · Physikalisches Rechnen: analoge neuromorphe Hardware

- **Numerisches Modell:** Parameter als **Binärzahlen** — Software-Simulation, digitale
  Beschleuniger, dedizierte Digitalschaltungen.
- **Physikalisches Modell (analog):** Parameter als **physikalische Größen** — **Spannung,
  Strom, Ladung**. Die Schaltung **ist** das Modell (die Physik „rechnet" die DGL selbst).

**Inhärente Geschwindigkeitslücke** (aus Brette/Gerstner 2005): biologische Membran ~10⁰ V/s,
VLSI ~10⁶ V/s → Faktor **~10⁶** → **beschleunigtes** Modell. Das erlaubt, langsame Prozesse
über **12–15 Größenordnungen** Zeitskala praktikabel zu emulieren:

| Prozess | Natur/Echtzeit | Simulation | beschl. Modell (×1000+) |
|---------|---------------|------------|-------------------------|
| Kausalitätsdetektion | 10⁻⁴ s | 0,1 s | 10⁻⁸ s |
| synaptische Plastizität | 1 s | 1000 s | 10⁻⁴ s |
| Lernen | Tag | 1000 Tage | 10 s |
| Entwicklung | Jahr | 1000 Jahre | 3000 s |

**Conductance-Based Integrate-and-Fire (Hardware-Gleichung):**

<p class="formula">C<sub>m</sub> dV/dt = g<sub>L</sub>(V−E<sub>L</sub>) + Σ<sub>k</sub> p<sub>k</sub>g<sub>k</sub>(V−E<sub>x</sub>) + Σ<sub>l</sub> p<sub>l</sub>g<sub>l</sub>(V−E<sub>i</sub>)</p>

→ direkt in eine **äquivalente Transistorschaltung** übersetzt (physical modeling).

## 5 · Das BrainScaleS-System (Heidelberg, Electronic Visions)

Ein **beschleunigtes physikalisches Modell**, optimiert für **Plastizitätsforschung**:

- **kontinuierliche Zeit**, **modularer** Aufbau, **AdEx**-Neuron (Adaptive Exponential I&F):

<p class="formula">C dV/dt = −g<sub>L</sub>(V−E<sub>L</sub>) + g<sub>L</sub>Δ<sub>T</sub> exp((V−V<sub>T</sub>)/Δ<sub>T</sub>) + I<sub>Syn</sub> − ω</p>
<p class="formula">τ<sub>ω</sub> dω/dt = a(V−E<sub>L</sub>) − ω</p>

- voller Satz **Ionenkanal-Schaltungen** je Kompartiment (**Na, Ca, NMDA**); komplexe
  Neuronen durch **Verbinden von Kompartimenten**; ~24 Kalibrationsparameter pro Kompartiment.
- **~1000× schneller** als Echtzeit; **65 nm** LP-CMOS; ~**10 pJ** pro synaptischem Event;
  **128k Synapsen**, **512** neuronale Kompartimente; **tile-basiert** (jede Tile kombiniert
  Analog- und Digitalteil, plus Prozessor + Vektoreinheit + Analogkern).
- **Synapse:** 6-bit-Gewicht + 6-bit-Adresse (SRAM), analoge **Korrelationsmessung**
  (kausal/anti-kausal) für STDP; bis zu **64 Membranschaltungen** kombinierbar zu einem Neuron.

## 6 · Neuromorphe Systeme weltweit (Vergleich)

| System | Art | Merkmale |
|--------|-----|----------|
| **TrueNorth** (IBM) | full-custom **digital** | **kein** lokales Lernen; ~Echtzeit; economy of scale |
| **Loihi** (Intel) | full-custom **digital**, 14 nm, 64 Kerne | **programmierbares** lokales Lernen; LIF (Schwelle ϑ, Reset 0 V); **nicht** Echtzeit (Kerne warten aufeinander) |
| **SpiNNaker** | **Many-core ARM** | jeder Kern löst ODEs für Neuronen; optimiertes Spike-Netzwerk; x0,01–1 Echtzeit |
| **BrainScaleS** | **analog** (physikalisch) | biologisch-lokales Lernen; **x1000–10 000 Echtzeit** |

Kernachsen: **analog vs. digital**, **Geschwindigkeit** (unter/über Echtzeit) und
**lokales Lernen** (ja/nein/programmierbar).

## 7 · Lernen auf dem Chip: Hybrid Plasticity

**Problem:** Millionen Parameter (Topologie, Neuronengrößen, Gewichte) müssen gesetzt werden.
Bisher: **Hardware-in-the-loop** mit externer Rechnerei (skaliert schlecht).
**Biologische Lösung:** **Lernen ersetzt Kalibrierung** — lokale Rückkopplungsschleifen
justieren die Parameter selbst.

**Hybrid Plasticity** kombiniert Analog + Digital:
- **analoge Korrelationsmessung in der Synapse** (kausal/anti-kausal) + paralleler **ADC**,
- digitale **Plasticity Processing Units (PPU, SIMD-CPU)**, die auf **Gewichte (ω)**,
  **Konfiguration/Adresse** (→ **strukturelle Plastizität**) und **Neuronspannungen/-raten**
  zugreifen.
- erlaubt **gleichzeitig**: strukturelle Optimierung, homöostatische Balance, Prä-Post-
  Korrelation (STDP) und weitere „third factors" (**Neuromodulatoren**).

**Beispiele/Demos:**
- Stabilisierung der Feuerraten via STDP (Stöckel, MA 2017; Beschleunigungsfaktor ~1000).
- **Reinforcement Learning „Pong"** komplett auf interner PPU (Wunderlich et al., 2019;
  ~0,4 ms Netzzeit/Iteration, ~23 µJ Gesamtenergie).
- **Strukturelle Plastizität**: 256 präsyn. Eingänge auf ein Dendrit, 32 aktive Synapsen;
  Regel kombiniert STDP-, homöostatische und strukturelle Terme (Cramer & Billaudelle, 2021).

## 8 · Weitere Ergebnisse

- **Surrogate-Gradient-Training** mehrschichtiger Netze auf BrainScaleS.
- **Spike-Latency-Coding** für schnelle Inferenz: **97,6 %** Testgenauigkeit, **85k
  Bilder/s**, **2,4 µJ/Bild**, **8 µs** Latenz.

<div class="keybox">
<strong>Kernbotschaften L11:</strong> von-Neumann-Flaschenhals → **In-Memory-Computing**
(Gewichte lokal, Algorithmus im Substrat verkörpert). Zwei Algorithmus-Klassen: **Deep
Learning** (Backprop/SGD) vs. **lokale Plastizität** (STDP, Homöostase). **Physikalisches
(analoges) Modell:** Parameter = Spannung/Strom/Ladung, ~10⁶ schneller → BrainScaleS
(**AdEx**, ~1000× Echtzeit, 65 nm, 128k Synapsen, Na/Ca/NMDA-Kanäle). Systeme:
TrueNorth/Loihi/SpiNNaker (digital) vs. **BrainScaleS** (analog). **Hybrid Plasticity:**
analoge Korrelationsmessung + digitale PPU → „Lernen ersetzt Kalibrieren"; Surrogate
Gradients & Spike-Latency-Coding für effiziente Inferenz.
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 11.1** — Der von-Neumann-Flaschenhals bezeichnet …

A) den Engpass durch ständigen Datentransport zwischen getrenntem Speicher und CPU.
B) die Kalibrierung analoger Synapsen.
C) die Refraktärzeit digitaler Neuronen.
D) die begrenzte Transistordichte nach Moore.
:::

::: mc
**MC 11.2** — Was kennzeichnet ein **physikalisches** (analoges) neuromorphes Modell?

A) Parameter als Binärzahlen im RAM.
B) Verzicht auf jegliche digitale Steuerung.
C) Modellgrößen als physikalische Größen (Spannung, Strom, Ladung); die Schaltung ist das Modell.
D) rein sequenzielle Ausführung.
:::

::: mc
**MC 11.3** — Welches Neuronmodell setzt BrainScaleS um?

A) FitzHugh-Nagumo
B) Adaptive Exponential Integrate-and-Fire (AdEx)
C) Hodgkin-Huxley (5 ODEs)
D) reines LIF
:::

::: mc
**MC 11.4** — Worin unterscheidet sich BrainScaleS grundlegend von Loihi/TrueNorth?

A) TrueNorth arbeitet analog.
B) BrainScaleS ist rein digital.
C) BrainScaleS ist **analog** und stark **beschleunigt** (~1000–10 000× Echtzeit); die anderen sind digital (≈/unter Echtzeit).
D) Loihi hat keine Neuronen.
:::

::: mc
**MC 11.5** — „Hybrid Plasticity" auf BrainScaleS bedeutet …

A) analoge Korrelationsmessung in der Synapse + digitale Plasticity Processing Units, die Gewichte/Struktur/Raten anpassen.
B) Training ausschließlich extern per Backprop.
C) Verzicht auf strukturelle Plastizität.
D) rein analoges Lernen ohne Digitalteil.
:::

::: mc
**MC 11.6** — Die beiden Hauptklassen neuromorpher Algorithmen sind …

A) LIF vs. HH
B) analog vs. digital
C) COBA vs. CUBA
D) Deep Learning (Backprop) vs. lokale Plastizität (Biologie)
:::

::: mc
**MC 11.7** — „In-Memory-Computing" heißt …

A) alle Daten im Cache halten.
B) synaptische Gewichte liegen lokal am Rechenort (multiply-and-accumulate an der Synapse), keine Trennung Speicher/Compute.
C) Neuronen durch eine zentrale CPU ersetzen, die sequentiell rechnet.
D) mehr RAM verbauen.
:::

::: mc
**MC 11.8** — Woher kommt die ~10⁶-fache **Beschleunigung** analoger Hardware ggü. Biologie?

A) aus höherer Taktfrequenz einer CPU.
B) aus dem Verzicht auf Synapsen.
C) aus paralleler Software-Simulation.
D) aus der viel höheren „Spannungsänderungsrate" (V/s) kleiner VLSI-Bauelemente ggü. der biologischen Membran.
:::

::: mc
**MC 11.9** — Wie werden **spike-basierte** Netze trainierbar gemacht?

A) durch Erhöhen der Refraktärzeit.
B) gar nicht — Spikes sind nicht differenzierbar.
C) mit Surrogate Gradients / Backprop-through-time.
D) nur mit elektrischen Synapsen.
:::

::: mc
**MC 11.10** — Welche Aussage über Intel **Loihi** stimmt?

A) Es ist ~10 000× schneller als Echtzeit.
B) Es bietet kein lokales Lernen (wie TrueNorth).
C) Es ist digital, nutzt LIF-Neuronen und bietet programmierbares lokales Lernen, läuft aber nicht in Echtzeit.
D) Es ist ein analoges System ohne Digitalteil.
:::

::: mc
**MC 11.11** — „Lernen ersetzt Kalibrierung" auf BrainScaleS bedeutet …

A) es findet gar kein Lernen statt.
B) Kalibrierung erfolgt nur durch Backprop auf einem Supercomputer.
C) lokale Plastizitätsregeln justieren die Millionen Parameter selbst, statt sie extern zu kalibrieren.
D) man muss jede Synapse manuell kalibrieren.
:::

::: mc
**MC 11.12** — Wozu dient die **PPU** (Plasticity Processing Unit)?

A) als Ersatz für die Synapsen.
B) zur analogen Erzeugung der Membranspannung.
C) zur Kühlung des Chips.
D) als digitale SIMD-Einheit, die Gewichte, Konfiguration (Struktur) und Neuronraten liest und Plastizitätsregeln ausführt.
:::

## Freitext-Fragen (zum Besprechen)

1. Erkläre den von-Neumann-Flaschenhals und wie In-Memory-Computing ihn überwindet. Was
   heißt „der Algorithmus ist im Substrat verkörpert"?
2. Vergleiche die zwei Algorithmus-Klassen (Deep Learning vs. lokale Plastizität) und
   erkläre, wie spike-basierte Netze dennoch mit Gradienten trainiert werden.
3. Was bedeutet „beschleunigtes physikalisches Modell"? Begründe den Faktor ~10⁶ (V/s-Lücke)
   und wozu die Beschleunigung nützt (Zeitskalen von Plastizität, Lernen, Entwicklung).
4. Vergleiche BrainScaleS, Loihi, TrueNorth und SpiNNaker entlang der Achsen analog/digital,
   Geschwindigkeit und lokales Lernen.
5. Beschreibe Hybrid Plasticity und warum „Lernen die Kalibrierung ersetzt". Welche Rolle
   spielt die PPU, und welche Terme (STDP, homöostatisch, strukturell) kombiniert die Regel?
6. Ordne die AdEx-Gleichungen ein: Welcher Term erzeugt den Spike-Anlauf, welcher die
   Adaptation? Wie hängt das mit L3 (2D-Modelle) zusammen?
7. Verknüpfe L11 mit dem Rest der Vorlesung: Wo tauchen COBA (L5), AdEx (L3), STDP (L10)
   und WTA (L9) in der Hardware wieder auf?
