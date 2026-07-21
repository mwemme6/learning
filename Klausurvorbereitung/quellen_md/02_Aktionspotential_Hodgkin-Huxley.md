# 02 · Aktionspotential & Hodgkin-Huxley-Modell

<p class="sub">Brain-Inspired Computing · Vorlesung 2 · ausführliche Zusammenfassung</p>

## 1 · Das Problem: passive Membran kann nicht feuern

Das RC-Modell aus L1 ist **passiv** — es relaxiert nur zurück zum Ruhepotential und kann
kein selbstverstärkendes Aktionspotential (AP) erzeugen. Die Lösung der Natur:
**spannungsgesteuerte Ionenkanäle**, deren Leitwert von **Spannung und Zeit** abhängt:

<p class="formula">g<sub>X</sub> = g<sub>X</sub>(u, t)</p>

Solche Kanäle sitzen vor allem in der Membran des **Axons** (dem „Ausgang" des Neurons)
und in **Synapsen** (L4/L5). Der Schlüssel ist eine **positive Rückkopplung**:
Depolarisation öffnet Na⁺-Kanäle → mehr Na⁺ strömt ein → noch stärkere Depolarisation.

## 2 · Wie misst man die Ionenströme? Voltage-Clamp

Das **Voltage-Clamp**-Verfahren (Kenneth Cole, 1947) war die experimentelle Grundlage
von Hodgkin & Huxley. Eine schnelle Rückkopplungselektronik injiziert einen
**Kommandostrom I<sub>c</sub>(t)**, sodass die Membranspannung u(t) einem **vorgegebenen**
Verlauf folgt (die Spannung wird „festgeklemmt").

**Trick zur Trennung der Ströme:**

1. Klemmt man u(t) auf den Verlauf eines Aktionspotentials, sollte netto I<sub>c</sub> ≈ 0
   sein (kapazitiver + ionische Ströme heben sich auf).
2. **Blockiert** man gezielt einen Kanaltyp — z. B. den Na⁺-Kanal mit dem Gift **TTX**
   (Tetrodotoxin) —, dann muss die Elektronik genau den Strom **ersetzen**, der sonst
   durch diesen Kanal geflossen wäre. Der nötige I<sub>c</sub>(t) **spiegelt** also
   I<sub>Na</sub> wider.
3. Aus I<sub>Na</sub> = g<sub>Na</sub>(E<sub>Na</sub> − u) mit dem Nernst-Umkehrpotential
   E<sub>Na</sub> lässt sich der **zeit- und spannungsabhängige Leitwert** g<sub>Na</sub>(u,t)
   rekonstruieren. Analog für K⁺ (mit TEA blockierbar).

So konnten HH die einzelnen Leitfähigkeiten quantitativ vermessen und ihr Modell fitten.

::: ref
**Verweise:** Folie L2 „Voltage-Clamp", „How can INa and IK be measured".
Literatur: Gerstner & Kistler, *Spiking Neuron Models*, Kap. 2.2; Dayan & Abbott,
Kap. 5.3–5.6; Gerstner et al., *Neuronal Dynamics*, Kap. 2.2.
:::

## 3 · Kanalzustände & Gating-Variablen

Ein spannungsgesteuerter Kanal kennt **drei** Zustände:

- **Activated** — offen, Ionen fließen.
- **Inactivated** — geschlossen und **nicht** direkt wieder öffenbar (blockiert).
- **Deactivated** — geschlossen, aber **öffnungsbereit**.

Diese drei Zustände (nicht nur „auf/zu"!) erklären die **Refraktärzeit** und die
komplexe Dynamik.

### 3.1 · Na⁺- und K⁺-Kanal

- **Na⁺-Kanal:** 4 Gates — **3× m** (schnelle **Aktivierung**) und **1× h** (langsame
  **Inaktivierung**). Der Kanal leitet nur, wenn **alle drei m offen und h offen** sind.
- **K⁺-Kanal:** 4 identische Gates **n** (Aktivierung).

Effektive Leitwerte als Produkt der Öffnungswahrscheinlichkeiten:

<p class="formula">g<sub>Na</sub><sup>eff</sup> = ḡ<sub>Na</sub> · m³h &nbsp;&nbsp; I<sub>Na</sub> = ḡ<sub>Na</sub> m³h (E<sub>Na</sub> − u)</p>
<p class="formula">g<sub>K</sub><sup>eff</sup> = ḡ<sub>K</sub> · n⁴ &nbsp;&nbsp; I<sub>K</sub> = ḡ<sub>K</sub> n⁴ (E<sub>K</sub> − u)</p>

### 3.2 · Dynamik der Gating-Variablen

Jede Gating-Variable x ∈ {m, h, n} relaxiert mit spannungsabhängiger Zeitkonstante
τ<sub>x</sub>(u) zu ihrem spannungsabhängigen Gleichgewicht x₀(u):

<p class="formula">dx/dt = [ x₀(u) − x ] / τ<sub>x</sub>(u)</p>

- **m** ist **schnell** (τ<sub>m</sub> klein) → folgt der Spannung nahezu instantan.
- **h** und **n** sind **langsamer** → sorgen für Repolarisation und Refraktärzeit.
- x₀(u) sind sigmoide Kurven: m₀ und n₀ steigen mit u (Aktivierung), h₀ fällt mit u
  (Inaktivierung).

## 4 · Das vollständige Hodgkin-Huxley-Modell

Die Strombilanz an der Membran ergibt zusammen mit den drei Gating-ODEs **fünf
gekoppelte gewöhnliche Differentialgleichungen** (u, m, h, n + externer Reiz):

<p class="formula">C<sub>m</sub> du/dt = I(t) − ḡ<sub>Na</sub>m³h(u−E<sub>Na</sub>) − ḡ<sub>K</sub>n⁴(u−E<sub>K</sub>) − g<sub>L</sub>(u−E<sub>L</sub>)</p>

**Ablauf eines APs (Phasen):**

1. **Depolarisation** über die kritische Region → m öffnet schnell.
2. **Aufstrich:** Na⁺ strömt ein (positive Rückkopplung) → u schießt Richtung E<sub>Na</sub>.
3. **Umkehr/Repolarisation:** h schließt (Na⁺-Inaktivierung) **und** n öffnet
   (K⁺-Ausstrom Richtung E<sub>K</sub>) → u fällt.
4. **Hyperpolarisation (Undershoot):** n ist noch offen → u unter E<sub>L</sub>.
5. **Erholung:** m, h, n kehren zu Ruhewerten zurück.

## 5 · Drei charakteristische Eigenschaften des HH-Modells

1. **Keine einfache Feuerschwelle / Rheobase.** Anders als beim LIF gibt es **keinen**
   festen Schwellwert ϑ. Ob ein Spike ausgelöst wird, hängt **sowohl von der Amplitude
   als auch von der Änderungsgeschwindigkeit** des Reizes ab. Man definiert die
   **Rheobase** als den kleinsten **konstanten** Strom, der (bei unendlich langsamem
   Anstieg) gerade noch einen Spike auslöst.
2. **Post-inhibitorische Rebound-Spikes.** Ein **abrupt endender inhibitorischer** Reiz
   kann einen Spike auslösen: Während der Hyperpolarisation deinaktiviert h (h₀ steigt bei
   negativem u) → nach dem Reizende ist viel Na⁺-Leitfähigkeit verfügbar → Überschießen.
3. **Resonanz.** Passend **zeitlich beabstandete** unterschwellige Reize können sich zu
   einem Spike aufschaukeln — das Neuron hat eine bevorzugte Eingangsfrequenz (Folge der
   zwei Zeitskalen m schnell / n,h langsam).

## 6 · Refraktärzeit

- **Absolute Refraktärzeit:** solange die **h-Gates geschlossen** sind (Na⁺-Inaktivierung),
  ist **gar kein** neuer Spike möglich — egal wie stark der Reiz.
- **Relative Refraktärzeit:** danach graduelle Erholung, während die Gating-Variablen zu
  ihren Ruhewerten zurückkehren (h öffnet, n schließt) → ein Spike ist nur mit **stärkerem**
  Reiz möglich. Das **einfache LIF (L3) hat nur eine absolute**, keine relative Refraktärzeit.

## 7 · Typ-I vs. Typ-II & Phasendiagramm

Auf **Stufenströme** antwortet das HH-Modell mit einer **Aktivierungsfunktion** (f-I-Kurve):

- **Typ I:** die Feuerrate startet **kontinuierlich bei 0** und wächst mit dem Strom
  (beliebig niedrige Raten möglich).
- **Typ II:** die Feuerrate **springt** bei Onset auf einen **endlichen** Wert (keine
  beliebig langsamen Raten). Das HH-Modell ist von diesem Typ.

Der Stufenstrom I(t) = I₂ − ΔI + ΔI·Θ(t) (mit Heaviside-Θ) hat **zwei unabhängige
Parameter** (I₂, ΔI) → man untersucht die Antwort in Abhängigkeit von beiden. Das
**Phasendiagramm** klassifiziert die Antwort in **I** (inactive), **S** (single spike),
**R** (repetitive firing).

<div class="keybox">
<strong>Kernbotschaften L2:</strong> Spannungsgesteuerte Kanäle g<sub>X</sub>(u,t) +
positive Rückkopplung → AP. Voltage-Clamp (Cole) + Blocker (TTX) trennen die Ströme.
HH = 5 ODEs (u, m, h, n). Na⁺ ∝ m³h (schnell aktiv, langsam inaktiv), K⁺ ∝ n⁴.
Keine feste Schwelle → Rheobase. Charakteristika: absolute/relative Refraktärzeit,
post-inhibitorischer Rebound, Resonanz; Typ-II-Aktivierungsfunktion. Nachteil:
5 ODEs → schwer analysierbar, langsam zu simulieren → Vereinfachung (L3).
</div>

::: ref
**Verweise:** Folie L2 „functional model of voltage-gated channels", „Three interesting
properties", „Refractory period", „Phase diagram (I/S/R)". Petrovici, *Form Versus
Function* (Rebound/Resonanz-Abbildungen, Springer 9783319395517).
:::

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 2.1** — Der Natrium-Leitwert im HH-Modell ist proportional zu …

A) n⁴
B) m³h
C) m·h³
D) m⁴
:::

