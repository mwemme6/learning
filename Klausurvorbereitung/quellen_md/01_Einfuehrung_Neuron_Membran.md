# 01 · Einführung: Gehirn vs. Computer, Neuron & Membran

<p class="sub">Brain-Inspired Computing · Vorlesung 1 · ausführliche Zusammenfassung</p>

## 1 · Motivation: Warum „brain-inspired"?

Das Gehirn löst Aufgaben, an denen klassische Computer lange scheiterten
(Mustererkennung, Assoziation, robustes Lernen), und verbraucht dabei nur **~20 W** —
weniger als eine Glühbirne. Umgekehrt ist exakte Arithmetik für einen Computer trivial,
fürs Gehirn aber mühsam. Ziel der Vorlesung ist ein Dreiklang: die **Rechenprinzipien
des Gehirns verstehen**, sie **mathematisch modellieren** und schließlich mit
**Mikroelektronik emulieren** (neuromorphe Technik, Höhepunkt: das Heidelberger
BrainScaleS-System, L11).

### 1.1 · Gehirn vs. klassischer Computer

| Eigenschaft | Gehirn | von-Neumann-Computer |
|-------------|--------|----------------------|
| Verarbeitung | massiv **parallel** (~10¹¹ Einheiten) | überwiegend **seriell** |
| Zeit | **kontinuierlich**, asynchron | zentraler **Takt**, synchron |
| Anpassung | **selbst-justierend** (Plastizität, Lernen) | extern **programmiert** |
| Architektur | Speicher & Rechnen **vermischt** (in-memory) | Speicher & CPU **getrennt** |
| Fehlertoleranz | **robust** (Redundanz, graceful degradation) | **fragil** (ein Bitfehler kann fatal sein) |
| Energie | ~20 W für 10¹¹ Neuronen | 10²–10⁶ W für vergleichbare Aufgaben |

Der entscheidende Architektur-Unterschied: Beim Computer sind **Prozessor und Speicher
getrennt** (von-Neumann-Architektur), Daten müssen ständig hin- und hergeschoben werden
(**von-Neumann-Flaschenhals**, s. L11). Im Gehirn ist das „Programm" (die Verschaltung
und die synaptischen Gewichte) **im Substrat selbst** gespeichert — Rechnen und Erinnern
passieren am selben Ort.

**Typische Aufgaben im Kontrast:** Der Computer glänzt bei „4711 × 0,815 = ?", Schleifen
und Array-Kopien. Das Gehirn glänzt bei „Erkenne die Stimmung aus einem Gesicht",
„Rufe eine alte Erinnerung aus einem kleinen Hinweis ab".

### 1.2 · Größenordnungen (auswendig fürs Namedropping)

| | menschliches Gehirn | simulierte kortikale Säule (Blue Brain) |
|---|---|---|
| Neuronen | ~10¹¹ | ~10⁴ |
| Synapsen | ~10¹⁵ | ~10⁷ |
| mittlere Rate | ~1 Hz | ~1 Hz (stark verlangsamt ggü. Biologie) |
| Leistung | ~20 W | ~10⁶ W |

Jedes Neuron ist mit **bis zu ~10 000** anderen verbunden. Die enorme Diskrepanz beim
Energieverbrauch (Gehirn 20 W vs. Simulation 10⁶ W) ist eine zentrale Motivation für
analoge neuromorphe Hardware.

::: ref
**Verweise:** Folie L1 „Comparison: Brain vs. Traditional Computer", „orders of
magnitude", „A glimpse at the Very Complex". Literatur: Gerstner et al., *Neuronal
Dynamics*, Kap. 1 (neuronaldynamics.epfl.ch); Mead, *Analog VLSI and Neural Systems*,
Kap. 1 (Motivation physikalisches Rechnen).
:::

## 2 · Ein kurzer Gang durch die Neurowissenschaft

