# 05 · Synapsenmodelle: COBA, CUBA & High-Conductance-State

<p class="sub">Brain-Inspired Computing · Vorlesung 5 · ausführliche Zusammenfassung</p>

## 1 · LIF mit Synapsen — zwei Modellklassen

Das LIF (L3) wird um synaptische Ströme erweitert. Zentrale Frage: Ist der synaptische
Strom **spannungsabhängig** oder nicht? Daraus ergeben sich zwei Modellklassen — **COBA**
(conductance-based) und **CUBA** (current-based) —, die sich in Realismus und
mathematischer Handhabbarkeit unterscheiden.

## 2 · COBA — Conductance-Based Synapses

Jede Synapse ist ein **zeitabhängiger Leitwert** g<sub>k</sub>(t) mit eigenem
**Umkehrpotential E<sub>k</sub>**. Die Membrangleichung:

<p class="formula">C du/dt = −g<sub>L</sub>(u−E<sub>L</sub>) − Σ<sub>k</sub> g<sub>k</sub>(t)(u−E<sub>k</sub>)</p>

Der synaptische Strom eines Kanals ist **g<sub>k</sub>(t)·(u−E<sub>k</sub>)** — also
**proportional zur Differenz** zwischen aktuellem Potential und E<sub>k</sub>. Das
synaptische Gewicht w hat bei COBA die Einheit eines **Leitwerts [S] (Siemens)**.

### 2.1 · Eigenschaften

