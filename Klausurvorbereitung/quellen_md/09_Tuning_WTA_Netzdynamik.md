# 09 · Tuning-Kurven, Netzdynamik & Winner-Takes-All

<p class="sub">Brain-Inspired Computing · Vorlesung 9 · ausführliche Zusammenfassung</p>

## 1 · Tuning-Kurven: das Neuron als Template-Matcher

Ein rate-basiertes Neuron z<sub>k</sub> erhält den Input **x** = (x<sub>1</sub>, …, x<sub>N</sub>)
über die Gewichte **V**<sub>k</sub> = (V<sub>k1</sub>, …, V<sub>kN</sub>). Für **statischen**
Input strebt es gegen

<p class="formula">z<sub>k</sub> → F( <b>V</b><sub>k</sub> · <b>x</b> )   (t → ∞)</p>

**Frage:** Auf welchen Stimulus **x**\* reagiert das Neuron am stärksten? Weil F(·) streng
monoton steigt, maximiert man einfach das Skalarprodukt:

<p class="formula"><b>x</b>* = argmax<sub>x</sub> <b>V</b><sub>k</sub>·<b>x</b>
= argmax<sub>x</sub> ‖<b>x</b>‖ ‖<b>V</b><sub>k</sub>‖ cos∠(<b>V</b><sub>k</sub>,<b>x</b>)</p>

Bei **fester Reizstärke** (‖**x**‖ = const) ist das Skalarprodukt maximal, wenn der Input
**parallel** zum Gewichtsvektor liegt:

<p class="formula"><b>x</b>* ∥ <b>V</b><sub>k</sub></p>

Man liest **V**<sub>k</sub> daher als **räumlichen Kernel** bzw. **bevorzugtes
Eingangsmuster**: „Neuron k ist auf das Muster **x** ∥ **V**<sub>k</sub> getunt." Die
Tuning-Kurve ist damit nichts anderes als **Template-Matching per Skalarprodukt** — sie
misst, wie gut der Input zum gespeicherten Muster passt.

::: ref
**Verweise:** Folie L9 „tuning curve", „temporal dynamics / low-pass filter /
Green's function", „competing excitatory populations", „phase plane analysis",
„Winner-Take-All", „multiple WTA populations". Literatur: Dayan & Abbott, Kap. 7
(network/firing-rate models); Gerstner et al., *Neuronal Dynamics*, Kap. 15–16 (rate
models, competition, attractors).
:::

## 2 · Zeitliche Dynamik in Feed-forward-Netzen

Für **Feed-forward-Netze** (keine Rückkopplungsschleifen) ist die Dynamik einfach: Jedes
Neuron ist ein **Tiefpassfilter** seines Inputs V<sub>k</sub>(t):

<p class="formula">( ∂<sub>t</sub> + 1/τ<sub>k</sub> ) z<sub>k</sub>
= (1/τ<sub>k</sub>) · F( V<sub>k</sub>(t) + b<sub>k</sub> ) =: f<sub>k</sub>(t)</p>

Die Aktivität pflanzt sich Schicht für Schicht fort; formal über die **Green'sche Funktion**
(Impulsantwort) G(t) = Θ(t) e<sup>−t/τ<sub>k</sub></sup>:

<p class="formula">z<sub>k</sub>(t) = ∫ G(t−t′) f<sub>k</sub>(t′) dt′</p>

Ein Puls wird also in jeder Schicht per Tiefpass **geglättet**. Schaltet man **zwei**
Exponential-Filter hintereinander (x →<sup>V</sup> z<sub>1</sub> →<sup>W</sup> z<sub>2</sub>),
ergibt sich — wie schon bei den synaptischen Kerneln (L5) — eine **Difference of
Exponentials**. Kleine τ → schnelle, „koinzidenzsensitive" Reaktion; große τ → träges
Mitteln.

## 3 · Konkurrierende exzitatorische Populationen (WTA)

Das eigentliche WTA-Motiv der Vorlesung besteht aus **zwei exzitatorischen Populationen**
z<sub>1</sub>, z<sub>2</sub>, die je eine **Selbsterregung** w<sub>ee</sub> haben und eine
**gemeinsame inhibitorische Population** treiben. Diese misst die **kombinierte** Aktivität
und gibt (praktisch instantan) eine effektive **direkte Hemmung** w<sub>ei</sub> = 1/a
zurück. Mit τ = 200 ms:

<p class="formula">τ dz<sub>k</sub>/dt = −z<sub>k</sub> + F( w<sub>ee</sub> z<sub>k</sub>
+ w<sub>ei</sub> · F(z<sub>1</sub>+z<sub>2</sub>) + V<sub>k</sub> ),   k = 1, 2</p>
<p class="formula">F(z) = exp( a (z + b) )</p>

Wichtig: Die Konkurrenz läuft **nicht** über direkte gegenseitige Hemmung, sondern über eine
**geteilte Inhibition** (shared inhibition), die beide Populationen gemeinsam dämpft.

