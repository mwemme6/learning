# 03 · Leaky Integrate-and-Fire & 2D-Neuronmodelle

<p class="sub">Brain-Inspired Computing · Vorlesung 3 · ausführliche Zusammenfassung</p>

## 1 · Die Idee der Vereinfachung

Das HH-Modell (L2) ist realistisch, aber mit 5 gekoppelten ODEs schwer analysierbar und
langsam zu simulieren. Betrachtet man ein Neuron bei realistischem Input I(t), erkennt man
**zwei Betriebsmodi**:

- **unterschwellige Integration** — die Gating-Variablen bleiben näherungsweise **konstant**,
  die Membran verhält sich passiv (RC).
- **Aktionspotentiale** — die Gating-Variablen durchlaufen **stereotype** Trajektorien;
  der Spike sieht (fast) immer gleich aus.

**Schlüsselidee:** Wenn der Spike stereotyp ist, muss man ihn nicht im Detail rechnen. Man
modelliert nur die **unterschwellige Dynamik** explizit und ersetzt den Spike durch einen
**Schwellwert-plus-Reset-Mechanismus**.

## 2 · Das Leaky Integrate-and-Fire-Modell (LIF)

Unterschwellig ist das LIF ein reines **RC-Glied** (wie L1):

<p class="formula">C du/dt = −g<sub>L</sub>(u − E<sub>L</sub>) + I(t)</p>

Dazu kommt die **Feuer-und-Reset-Regel:** Erreicht u die **Schwelle ϑ**, wird
- ein **Spike** zum Zeitpunkt t<sup>(f)</sup> ausgegeben,
- u instantan auf das **Reset-Potential E<sub>r</sub>** gesetzt (oft E<sub>r</sub> = E<sub>L</sub>),
- u für die **absolute Refraktärzeit τ<sub>ref</sub>** dort festgehalten.

### 2.1 · Eigenschaften des LIF (Prüfungsliste)

- **Membranzeitkonstante** τ<sub>m</sub> = C / g<sub>L</sub> (bestimmt Integrationsfenster).
- **Reset-Potential** E<sub>r</sub> (häufig = E<sub>L</sub>).
- **absolute Refraktärzeit** τ<sub>ref</sub> → **keine relative** Refraktärzeit.
- fest definierte, **wohldefinierte Schwelle ϑ** (im Gegensatz zu HH!).
- Ausgang ist ein **Spike-Train** {t<sup>(f)</sup>}, der **nicht** Teil der
  Membranspannung ist. **Ein- und Ausgang sind elektrisch getrennt** → die Information
  fließt **immer von der Membran zum Spike**, nie zurück. Der Spike ist eine reine
  Ereignismarke, keine modellierte Spannungsform.

### 2.2 · Herleitung der Antwort auf konstanten Strom

Für konstanten I und E<sub>r</sub> = E<sub>L</sub> löst man die lineare ODE. Die Spannung
steigt exponentiell Richtung Gleichgewicht u<sub>∞</sub> = E<sub>L</sub> + I/g<sub>L</sub>.
Erreicht u<sub>∞</sub> die Schwelle nicht (I zu klein), feuert das Neuron **nie**. Sonst
ergibt sich das Interspike-Intervall aus der Zeit T, bis u von E<sub>r</sub> auf ϑ steigt:

<p class="formula">T = τ<sub>m</sub> · ln[ (I/g<sub>L</sub> + E<sub>L</sub> − E<sub>r</sub>) / (I/g<sub>L</sub> + E<sub>L</sub> − ϑ) ]</p>

Die **Feuerrate** ist ν = 1/(T + τ<sub>ref</sub>).

## 3 · Aktivierungsfunktion (f-I-Kurve) des LIF

Aus obiger Rate folgt die **Aktivierungsfunktion** ν(I):

- unterhalb eines **Schwellstroms** (I·R<sub>m</sub> reicht nicht bis ϑ): ν = 0.
- knapp darüber: ν steigt **kontinuierlich ab 0** → **Typ I** (im Gegensatz zu HH = Typ II!).
- bei großem I: **Sättigung** durch τ<sub>ref</sub> gegen ν<sub>max</sub> = 1/τ<sub>ref</sub>.

Qualitativ merken: **weiches Einsetzen ab Schwellstrom, monoton wachsend, Sättigung durch
die Refraktärzeit.**

::: ref
**Verweise:** Folie L3 „Leaky integrate-and-fire model", „LIF properties", „Activation
function of LIF neurons". Literatur: Gerstner et al., *Neuronal Dynamics*, Kap. 1.3 & 5.1;
Gerstner & Kistler, *Spiking Neuron Models*, Kap. 4.1; Dayan & Abbott, Kap. 5.4.
:::