- **Spannungsabhängig / multiplikativ:** Der Effekt eines zusätzlichen Spikes hängt vom
  **aktuellen Membranpotential** ab. Nahe E<sub>k</sub> wird der Strom **klein** (die
  „Triebkraft" u−E<sub>k</sub> verschwindet); ein EPSP wirkt umso schwächer, je näher u
  bereits an E<sub>exc</sub> liegt → **automatische Sättigung / Nichtlinearität**.
- **Reversal-Potentiale bestimmen die Dynamik**, insbesondere bei Inhibition (E<sub>i</sub>):
  inhibitorische COBA-Synapsen erzeugen je nach u ein IPSP oder wirken shuntend.
- **Effektiver Leitwert & effektive Zeitkonstante:** Viele aktive Synapsen erhöhen den
  Gesamtleitwert und **verkürzen** damit die Membranzeitkonstante:

<p class="formula">g<sub>eff</sub> = g<sub>L</sub> + Σ<sub>k</sub> g<sub>k</sub>(t) &nbsp;⟹&nbsp; τ<sub>eff</sub> = C / g<sub>eff</sub> &lt; τ<sub>m</sub></p>

→ COBA ist **biophysikalisch realistisch** und die Grundlage des High-Conductance-State
(Abschnitt 5).

## 3 · CUBA — Current-Based Synapses

Jede Synapse ist ein reiner **Strom** I<sub>k</sub>(t), **unabhängig** vom Membranpotential
(kein (u−E)-Term); das Gewicht w hat hier die Einheit eines **Stroms [A] (Ampere)**:

<p class="formula">C du/dt = −g<sub>L</sub>(u−E<sub>L</sub>) + Σ<sub>k</sub> I<sub>k</sub>(t)</p>

Weil CUBA linear und u-unabhängig ist, existiert für exponentielle Kernel sogar eine
**geschlossene Lösung** (die PSP-Form ist eine Difference of Exponentials, symmetrisch in
τ<sub>m</sub> ↔ τ<sub>syn</sub>) — man muss keine DGL numerisch lösen.

### 3.1 · Eigenschaften

- **Kein Kontexteffekt:** Ein PSP derselben Synapse ist **immer gleich groß**, unabhängig
  vom aktuellen u — keine Sättigung nahe einem Reversal-Potential.
- **Konstante effektive Zeitkonstante:** τ<sub>eff</sub> = τ<sub>m</sub> bleibt unverändert
  (Synapsen tragen keinen Leitwert bei).
- **Linear & einfach:** analytisch gut behandelbar, schneller zu simulieren — aber
  **weniger realistisch**. **Warnung:** In Computersimulationen kann CUBA unphysikalische
  Ergebnisse liefern (z. B. beliebig große Depolarisation über E<sub>exc</sub> hinaus).

::: ref
**Verweise:** Folie L5 „COBA / CUBA CIF equations", „g_eff", „PSPs depend on context".
Literatur: Gerstner et al., *Neuronal Dynamics*, Kap. 3.1 (conductance vs. current based);
Dayan & Abbott, Kap. 5.8.
:::

## 4 · Synaptische Kernel — zeitlicher Verlauf

Nach einem präsynaptischen Spike bei t=0 folgt der Leitwert/Strom einem **Kernel** ε(t)
(kausal, ε(t)=0 für t&lt;0). Der Gesamtbeitrag ist die mit dem **synaptischen Gewicht w**
gewichtete Summe über alle präsynaptischen Spikes:

- **Exponentiell (single):** ε(t) = (1/τ<sub>s</sub>) e<sup>−t/τ<sub>s</sub></sup> —
  **sprunghafter** Anstieg, exponentieller Abfall mit synaptischer Zeitkonstante τ<sub>s</sub>.
  Einfachster realistischer Kernel; entsteht aus einer ODE ε̇ = −ε/τ<sub>s</sub> + Spikes.
- **Difference of Exponentials (DoE):** ε(t) ∝ (e<sup>−t/τ<sub>d</sub></sup> −
  e<sup>−t/τ<sub>r</sub></sup>) mit Abfall- τ<sub>d</sub> und Anstiegszeit τ<sub>r</sub> —
  **endliche Anstiegs- UND Abfallzeit** (realistischer als single-exp).
- **Alpha-Funktion:** Grenzfall τ<sub>r</sub> → τ<sub>d</sub> = τ:
  ε(t) = (t/τ) e<sup>−t/τ</sup> — glatter, symmetrisch wirkender Verlauf mit **einem**
  Zeitparameter; Maximum bei t = τ.

In Simulatoren wie **NEST** sind exponentielle und Alpha-Kernel Standard. Die Vorfaktor-
Konstante A vor dem Kernel legt die **physikalische Einheit** und die **Normierung** fest.
NEST wählt z. B. A = τ<sub>syn</sub> (exp) bzw. A = e·τ<sub>syn</sub> (alpha), sodass der
Kernel auf **max(ε) = 1** normiert ist. **Warnung:** Verschiedene Bücher/Simulatoren nutzen
**unterschiedliche Normierungen** — bei Zahlenwerten immer die Konvention prüfen.

## 5 · Der High-Conductance State (HCS)

**In vivo** empfangen kortikale Neuronen ständig **tausende** synaptische Eingänge → viele
Kanäle sind gleichzeitig offen. Folgen:

- **hoher Gesamtleitwert** g<sub>eff</sub> ≫ g<sub>L</sub> → **sehr kurze** effektive
  Zeitkonstante τ<sub>eff</sub> = C/g<sub>eff</sub>.
- **depolarisiertes**, stark **fluktuierendes** Membranpotential; **unregelmäßiges** Feuern
  (hoher C<sub>V</sub>, L6).
- Das Neuron wechselt vom trägen **Integrator** zum schnellen **Koinzidenzdetektor**: Nur
  Eingänge, die **zeitlich zusammenfallen**, überschreiten die Schwelle, bevor die
  Fluktuation abklingt.

Diesen Zustand bildet man korrekt nur mit **COBA** ab — bei CUBA steigt der Leitwert nicht,
also verkürzt sich τ<sub>eff</sub> nicht, und der HCS entsteht gar nicht.

::: ref
**Verweise:** Folie L5 „high-conductance state (HCS)". Grundlagenpaper: Destexhe, Rudolph
& Paré, *The high-conductance state of neocortical neurons in vivo*, Nat Rev Neurosci 4,
739–751 (2003). Gerstner et al., *Neuronal Dynamics*, Kap. 13.
:::

<div class="keybox">
<strong>Kernbotschaften L5:</strong> COBA = Leitwert g<sub>k</sub>(t)·(u−E<sub>k</sub>),
spannungsabhängig/multiplikativ, realistisch, verkürzt τ<sub>eff</sub>, PSP kontextabhängig
(Sättigung nahe E<sub>k</sub>). CUBA = Strom I<sub>k</sub>(t), spannungsunabhängig,
linear/einfach, PSP konstant, τ<sub>eff</sub>=τ<sub>m</sub>, aber unrealistischer.
Kernel: single-exp (Sprung+Abfall), Difference-of-Exp (Anstieg+Abfall), Alpha (Grenzfall,
1 Parameter). High-Conductance-State (Destexhe 2003): viele offene Kanäle → kleines
τ<sub>eff</sub>, fluktuierende Spannung, Koinzidenzdetektion → nur mit COBA modellierbar.
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 5.1** — Zentraler Unterschied COBA vs. CUBA:

A) CUBA ist biophysikalisch realistischer.
B) COBA lässt sich nicht mit LIF kombinieren.
C) COBA nutzt Ströme, CUBA Leitwerte.
D) Bei COBA hängt der synaptische Strom vom Membranpotential ab (g·(u−E<sub>syn</sub>)), bei CUBA nicht.
:::