Ein wenig Historie hilft, Modelle einzuordnen (und ist gern eine Einstiegsfrage):

- **Antonie van Leeuwenhoek / Robert Hooke** (17. Jh.): Entdeckung der Zelle.
- **Santiago Ramón y Cajal & Camillo Golgi** (Nobelpreis 1906): die **Neuron-Doktrin** —
  das Nervensystem besteht aus einzelnen, diskreten Zellen (Neuronen), nicht aus einem
  kontinuierlichen Netz.
- **Hodgkin & Huxley** (1952, NP 1963): erstes **vollständiges mechanistisches
  Neuronmodell** (L2).
- **Hubel & Wiesel** (1968, NP 1981): **Orientierungsselektivität** und Säulen-
  architektur im visuellen Cortex V1.
- **Neher & Sakmann** (1970er, NP 1991): **Patch-Clamp** — Messung der Leitfähigkeit
  **einzelner** Ionenkanäle.

Kernidee der Vorlesung: Es gibt **nicht eine** universelle mathematische Beschreibung
des Gehirns, sondern man **wechselt zwischen Abstraktionsebenen** — Biophysik →
vereinfachte Modelle → theoretische Analyse → Simulation → neuromorphe Hardware.

## 3 · Aufbau eines Neurons

Ein Neuron gliedert sich funktional in **Eingang**, **Integration** und **Ausgang**:

- **Dendriten** — empfangender Teil, sammeln synaptische Eingänge.
- **Soma (Zellkörper)** — integriert die Eingänge; hier wird über einen Spike entschieden.
- **Axon** — sendender Teil, leitet das Aktionspotential weiter; oft **> 1 m** lang.
- **Axonterminale** — bilden Synapsen zum nächsten Neuron.
- **Myelinscheide** (Schwann-Zellen) mit **Ranvier-Schnürringen** — beschleunigt die
  Leitung (saltatorisch, L4).

Wichtige Kennzahlen: hoher **Fan-in/Fan-out** (10⁴ bis >10⁵), komplexer interner Zustand,
der im **LIF-Modell** (L3) auf eine einzige Größe — die **Membranspannung des Somas** —
reduziert wird. Es gibt eine enorme morphologische Vielfalt von Neuronen (Pyramidenzellen,
Interneurone, …).

## 4 · Die Zellmembran & das Ruhepotential

Die ~5 nm dünne Lipidmembran trennt Innen von Außen und ist selektiv für bestimmte Ionen
durchlässig. Innen und außen herrschen **unterschiedliche Ionenkonzentrationen**. Das
Ruhepotential entsteht in **drei Schritten**:

1. **Pumpen** — die **Na⁺/K⁺-Pumpe** (Antiporter) schleust unter ATP-Verbrauch **3 Na⁺
   nach außen** und **2 K⁺ nach innen**. Sie ist der wichtigste aktive Transporter,
   verbraucht **~⅔ der Energie** des Neurons, ist **langsam** (diffusionsbegrenzt) und
   trägt **kaum direkt** zur Spannung bei — ihre Aufgabe ist, die **Konzentrations-
   differenz** aufzubauen und zu erhalten.
2. **Diffusion** — Ionen wandern entlang ihres Konzentrationsgefälles durch offene
   (Leck-)Kanäle → es entsteht eine **Ladungstrennung**.
3. **Elektrisches Feld** — die durch die Ladungstrennung entstehende Spannung wirkt der
   weiteren Diffusion **entgegen**. Im **dynamischen Gleichgewicht** definiert das das
   Ruhepotential U = E<sub>L</sub>.

### 4.1 · Gemessene Ionenkonzentrationen

| Ion | innen | außen | Umkehrpotential E<sub>X</sub> |
|-----|-------|-------|-------------------------------|
| Na⁺ | 10 mM | 140 mM | ≈ +50 mV |
| K⁺ | 145 mM | 4 mM | ≈ −90 mV |
| Cl⁻ | 5 mM | 110 mM | ≈ −65 mV |
| Ca²⁺ | 10⁻⁴ mM | 5 mM | stark positiv |