## 4 · HH vs. LIF — direkter Vergleich

| Merkmal | Hodgkin-Huxley | LIF |
|---------|:--------------:|:---:|
| unterschwellige Integration | ✓ | ✓ |
| Spiking | ✓ (mechanistisch) | ✓ (per Schwelle + Reset) |
| wohldefinierte Schwelle ϑ | – | ✓ |
| Typ der f-I-Kurve | 2 | 1 |
| post-inhibitorischer Rebound | ✓ | – |
| Resonanz | ✓ | – |
| Zahl der ODEs | 5 | 1 |
| Rechenkosten | hoch | sehr niedrig |

→ **LIF ist eines der meistgenutzten Neuronmodelle** — schnell, analytisch handhabbar,
ideal für große Netze und Hardware. Der Preis: Es verliert Rebound, Resonanz und den
zweiten dynamischen Freiheitsgrad.

## 5 · Warum 2D? Dimensionsreduktion des HH-Modells

Reine 1D-Integration reicht nicht, um Adaptation/Rebound abzubilden. Man reduziert HH
systematisch auf **zwei** Variablen:

- **m eliminieren:** m ist sehr schnell → quasi instantan, m(t) → m₀(u(t)). Damit
  entfällt die **1. ODE**; die Na⁺-Aktivierung wird eine reine Funktion von u.
- **n und h zusammenfassen:** Es gilt näherungsweise τ<sub>n</sub>(u) ≈ τ<sub>h</sub>(u)
  und n₀(u) ≈ 1 − h₀(u). Man kombiniert sie zu **einer** langsamen Variablen **ω** mit
  Zeitkonstante τ<sub>ω</sub>. Damit entfällt die **2. ODE**.

Übrig bleibt ein **2D-System (u, ω)**. Die langsame Variable ω:
- **zieht u nach einem Spike nach unten** (Repolarisation/Adaptation),
- **reagiert langsam beim Rebound-Szenario** → spielt eine wichtige Rolle für schnell
  veränderlichen Input.

## 6 · Funktionale 2D- und Erweiterungsmodelle

Statt HH direkt zu reduzieren, entwirft man **neue, funktionale** Modelle, die die
gewünschten Effekte (2 Zeitskalen, exponentieller Spike-Anlauf, Adaptation) reproduzieren:

- **FitzHugh-Nagumo (1961)** — 2D-Prototyp mit kubischer Nichtlinearität; anschauliche
  Phasenraum-Analyse (Erregbarkeit, Grenzzyklen).
- **Izhikevich – Quadratic Integrate-and-Fire (2003)** — quadratischer Term + Reset;
  bildet mit wenigen Parametern viele Feuermuster ab; sehr recheneffizient.
- **Naud – Adaptive Exponential Integrate-and-Fire, AdEx (2008)** — LIF + exponentieller
  Spike-Term + Adaptationsvariable ω. Realistischer Spike-Anlauf, Adaptation, Rebound.
- → **Heidelberg BrainScaleS-System (2010)** setzt **AdEx** in analoger Hardware um (L11).

Zur Einordnung der AdEx-Gleichungen (Details in L11):

<p class="formula">C du/dt = −g<sub>L</sub>(u−E<sub>L</sub>) + g<sub>L</sub>Δ<sub>T</sub> exp((u−V<sub>T</sub>)/Δ<sub>T</sub>) + I − ω</p>
<p class="formula">τ<sub>ω</sub> dω/dt = a(u−E<sub>L</sub>) − ω &nbsp;&nbsp;(bei Spike: ω → ω + b)</p>

<div class="keybox">
<strong>Kernbotschaften L3:</strong> LIF = RC-Integrator + Schwelle ϑ + Reset E<sub>r</sub>
+ τ<sub>ref</sub>; Ein-/Ausgang elektrisch getrennt. Typ 1, wohldefinierte Schwelle,
1 ODE, sehr schnell — aber kein Rebound/Resonanz. f-I-Kurve: ab Schwellstrom weich
ansteigend, Sättigung durch τ<sub>ref</sub>. Für Adaptation/Rebound braucht man eine
2. langsame Variable ω → HH-Reduktion (m instantan, n&1−h→ω) oder funktionale Modelle:
FitzHugh-Nagumo, Izhikevich (QIF), AdEx (→ BrainScaleS).
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 3.1** — Welche Eigenschaft hat das **einfache** LIF-Modell **nicht**?

A) wohldefinierte Schwelle ϑ
B) absolute Refraktärzeit
C) exponentielle unterschwellige Relaxation
D) post-inhibitorischer Rebound-Spike
:::