::: mc
**MC 5.2** — Was passiert mit der effektiven Membranzeitkonstante bei vielen aktiven COBA-Synapsen?

A) Sie sinkt, weil g<sub>eff</sub> = g<sub>L</sub> + Σg<sub>k</sub> steigt.
B) Sie bleibt konstant.
C) Sie wird negativ.
D) Sie steigt.
:::

::: mc
**MC 5.3** — Die Alpha-Funktion ε(t) = (t/τ)e<sup>−t/τ</sup> ist …

A) nur für inhibitorische Synapsen definiert.
B) der Grenzfall der Difference-of-Exponentials für τ<sub>r</sub> → τ<sub>d</sub>.
C) spannungsabhängig.
D) ein rein exponentieller Abfall ohne Anstiegszeit.
:::

::: mc
**MC 5.4** — Welche Aussage zum High-Conductance-State stimmt?

A) Er tritt v. a. in ruhenden In-vitro-Slices auf.
B) Er ist durch hohen Leitwert, kurzes τ<sub>eff</sub> und fluktuierendes Potential gekennzeichnet und wird mit COBA modelliert.
C) Das Neuron wird dadurch ein langsamer Integrator.
D) CUBA bildet ihn korrekt ab.
:::

::: mc
**MC 5.5** — Warum ist bei COBA der Effekt eines EPSPs kleiner, wenn u bereits nahe
E<sub>exc</sub> liegt?

A) weil die Refraktärzeit steigt.
B) das ist bei CUBA so, nicht bei COBA.
C) weil die Triebkraft (u − E<sub>exc</sub>) klein wird → kleiner Strom.
D) weil das Gewicht w sinkt.
:::

::: mc
**MC 5.6** — Welcher synaptische Kernel hat einen **sprunghaften** Anstieg und
exponentiellen Abfall?

A) Gauß-Kernel
B) Alpha-Funktion
C) single-exponentieller Kernel
D) Difference of Exponentials
:::

::: mc
**MC 5.7** — Eine Gefahr von **CUBA** in Simulationen ist …

A) dass Synapsen zu realistisch werden.
B) dass τ<sub>eff</sub> zu stark sinkt.
C) dass das Potential unphysikalisch weit depolarisiert (kein Reversal begrenzt den Strom).
D) dass keine Spikes möglich sind.
:::

::: mc
**MC 5.8** — Im High-Conductance-State wird das Neuron funktional zum …

A) linearen Verstärker
B) reinen Oszillator
C) schnellen Koinzidenzdetektor
D) langsamen Integrator
:::

::: mc
**MC 5.9** — Die Difference-of-Exponentials unterscheidet sich vom single-exp Kernel v. a.
dadurch, dass sie …

A) keine Abfallzeit hat.
B) eine **endliche Anstiegszeit** besitzt.
C) nur bei COBA vorkommt.
D) spannungsabhängig ist.
:::

::: mc
**MC 5.10** — Welche Aussage zu CUBA ist korrekt?

A) CUBA erzeugt den High-Conductance-State.
B) PSPs derselben Synapse sind stets gleich groß; τ<sub>eff</sub> = τ<sub>m</sub>.
C) CUBA ist stets realistischer als COBA.
D) PSPs hängen stark vom aktuellen Membranpotential ab.
:::

## Freitext-Fragen (zum Besprechen)

1. Leite anschaulich her, warum bei COBA der Einfluss eines Spikes vom aktuellen
   Membranpotential abhängt (Triebkraft u−E<sub>k</sub>), bei CUBA aber nicht.
2. Zeige, wie viele COBA-Synapsen die effektive Zeitkonstante verkürzen, und verknüpfe das
   mit dem High-Conductance-State.
3. Wann würdest du CUBA bevorzugen (Analyse/Recheneffizienz), wann COBA (Realismus)?
   Welche konkreten Fehler drohen bei CUBA?
4. Erkläre den High-Conductance-State (Destexhe 2003) und seine funktionale Bedeutung
   (Integrator vs. Koinzidenzdetektor). Warum braucht man dafür zwingend COBA?
5. Vergleiche single-exp, Difference-of-Exponentials und Alpha-Kernel bezüglich Anstiegs-/
   Abfallverhalten und Parameterzahl. Wie entsteht der Alpha-Kernel als Grenzfall?
6. Diskutiere: Wie wirkt eine inhibitorische COBA-Synapse abhängig davon, ob u über oder
   unter E<sub>i</sub> liegt (Hyperpolarisation vs. Shunting)?