### 3.1 · Phasenraum-Analyse (Nullklinen & Fixpunkte)

Man analysiert das System in der Phasenebene (z<sub>1</sub>, z<sub>2</sub>): Die **Nullklinen**
(dz<sub>1</sub>/dt = 0 und dz<sub>2</sub>/dt = 0) und ihre **Schnittpunkte = Fixpunkte**
bestimmen das Verhalten. Je nach Input ergeben sich drei Regime:

| Input | Fixpunkt-Struktur & Verhalten |
|-------|-------------------------------|
| **V<sub>1</sub> = V<sub>2</sub> = 4** (schwach) | **Drei stabile Fixpunkte**. FP1 (symmetrisch, ~ (3,3)): beide Populationen feuern moderat und **koexistieren**. FP2/FP3 (Ecken): eine Population unterdrückt die andere. Welcher Fixpunkt erreicht wird, hängt vom **Startzustand** ab. |
| **\|V<sub>1</sub> − V<sub>2</sub>\| > δ** (asymmetrisch) | Nur **ein** stabiler Fixpunkt → der **stärker getriebene** Kanal gewinnt fast die gesamte Aktivität. Das Netz **selektiert** zuverlässig den größten Input. |
| **V<sub>1</sub> = V<sub>2</sub> ≳ 4,7** (stark, symmetrisch) | **Saddle-node-Bifurkation**: symmetrischer Fixpunkt und Sattelpunkt verschmelzen → schon kleinste Anfangsunterschiede entscheiden über den Gewinner. |

### 3.2 · Winner-Takes-All & kritische Verlangsamung

Sobald Start- oder Eingangszustand **unsymmetrisch** ist, zieht das System in eine
**Gewinner-Ecke**: die stärkere Population übernimmt fast die ganze Aktivität, die schwächere
wird nahezu ausgeschaltet — **„Winner takes all"**.

Nahe der **Saddle-node-Bifurkation** (V ≳ 4,7) zeigt das System **kritische Verlangsamung
(critical slowing down)**: Es „klebt" lange im labilen symmetrischen Zustand (z<sub>1</sub> ≈
z<sub>2</sub> ≈ 4), bevor es **abrupt** umschaltet (ein Kanal springt hoch, der andere fällt
auf ~ 0). So wirkt das WTA-Netz nahe der Bifurkation als **sensibler Entscheider** mit
variabler, teils langer Reaktionszeit — ein Modell z. B. für wahrnehmungsbezogene
Entscheidungen.

## 4 · Input-Integration mit mehreren WTA-Populationen

Erweitert man auf **viele** konkurrierende Populationen z<sub>k</sub>, jede auf ein anderes
Muster getunt (V<sub>k</sub> = Σ<sub>i</sub> V<sub>ki</sub> x<sub>i</sub>), die alle denselben
Input **x** sehen, steht die Frage: **„Wer passt am besten?"** Aus Tuning (§1) + WTA-Konkurrenz
(§3) entsteht ein **Klassifikator** mit zwei Eigenschaften:

- **Zuverlässige Detektion** des Inputs durch Konkurrenz.
- **Eindeutiger Output-Code**: der Gewinner nimmt fast die gesamte Aktivität → Place-Code.

Jede Population misst per **Skalarprodukt**, wie gut der Input zu ihrem Muster passt; die
Konkurrenz wählt den besten Treffer. Das ist die Grundidee vieler neuronaler
Erkennungssysteme.

<div class="keybox">
<strong>Kernbotschaften L9:</strong> Tuning = Template-Matching: z<sub>k</sub> = F(<b>V</b><sub>k</sub>·<b>x</b>),
maximale Antwort für <b>x</b> ∥ <b>V</b><sub>k</sub>. Feed-forward-Neuron = Tiefpass,
Green-Funktion G(t)=Θ(t)e<sup>−t/τ</sup>; zwei Filter hintereinander → Difference of
Exponentials. WTA-Modell: zwei exzitatorische Populationen (Selbsterregung w<sub>ee</sub>) +
<b>gemeinsame</b> Inhibition w<sub>ei</sub>=1/a, F(z)=exp(a(z+b)), τ=200 ms. Phasenraum:
schwacher Input (V=4) → <b>drei</b> stabile Fixpunkte (symmetrisch + zwei Gewinner);
asymmetrischer Input → <b>ein</b> Fixpunkt (stärkerer gewinnt); V≳4,7 → Saddle-node-Bifurkation
mit <b>kritischer Verlangsamung</b>. Viele WTA-Populationen + Tuning = Klassifikator
(zuverlässige Detektion + eindeutiger Place-Code).
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 9.1** — Ein Neuron z<sub>k</sub> = F(**V**<sub>k</sub>·**x**) reagiert bei fester
Reizstärke ‖**x**‖ maximal, wenn der Input …

A) orthogonal zum Gewichtsvektor V<sub>k</sub> steht
B) parallel zum Gewichtsvektor V<sub>k</sub> liegt
C) minimale Norm hat
D) rein zufälliges Rauschen ist
:::