::: mc
**MC 2.2** — Was beschreibt die **absolute** Refraktärzeit korrekt?

A) Die Membranzeitkonstante τ<sub>m</sub>.
B) Die Zeit bis zum Erreichen der Rheobase.
C) Zeit, in der wegen geschlossener h-Gates (Na⁺-Inaktivierung) gar kein Spike möglich ist.
D) Zeit, in der ein Spike nur mit stärkerem Reiz möglich ist.
:::

::: mc
**MC 2.3** — Welche Aussage zur Feuerschwelle des HH-Modells stimmt?

A) Es gibt keine einfache Schwelle; Amplitude und Änderungsrate des Reizes zählen.
B) Das Feuern hängt nur von der Reizamplitude ab.
C) Es gibt eine scharf definierte, konstante Spannungsschwelle ϑ.
D) Die Rheobase ist unabhängig von den Gating-Zeitkonstanten.
:::

::: mc
**MC 2.4** — Ein post-inhibitorischer Rebound-Spike entsteht, weil …

A) das Ende eines inhibitorischen Reizes die h-Inaktivierung aufhebt und Na⁺ verfügbar macht.
B) ein starker exzitatorischer Reiz anliegt.
C) die Membrankapazität gegen null geht.
D) die K⁺-Kanäle dauerhaft offen bleiben.
:::

