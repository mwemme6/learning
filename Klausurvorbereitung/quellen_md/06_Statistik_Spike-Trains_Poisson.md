# 06 · Statistische Beschreibung von Spike-Trains

<p class="sub">Brain-Inspired Computing · Vorlesung 6 · ausführliche Zusammenfassung</p>

## 1 · Warum Statistik?

Kortikale Neuronen feuern **unregelmäßig**; einzelne Spike-Zeitpunkte sind kaum exakt
reproduzierbar (Rauschen ist allgegenwärtig — Ionenkanäle, probabilistische Vesikel-
freisetzung L4, Netzwerkfluktuationen). Statt einzelne Spikes vorherzusagen, beschreibt
man Spike-Trains **statistisch**. Der Spike-Train wird als Summe von Dirac-Impulsen
dargestellt (neuronaler „Response"):

<p class="formula">ρ(t) = Σ<sub>i</sub> δ(t − t<sub>i</sub>)</p>

Die **momentane Feuerrate** ν(t) = ⟨ρ(t)⟩ schätzt man durch Mittelung:
- über **viele Trials** (bei zeitabhängigem Reiz) → führt aufs **PSTH** (Abschnitt 6),
- über **die Zeit** (bei Stationarität) → mittlere Rate ν₀.

## 2 · Der Poisson-Prozess

Idealisiertes Modell für **gedächtnislose** (memoryless) Spike-Erzeugung: Jeder Spike
tritt **unabhängig** von der Vergangenheit auf, mit konstanter Rate ν.

- Wahrscheinlichkeit **eines** Spikes im infinitesimalen Intervall δt: **P = ν·δt**.
- P(kein Spike in δt) = 1 − ν·δt; zwei Spikes in δt sind vernachlässigbar (O(δt²)).

### 2.1 · Herleitung der Poisson-Verteilung

Teile [0, T] in M = T/δt Bins. Die Zahl N der Spikes ist binomialverteilt mit
Erfolgswahrscheinlichkeit p = νδt. Im Grenzfall M → ∞, δt → 0 mit **Mp = νT konstant**
geht die Binomial- in die **Poisson-Verteilung** über:

<p class="formula">P(N) = (νT)<sup>N</sup> e<sup>−νT</sup> / N!</p>

### 2.2 · Momente & Fano-Faktor

- **Mittelwert = Varianz:** ⟨N⟩ = Var(N) = νT (charakteristisch für Poisson).
- Der **Fano-Faktor** F = Var(N)/⟨N⟩. Für Poisson gilt **F = 1**. Misst man an einem
  Neuron F ≈ 1, spricht das für Poisson-artige Variabilität; F &lt; 1 = regelmäßiger,
  F &gt; 1 = überdispers (z. B. Bursts, langsame Rate-Fluktuationen).

## 3 · Die Interspike-Interval (ISI)-Verteilung

Komplementäres Maß: die Verteilung der Zeit s zwischen aufeinanderfolgenden Spikes.

**Herleitung (Poisson):** P(ISI ∈ [s, s+ds]) = P(kein Spike in [0,s]) · P(Spike in ds).
P(kein Spike in s) = e<sup>−νs</sup> (Grenzwert von (1−νδt)<sup>s/δt</sup>), also:

<p class="formula">P<sub>ISI</sub>(s) = ν e<sup>−νs</sup></p>

Die exponentielle ISI-Verteilung hat ihr Maximum bei s = 0 → sehr kurze Intervalle sind am
wahrscheinlichsten (typisch für Poisson: „bursty" wirkende Züge trotz konstanter Rate).

## 4 · Regularität: der Variationskoeffizient CV

Ein Maß für die **Regelmäßigkeit**:

<p class="formula">C<sub>V</sub> = σ<sub>ISI</sub> / ⟨ISI⟩</p>

- **Poisson:** C<sub>V</sub> = 1 (bei gegebener Rate maximal irregulär).
- **sehr regelmäßig** (fast periodisch): C<sub>V</sub> → 0.
- **C<sub>V</sub> &gt; 1:** irregulärer als Poisson (z. B. Bursting, gemischte Zustände).

C<sub>V</sub> ist dimensionslos und daher **ratenunabhängig** vergleichbar — anders als die
absolute Streuung σ<sub>ISI</sub>.

## 5 · Poisson-Prozess mit Refraktärzeit (→ Renewal)

Reale Neuronen haben eine **Refraktärzeit** τ<sub>ref</sub>: Direkt nach einem Spike ist
kein weiterer möglich. Das **entfernt kurze ISIs**, macht den Zug **regelmäßiger** →
**C<sub>V</sub> &lt; 1**. Die ISI-Verteilung ist dann eine um τ<sub>ref</sub> **verschobene**
Exponentialverteilung. Solche Prozesse mit „Gedächtnis nur bis zum letzten Spike" heißen
**Renewal-Prozesse** (formal in L7) — der LIF-Reset erzeugt genau so einen Prozess.

## 6 · Perspektivwechsel: Bottom-up vs. Top-down

Bis hierher (L1–L5) wurde das neuronale System **bottom-up** aufgebaut: aus der
**Biophysik** (Ionenkanäle, LIF, Synapsen), mit **vereinfachten Modellen**, um die Antwort
zu **vorherzusagen**. Die statistische Beschreibung eröffnet den umgekehrten, **top-down**
Blick: das System wird als **Black Box** behandelt (biophysik-**agnostisch**), man geht von
**Messungen** aus und beschreibt die **charakteristische** Antwort.

| | Bottom-up (bisher) | Top-down (jetzt) |
|---|--------------------|------------------|
| Grundlage | Biophysik | agnostisch (Black Box) |
| Modelle | vereinfachte Modelle | Messungen |
| Ziel | Antwort **vorhersagen** | **charakteristische** Antwort |

In diesem Rahmen unterscheidet man **Encoding** (wie ein Stimulus in Spikes übersetzt wird)
und **Decoding** (wie man aus Spikes den Stimulus rekonstruiert) — die Werkzeuge dazu
(Korrelation, PSD, STA) folgen in **L7**.

## 7 · Peri-Stimulus-Time-Histogram (PSTH)

Bei einem **wiederholten** Reiz variiert die Antwort von Trial zu Trial. Das **PSTH**
schätzt die zeitabhängige Rate:

1. Alle Trials am **Stimulus-Onset** ausrichten.
2. Spikes in Zeitfenstern [t, t+Δt] zählen.
3. über die n<sub>Trials</sub> Trials mitteln und durch die Fensterbreite teilen:

<p class="formula">ν(t) ≈ ( Anzahl Spikes in [t, t+Δt] ) / ( Δt · n<sub>Trials</sub> )</p>

Trade-off bei Δt: klein → hohe Zeitauflösung, aber verrauscht; groß → glatter, aber
verschmiert. Das PSTH ist die empirische Schätzung von ν(t) = ⟨ρ(t)⟩<sub>Trials</sub>.

::: ref
**Verweise:** Folie L6 „Poisson process", „ISI distribution", „CV", „Poisson with
refractoriness", „PSTH". Literatur: Dayan & Abbott, *Theoretical Neuroscience*, Kap.
1.2–1.4 (spike statistics, Poisson, Fano, CV); Gerstner et al., *Neuronal Dynamics*,
Kap. 7 (variability, renewal, PSTH).
:::

<div class="keybox">
<strong>Kernbotschaften L6:</strong> Spike-Train ρ(t)=Σδ(t−t<sub>i</sub>); Rate ν(t)=⟨ρ(t)⟩.
Poisson = gedächtnislos, P(Spike)=νδt → P(N)=(νT)<sup>N</sup>e<sup>−νT</sup>/N!,
Mittel=Varianz, Fano F=1, ISI exponentiell (νe<sup>−νs</sup>), C<sub>V</sub>=1.
Refraktärzeit → C<sub>V</sub>&lt;1 (regelmäßiger, verschobene Exp-Verteilung, Renewal).
PSTH = Trial-gemittelte Rate, am Stimulus-Onset ausgerichtet; Δt = Auflösung/Rausch-Trade-off.
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 6.1** — Für einen homogenen Poisson-Prozess mit Rate ν gilt für N Spikes in [0,T]:

A) ⟨N⟩ = νT, Var(N) = 0
B) ⟨N⟩ = Var(N) = νT
C) ⟨N⟩ = νT, Var(N) = (νT)²
D) ⟨N⟩ = ν, Var(N) = T
:::