::: mc
**MC 9.2** — Wie ist der Gewichtsvektor **V**<sub>k</sub> zu interpretieren?

A) als Refraktärzeit des Neurons
B) als Poisson-Rate des Inputs
C) als bevorzugtes Eingangsmuster / räumlicher Kernel (Template-Matching)
D) als Membranzeitkonstante
:::

::: mc
**MC 9.3** — In einem Feed-forward-Netz wirkt jedes Neuron auf seinen Input als …

A) reiner Hochpass
B) idealer Integrator ohne Leck
C) Tiefpass mit Green-Funktion G(t) = Θ(t) e<sup>−t/τ</sup>
D) NAND-Gatter
:::

::: mc
**MC 9.4** — Schaltet man zwei exponentielle Tiefpassfilter hintereinander, ergibt sich als
Impulsantwort …

A) eine Sinusschwingung
B) eine lineare Rampe
C) ein reiner Dirac-Impuls
D) eine Difference of Exponentials
:::

::: mc
**MC 9.5** — Wodurch konkurrieren die beiden exzitatorischen Populationen im WTA-Modell der
Vorlesung?

A) über eine gemeinsame inhibitorische Population (geteilte Hemmung)
B) über elektrische Synapsen (Gap Junctions)
C) über direkte gegenseitige Erregung
D) gar nicht — sie sind unabhängig
:::

::: mc
**MC 9.6** — Bei **schwachem, symmetrischem** Input (V<sub>1</sub> = V<sub>2</sub> = 4) hat
das WTA-System …

A) gar keinen Fixpunkt
B) genau einen instabilen Grenzzyklus
C) drei stabile Fixpunkte (ein symmetrischer + zwei Gewinner-Fixpunkte)
D) exakt zwei Fixpunkte und sonst nichts
:::

::: mc
**MC 9.7** — Bei **asymmetrischem** Input (\|V<sub>1</sub> − V<sub>2</sub>\| > δ) …

A) feuern beide Populationen exakt gleich stark
B) gibt es einen stabilen Fixpunkt — der stärker getriebene Kanal gewinnt
C) verschwindet jede Aktivität
D) entsteht eine Poisson-Statistik
:::

::: mc
**MC 9.8** — Was passiert bei V<sub>1</sub> = V<sub>2</sub> ≳ 4,7?

A) das System wird rein linear
B) Saddle-node-Bifurkation — kleinste Anfangsunterschiede entscheiden den Gewinner
C) alle Fixpunkte werden instabil und die Aktivität explodiert
D) die Zeitkonstante τ wird negativ
:::

::: mc
**MC 9.9** — „Kritische Verlangsamung" (critical slowing down) nahe der Bifurkation bedeutet …

A) das Neuron feuert gar nicht mehr
B) die Membranzeitkonstante sinkt auf 0
C) globale Synchronisation aller Neuronen
D) das System verharrt lange im labilen symmetrischen Zustand und schaltet dann abrupt um
:::

::: mc
**MC 9.10** — Kombiniert man Tuning mit mehreren konkurrierenden WTA-Populationen, entsteht …

A) ein reines Feed-forward-Signal ohne Funktion
B) ausschließlich Poisson-Rauschen
C) ein Klassifikator: zuverlässige Detektion + eindeutiger Output-Code (Gewinner nimmt fast alle Aktivität)
D) ein idealer linearer Mittelwertbildner
:::

## Freitext-Fragen (zum Besprechen)

1. Zeige, dass ein Neuron z<sub>k</sub> = F(**V**<sub>k</sub>·**x**) bei fester Reizstärke
   maximal auf **x** ∥ **V**<sub>k</sub> antwortet. Wieso ist die Tuning-Kurve ein
   Template-Matching, und was bedeutet **V**<sub>k</sub> anschaulich?
2. Erkläre die zeitliche Dynamik in Feed-forward-Netzen: Warum ist jedes Neuron ein Tiefpass,
   was ist die Green'sche Funktion, und warum ergeben zwei kaskadierte Filter eine Difference
   of Exponentials?
3. Beschreibe das WTA-Modell der Vorlesung (zwei exzitatorische Populationen mit
   Selbsterregung, gemeinsame Inhibition, F(z) = exp(a(z+b))). Wie liefert die
   Nullklinen-/Phasenraum-Analyse die Fixpunkte?
4. Vergleiche die drei Input-Regime (schwach-symmetrisch, asymmetrisch, V ≳ 4,7) hinsichtlich
   Zahl und Art der Fixpunkte und des resultierenden Verhaltens.
5. Was ist eine Saddle-node-Bifurkation, und was bedeutet „kritische Verlangsamung"? Warum
   wirkt das WTA-Netz nahe der Bifurkation als sensibler Entscheider mit variabler
   Reaktionszeit?
6. Wie entsteht aus Tuning (§1) und mehreren konkurrierenden WTA-Populationen ein
   Klassifikator? Welche zwei Eigenschaften machen ihn nützlich?