Zum Vergleich: Meerwasser [Na⁺] ≈ 470 mM, reines Wasser 55,5 mol/l.

### 4.2 · Umkehrpotential & Nernst-Gleichung

Für **einen einzelnen Ionentyp** X gibt die **Nernst-Gleichung** die Spannung an, bei der
Diffusions- und elektrische Kraft sich ausgleichen (Stromrichtung kehrt um):

<p class="formula">E<sub>X</sub> = (RT / zF) · ln( [X]<sub>außen</sub> / [X]<sub>innen</sub> )</p>

R = Gaskonstante, T = Temperatur, z = Ladungszahl, F = Faraday-Konstante. Es gilt:

- **u &lt; E<sub>X</sub>:** I &lt; 0 · **u &gt; E<sub>X</sub>:** I &gt; 0
- Der Strom durch einen Kanal ist **I<sub>X</sub> = g<sub>X</sub>(u − E<sub>X</sub>)**
  (ohmsch, mit Umkehrpotential E<sub>X</sub> als „Batterie").

### 4.3 · Ruhepotential bei mehreren Ionen: GHK

Sind **mehrere** Ionen mit unterschiedlichen **Permeabilitäten p<sub>X</sub>** beteiligt,
liefert die **Goldman-Hodgkin-Katz (GHK)-Gleichung** das effektive Ruhepotential:

<p class="formula">E<sub>L</sub> = (RT/F) · ln( (p<sub>K</sub>[K]<sub>a</sub> + p<sub>Na</sub>[Na]<sub>a</sub> + p<sub>Cl</sub>[Cl]<sub>i</sub>) / (p<sub>K</sub>[K]<sub>i</sub> + p<sub>Na</sub>[Na]<sub>i</sub> + p<sub>Cl</sub>[Cl]<sub>a</sub>) )</p>

Anschaulich: E<sub>L</sub> ist ein **permeabilitätsgewichteter Mittelwert** der einzelnen
Nernst-Potentiale. Im Ruhezustand dominiert die K⁺-Permeabilität → E<sub>L</sub> liegt
nahe E<sub>K</sub> (~−65 bis −70 mV). Steigt p<sub>K</sub>, wandert E<sub>L</sub> Richtung
E<sub>K</sub> (hyperpolarisiert); steigt p<sub>Na</sub> (wie beim AP, L2), wandert es
Richtung E<sub>Na</sub> (depolarisiert).

### 4.4 · Die Zelle als RC-Schaltkreis

Fasst man alle Leckströme zu einem effektiven Leitwert g<sub>L</sub> mit Batterie
E<sub>L</sub> zusammen, verhält sich die Membran wie ein **RC-Glied**: die Kapazität
C<sub>m</sub> (Ladungstrennung) parallel zum Leitwert g<sub>L</sub> = 1/R<sub>m</sub>.
Die passive Dynamik lautet:

<p class="formula">C<sub>m</sub> du/dt = −g<sub>L</sub>(u − E<sub>L</sub>) + I(t)</p>

Das ist ein **leaky integrator** bzw. **Tiefpassfilter erster Ordnung** mit der
**Membranzeitkonstante**

<p class="formula">τ<sub>m</sub> = C<sub>m</sub> / g<sub>L</sub> = R<sub>m</sub> · C<sub>m</sub></p>

Nach einem Strompuls relaxiert u exponentiell mit e<sup>−t/τ<sub>m</sub></sup> zurück zu
E<sub>L</sub>. Große τ<sub>m</sub> → träges, stark integrierendes Neuron; kleine τ<sub>m</sub>
→ schnelles, „koinzidenzsensitives" Neuron. Diese RC-Sicht ist die Grundlage von LIF (L3)
und der analogen Hardware (L11). **Grenze:** Das RC-Modell ist rein **passiv** — es kann
kein Aktionspotential erzeugen. Dafür braucht man spannungsabhängige Kanäle (L2).

::: ref
**Verweise:** Folie L1 „A simple model of the cell membrane", „resting potential",
„Na/K pump", „cell as an RC-circuit". Literatur: Dayan & Abbott, *Theoretical
Neuroscience*, Kap. 5.1–5.2 (Nernst, GHK, Membran); Gerstner & Kistler, *Spiking Neuron
Models*, Kap. 2.1; Gerstner et al., *Neuronal Dynamics*, Kap. 2.1.
:::

## 5 · Grobstruktur des Gehirns (Vokabular)

Graue Substanz (Zellkörper) vs. weiße Substanz (myelinisierte Axone); Gyrus (Windung),
Sulcus/Fissura (Furchen), Lobus (Lappen); Cortex (Großhirnrinde), Corpus callosum
(verbindet die Hemisphären). ~10¹¹ Neuronen, je bis ~10⁴ Verbindungen. Der **Homunculus**
zeigt die somatotope Karte; **Split-Brain-Experimente** (durchtrenntes Corpus callosum)
illustrieren die Lateralisierung der Funktionen.

<div class="keybox">
<strong>Kernbotschaften L1:</strong> (1) Gehirn = parallel, kontinuierlich, robust,
in-memory, energieeffizient (~20 W); Computer = seriell, getaktet, getrennt (von-Neumann).
(2) Ruhepotential entsteht aus Pumpe (Konzentrationsdifferenz, ATP) + Diffusion + E-Feld.
(3) Nernst = ein Ion; GHK = mehrere Ionen, permeabilitätsgewichtet. Kanalstrom
I<sub>X</sub>=g<sub>X</sub>(u−E<sub>X</sub>). (4) Membran ≈ RC-Tiefpass mit
τ<sub>m</sub>=C<sub>m</sub>/g<sub>L</sub> — passiv, daher (noch) kein Spike.
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 1.1** — Welche Aussage über das Gehirn (vs. klassischer Computer) ist **falsch**?

A) Speicher und Verarbeitung sind räumlich getrennt.
B) Es arbeitet massiv parallel.
C) Es ist robust gegen den Ausfall einzelner Elemente.
D) Es justiert sich selbst (Plastizität).
:::