::: mc
**MC 6.2** — Die ISI-Verteilung eines Poisson-Prozesses ist …

A) bimodal
B) exponentiell: ν e<sup>−νs</sup>
C) gaußförmig
D) gleichverteilt
:::

::: mc
**MC 6.3** — Ein Neuron mit ausgeprägter Refraktärzeit hat einen …

A) C<sub>V</sub> = 1
B) C<sub>V</sub> < 1
C) undefinierten C<sub>V</sub>
D) C<sub>V</sub> > 1
:::

::: mc
**MC 6.4** — Wozu dient der Fano-Faktor?

A) Zur Berechnung der Refraktärzeit.
B) Zur Messung der ISI-Länge.
C) Als Verhältnis Var(N)/⟨N⟩; ≈1 spricht für Poisson-artige Variabilität.
D) Als Maß für die Membranzeitkonstante.
:::

::: mc
**MC 6.5** — Das PSTH …

A) ist identisch zur ISI-Verteilung.
B) misst die Zahl der Ionenkanäle.
C) schätzt die zeitabhängige Feuerrate durch Trial-Mittelung, ausgerichtet am Stimulus-Onset.
D) benötigt nur einen einzigen Trial.
:::

::: mc
**MC 6.6** — Was bedeutet „gedächtnislos" (memoryless) beim Poisson-Prozess?