::: mc
**MC 2.5** — Wozu dient der pharmakologische Blocker TTX im Voltage-Clamp-Experiment?

A) Er setzt das Ruhepotential auf 0 mV.
B) Er blockiert Na⁺-Kanäle, sodass der Kommandostrom I<sub>Na</sub> spiegelt.
C) Er erhöht die Membrankapazität.
D) Er blockiert K⁺-Kanäle, um I<sub>K</sub> zu messen.
:::

::: mc
**MC 2.6** — Welche Gating-Variable ist am **schnellsten** und dominiert den Aufstrich
des APs?

A) alle gleich schnell
B) m
C) h
D) n
:::

::: mc
**MC 2.7** — Das HH-Modell ist bezüglich seiner Aktivierungsfunktion vom …

A) Typ ohne definierte f-I-Kurve.
B) Typ I (Rate startet kontinuierlich bei 0).
C) reinen Integratortyp ohne Feuern.
D) Typ II (Rate springt bei Onset auf endlichen Wert).
:::

::: mc
**MC 2.8** — Aus wie vielen gekoppelten ODEs besteht das HH-Modell (inkl. Membranspannung)?

A) 10
B) 5
C) 3
D) 2
:::

::: mc
**MC 2.9** — Welche Kombination öffnet den Na⁺-Kanal, sodass er leitet?

A) mindestens ein m offen
B) alle 3 m offen und h offen
C) alle 4 n offen
D) h geschlossen
:::

::: mc
**MC 2.10** — Der **Undershoot** (Hyperpolarisation) nach dem Spike entsteht, weil …

A) Na⁺-Kanäle noch offen sind.
B) die K⁺-Gates (n) noch offen sind und u Richtung E<sub>K</sub> (≈ −90 mV) ziehen.
C) C<sub>m</sub> negativ wird.
D) die Pumpe kurzfristig abschaltet.
:::

::: mc
**MC 2.11** — „Resonanz" im HH-Modell bedeutet …

A) dass passend zeitlich beabstandete unterschwellige Reize gemeinsam einen Spike auslösen können.
B) dass das Neuron nie feuert.
C) dass die Refraktärzeit unendlich lang ist.
D) dass jeder Reiz sofort einen Spike auslöst.
:::

## Freitext-Fragen (zum Besprechen)

1. Beschreibe den zeitlichen Ablauf eines Aktionspotentials Phase für Phase anhand von
   m, h, n. Welche Variable ist schnell, welche langsam, und warum ist das entscheidend?
2. Erkläre die **positive Rückkopplung** beim Aufstrich und was den Aufstrich schließlich
   **stoppt**.
3. Warum lässt sich beim HH-Modell keine einfache, feste Schwelle angeben? Definiere die
   Rheobase und erkläre, warum die *Änderungsrate* des Reizes eine Rolle spielt.
4. Erkläre Schritt für Schritt, wie Voltage-Clamp + TTX die einzelnen Ionenströme
   messbar/separierbar machen.
5. Was ist der Unterschied zwischen absoluter und relativer Refraktärzeit — jeweils
   mechanistisch über die Gating-Variablen begründet?
6. Warum sind post-inhibitorischer Rebound und Resonanz für ein 1D-Modell (LIF, L3)
   nicht darstellbar? Was fehlt dem LIF strukturell?
7. Vergleiche Typ-I- und Typ-II-Neuronen anhand der f-I-Kurve. Welche Konsequenzen hat
   das für die Kodierung schwacher Reize?
8. Diskutiere Vor- und Nachteile des HH-Modells für (a) Simulation und (b) analoge
   Hardware. Warum will man vereinfachen?