::: mc
**MC 3.2** — „Ein- und Ausgang sind beim LIF elektrisch getrennt" bedeutet …

A) Reset und Refraktärzeit sind identisch.
B) der Spike ist Teil der Membranspannung.
C) das Neuron hat keine Schwelle.
D) der Spike-Train wirkt nicht auf die eigene Membranspannung zurück; Information fließt Membran → Spike.
:::

::: mc
**MC 3.3** — Bei der Reduktion HH → 2D wird m eliminiert, weil …

A) m sehr schnell (quasi instantan) ist, also m ≈ m₀(u).
B) m mit n identisch ist.
C) m konstant null ist.
D) m sehr langsam ist.
:::

::: mc
**MC 3.4** — Welches Modell ist die Grundlage des BrainScaleS-Systems?

A) Quadratic Integrate-and-Fire
B) reines LIF
C) Adaptive Exponential Integrate-and-Fire (AdEx)
D) FitzHugh-Nagumo
:::

::: mc
**MC 3.5** — Die Aktivierungsfunktion des LIF ist vom …

A) rein linearen Typ ohne Sättigung.
B) Typ II (Sprung auf endliche Rate).
C) Typ I (kontinuierlicher Anstieg ab Schwellstrom).
D) Typ ohne Schwellstrom.
:::

::: mc
**MC 3.6** — Wodurch wird die maximale Feuerrate des LIF bei sehr großem Strom begrenzt?

A) sie ist unbegrenzt
B) durch die Kapazität allein
C) durch die absolute Refraktärzeit τ<sub>ref</sub>
D) durch das Reset-Potential
:::

::: mc
**MC 3.7** — Ein LIF-Neuron mit konstantem Strom I feuert **gar nicht**, wenn …

A) E<sub>r</sub> = E<sub>L</sub>.
B) I/g<sub>L</sub> + E<sub>L</sub> die Schwelle ϑ nicht erreicht.
C) C sehr klein ist.
D) τ<sub>ref</sub> = 0.
:::

::: mc
**MC 3.8** — Welche Rolle spielt die langsame Variable ω im 2D-Modell?

A) Sie legt die Schwelle fest.
B) Sie zieht u nach einem Spike nach unten (Adaptation) und ermöglicht Rebound.
C) Sie erzeugt den schnellen Aufstrich des Spikes.
D) Sie ersetzt die Kapazität.
:::

::: mc
**MC 3.9** — Welche Aussage über den Vergleich HH vs. LIF ist **falsch**?

A) HH hat eine Typ-II-, LIF eine Typ-I-f-I-Kurve.
B) LIF kann post-inhibitorischen Rebound zeigen.
C) HH besteht aus 5, LIF aus 1 ODE.
D) LIF besitzt eine wohldefinierte Schwelle, HH nicht.
:::

::: mc
**MC 3.10** — Bei der HH-Reduktion werden n und h zusammengefasst, weil …

A) sie beide konstant sind.
B) beide sehr schnell sind.
C) τ<sub>n</sub> ≈ τ<sub>h</sub> und n₀ ≈ 1 − h₀ gilt → eine Variable ω genügt.
D) sie identisch mit m sind.
:::

## Freitext-Fragen (zum Besprechen)

1. Leite die Feuerrate des LIF für konstanten Strom her (unterschwellige RC-Lösung → Zeit
   bis ϑ → ν = 1/(T+τ<sub>ref</sub>)). Wann ist ν = 0?
2. Skizziere die Aktivierungsfunktion des LIF und erkläre Schwellstrom, Anstieg und die
   Sättigung durch τ<sub>ref</sub>.
3. Vergleiche HH und LIF systematisch (Schwelle, Typ, Rebound, ODE-Zahl, Kosten). In
   welchen Situationen wählst du welches Modell?
4. Erkläre, was „Ein- und Ausgang elektrisch getrennt" für die Interpretation des Spikes
   bedeutet. Warum ist der Spike beim LIF **keine** modellierte Spannungsform?
5. Warum genügt ein 1D-Integrator nicht für Adaptation/Rebound? Beschreibe die Rolle von ω.
6. Erkläre die beiden Schritte der HH→2D-Reduktion (m instantan; n & 1−h → ω) und ihre
   physikalische Rechtfertigung.
7. Nenne die vier Erweiterungsmodelle (FitzHugh-Nagumo, QIF, AdEx, → BrainScaleS) und
   ordne sie nach Komplexität/Realismus. Was fügt AdEx dem LIF konkret hinzu?
8. Was bedeutet der „Verlust der relativen Refraktärzeit" beim LIF für seine Dynamik und
   für die kodierbaren Feuermuster?