A) Alle ISIs sind gleich lang.
B) Die Wahrscheinlichkeit eines Spikes hängt nicht von der Vergangenheit ab.
C) Die Rate ν ändert sich zufällig.
D) Es gibt keine ISI-Verteilung.
:::

::: mc
**MC 6.7** — Der Variationskoeffizient C<sub>V</sub> ist definiert als …

A) σ<sub>ISI</sub>² · ⟨ISI⟩
B) Var(N) / ⟨N⟩
C) ⟨ISI⟩ / σ<sub>ISI</sub>
D) σ<sub>ISI</sub> / ⟨ISI⟩
:::

::: mc
**MC 6.8** — Ein Prozess mit C<sub>V</sub> ≈ 0 beschreibt ein Neuron, das …

A) nahezu periodisch/sehr regelmäßig feuert.
B) in Bursts feuert.
C) rein zufällig (Poisson) feuert.
D) gar nicht feuert.
:::

::: mc
**MC 6.9** — Beim Übergang Binomial → Poisson hält man konstant:

A) die Varianz = 0.
B) das Produkt M·p = νT.
C) die Bin-Breite δt.
D) die Zahl der Trials.
:::

::: mc
**MC 6.10** — Welche Aussage über die exponentielle ISI-Verteilung ist korrekt?

A) Sie ist symmetrisch um ⟨ISI⟩.
B) Sie hat ihr Maximum bei s = 0 (kurze ISIs am wahrscheinlichsten).
C) Sie hat ihr Maximum bei großen s.
D) Sie ist nur bei Refraktärzeit definiert.
:::

::: mc
**MC 6.11** — Was kennzeichnet die **Top-down**-Perspektive (im Gegensatz zu Bottom-up)?

A) Aufbau aus Ionenkanälen und LIF-Gleichungen.
B) Vorhersage der Antwort aus der Biophysik.
C) Das System wird als Black Box aus Messungen charakterisiert (biophysik-agnostisch).
D) Sie ist nur für einzelne Spikes definiert.
:::

## Freitext-Fragen (zum Besprechen)

1. Leite die Poisson-Verteilung aus der Binomialverteilung her (Grenzwert M→∞, νT
   konstant). Warum ist ⟨N⟩ = Var(N)?
2. Was sagt eine Abweichung des Fano-Faktors von 1 (nach oben/unten) über den neuronalen
   Code bzw. den Feuerprozess aus?
3. Leite die exponentielle ISI-Verteilung des Poisson-Prozesses her. Warum sind kurze ISIs
   am wahrscheinlichsten, obwohl die Rate konstant ist?
4. Erkläre C<sub>V</sub> und die Fälle C<sub>V</sub> = 1, &lt; 1, &gt; 1. Wie verändert
   eine Refraktärzeit ISI-Verteilung und C<sub>V</sub>?
5. Wie unterscheidet sich Ratenmittelung über Zeit von der über Trials (PSTH)? Wann ist
   welche zulässig, und welche Rolle spielt die Fensterbreite Δt?
6. Warum ist der Poisson-Prozess trotz seiner Einfachheit ein so nützliches Nullmodell für
   kortikale Aktivität — und wo versagt er?