::: mc
**MC 1.2** — Die Na⁺/K⁺-Pumpe …

A) transportiert netto Na⁺ in die Zelle hinein.
B) verbraucht keine Energie.
C) trägt direkt und maßgeblich über ihre Ladung zum Ruhepotential bei.
D) erzeugt die Konzentrationsdifferenz und verbraucht dafür ATP (~⅔ des Energiebudgets).
:::

::: mc
**MC 1.3** — Die Membranzeitkonstante τ<sub>m</sub> ist gegeben durch …

A) g<sub>L</sub> · C<sub>m</sub>
B) C<sub>m</sub> / g<sub>L</sub>
C) 1 / (R<sub>m</sub> C<sub>m</sub>)
D) g<sub>L</sub> / C<sub>m</sub>
:::

::: mc
**MC 1.4** — Wozu dient die GHK-Gleichung (im Gegensatz zur Nernst-Gleichung)?

A) Sie beschreibt das Umkehrpotential eines *einzelnen* Ions.
B) Sie berechnet die Ausbreitungsgeschwindigkeit des Aktionspotentials.
C) Sie kombiniert mehrere Ionen gewichtet nach ihren Permeabilitäten zu E<sub>L</sub>.
D) Sie beschreibt die Öffnungswahrscheinlichkeit der Gating-Variablen.
:::

::: mc
**MC 1.5** — Für einen Ionenkanal gilt I<sub>X</sub> = g<sub>X</sub>(u − E<sub>X</sub>).
Wenn u &lt; E<sub>X</sub> …

A) ist der Strom I<sub>X</sub> &gt; 0.
B) ist g<sub>X</sub> negativ.
C) fließt kein Strom.
D) ist der Strom I<sub>X</sub> &lt; 0.
:::

::: mc
**MC 1.6** — Warum kann das reine RC-Membranmodell **kein** Aktionspotential erzeugen?

A) Weil E<sub>L</sub> zu negativ ist.
B) Weil es passiv/linear ist und keine spannungsabhängigen (regenerativen) Leitwerte enthält.
C) Weil τ<sub>m</sub> zu groß ist.
D) Weil die Kapazität fehlt.
:::

::: mc
**MC 1.7** — Im Ruhezustand liegt E<sub>L</sub> nahe E<sub>K</sub> (≈ −70 mV), weil …

A) K⁺ im Ruhezustand die dominierende Permeabilität besitzt.
B) Na⁺ die höchste Permeabilität hat.
C) die Pumpe die Spannung direkt setzt.
D) Cl⁻ keine Rolle spielt.
:::

::: mc
**MC 1.8** — Ordne zu: Wer erhielt den Nobelpreis für die Untersuchung **einzelner
Ionenkanäle** (Patch-Clamp)?

A) Hubel & Wiesel
B) Neher & Sakmann
C) Ramón y Cajal & Golgi
D) Hodgkin & Huxley
:::

::: mc
**MC 1.9** — Ein Neuron mit **kleiner** Membranzeitkonstante τ<sub>m</sub> …

A) reagiert schnell und eignet sich als Koinzidenzdetektor.
B) kann keine Spikes erzeugen.
C) integriert Eingänge über lange Zeit und wirkt träge.
D) hat automatisch ein positiveres Ruhepotential.
:::

::: mc
**MC 1.10** — Welche Größenordnung stimmt für das menschliche Gehirn?

A) ~10¹⁵ Neuronen, ~10¹¹ Synapsen, ~2 W.
B) ~10⁶ Neuronen, ~10⁹ Synapsen, ~20 kW.
C) ~10¹¹ Neuronen, ~10¹⁵ Synapsen, ~20 W.
D) ~10⁸ Neuronen, ~10¹⁰ Synapsen, ~200 W.
:::

## Freitext-Fragen (zum Besprechen)

1. Erkläre in eigenen Worten, warum die Trennung von Speicher und Rechenwerk beim
   klassischen Computer zum „von-Neumann-Flaschenhals" führt — und wie das Gehirn ihn
   umgeht (Stichwort in-memory computing).
2. Leite qualitativ her, wie aus Pumpe, Diffusion und elektrischem Feld ein **stabiles**
   Ruhepotential entsteht. Warum ist es ein *dynamisches* Gleichgewicht?
3. Was passiert mit E<sub>L</sub>, wenn (a) die K⁺-Permeabilität steigt, (b) die
   Na⁺-Permeabilität steigt? Begründe mit der GHK-Intuition.
4. Erkläre das RC-Modell der Membran. Was bedeuten g<sub>L</sub>, C<sub>m</sub> und
   τ<sub>m</sub> physikalisch, und wie sieht die Antwort auf einen kurzen Strompuls aus?
5. Ordne Nernst-Gleichung, GHK-Gleichung und Ruhepotential zueinander ein. Wann brauchst
   du welche Beschreibung?
6. Warum ist der Energieverbrauch (20 W vs. 10⁶ W in der Simulation) ein so starkes
   Argument für **analoge** neuromorphe Hardware?
7. Diskutiere: Welche der fünf Gegensatzpaare (parallel/seriell, kontinuierlich/getaktet,
   selbstjustierend/programmiert, in-memory/getrennt, robust/fragil) hängen kausal
   zusammen?
8. Erkläre die Neuron-Doktrin (Cajal vs. Golgi) und warum sie für die gesamte
   Modellierung eine Voraussetzung ist.
