# 09 · Tuning-Kurven, Netzdynamik & Winner-Takes-All

<p class="sub">Brain-Inspired Computing · Vorlesung 9 · ausführliche Zusammenfassung</p>

## 1 · Tuning-Kurven als Filter

Die **Tuning-Kurve** F(x) beschreibt die stationäre Feuerrate als Funktion eines
Reizmerkmals x (z. B. Orientierung, Richtung, Frequenz). Typisch: glockenförmig, mit einer
**bevorzugten** Reizrichtung und monotonem Abfall zu beiden Seiten.

Bei **zeitlich veränderlichem** Reiz wirkt die Membran/Population als **Tiefpassfilter**:
Der Ausgang ν folgt dem Input **verzögert**. Das rate-basierte Neuron:

<p class="formula">τ dν/dt = −ν + F( I(t) )</p>

Für konstantes I ist der Fixpunkt ν* = F(I). Die **Impulsantwort** (Green'sche Funktion)
eines solchen Systems ist eine abklingende Exponentielle ∝ e<sup>−t/τ</sup> — genau die
Definition der Exponentialfunktion als Lösung von dν/dt = −ν/τ. Kleine τ → schnelle,
„koinzidenzsensitive" Reaktion; große τ → träges Mitteln.

::: ref
**Verweise:** Folie L9 „tuning curve", „low-pass filter / Green's function",
„competing populations", „phase plane analysis", „Winner-Takes-All". Literatur: Dayan &
Abbott, Kap. 7 (network/firing-rate models); Gerstner et al., *Neuronal Dynamics*,
Kap. 15–16 (rate models, competition, attractors).
:::

## 2 · Konkurrierende Populationen & Phasenraum-Analyse

Zwei (oder mehr) Populationen, die sich **gegenseitig hemmen** (laterale Inhibition),
bilden ein **kompetitives** System. Zustandsvariablen sind die Raten ν₁, ν₂:

<p class="formula">τ dν<sub>1</sub>/dt = −ν<sub>1</sub> + F( w·I<sub>1</sub> − c·ν<sub>2</sub> )</p>
<p class="formula">τ dν<sub>2</sub>/dt = −ν<sub>2</sub> + F( w·I<sub>2</sub> − c·ν<sub>1</sub> )</p>

c = Stärke der gegenseitigen Hemmung, w = Eingangsgewicht. Man analysiert das System im
**Phasenraum (ν₁, ν₂)**:

- **Fixpunkte** = Schnittpunkte der **Nullklinen** (dν₁/dt = 0 und dν₂/dt = 0).
- Ihre **Stabilität** (Linearisierung/Jacobi-Matrix, Eigenwerte) entscheidet über das
  Verhalten.
- **Schwache Hemmung** (kleines c): ein einziger, symmetrischer, **stabiler** Fixpunkt →
  **beide** Populationen aktiv (Koexistenz).
- **Starke Hemmung** (großes c): **zwei stabile** Fixpunkte (nur je eine Population aktiv)
  und ein **instabiler** Sattelpunkt dazwischen → **bistabiles / WTA-Regime**.

## 3 · Winner-Takes-All (WTA)

Im WTA-Regime werden schon **kleine Input-Unterschiede** (I₁ vs. I₂) **verstärkt**: Die
stärker getriebene Population unterdrückt die andere fast vollständig → **„Winner takes
all"**.

- realisiert eine **zuverlässige Detektion des maximalen Inputs** → **Klassifikation,
  Entscheidung, Selektion**.
- die **Ausgabe** ist ein **Place-Code** (welche Population „gewinnt").
- benötigt **Nichtlinearität** in F **und** ausreichend **starke laterale Hemmung**. Bei
  rein linearer Dynamik gäbe es nur einen gemittelten Fixpunkt (kein „Sieger").

### 3.1 · Ring-Attraktor / kontinuierliches WTA

Ordnet man viele Neuronen **ringförmig** an, mit **lokaler Erregung** (Nachbarn) und
**weiter reichender Hemmung**, entsteht ein stabiler **„bump" of activity** — ein lokal
begrenztes Aktivitätsmaximum, das sich selbst erhält und (bei asymmetrischem Input) über
den Ring **wandern** kann. Modell u. a. für **Kopfrichtung** und Orientierung. Die
Zeitentwicklungs-Plots auf den Folien (V₁(t), z₁(t)) zeigen die **Konvergenz** aus
verschiedenen Startzuständen zu einem stabilen Bump (Attraktor-Dynamik).

<div class="keybox">
<strong>Kernbotschaften L9:</strong> Tuning-Kurve F(x) = stationäre Rate; Membran/Population
= Tiefpass (τ dν/dt = −ν + F(I)), Impulsantwort ∝ e<sup>−t/τ</sup>. Konkurrierende
Populationen mit lateraler Hemmung → Phasenraum-/Nullklinen-Analyse. Schwache Hemmung →
1 stabiler Fixpunkt (Koexistenz); starke Hemmung → 2 stabile Fixpunkte + 1 Sattel =
**WTA**. WTA verstärkt kleine Input-Unterschiede → Selektion/Klassifikation (Place-Code),
braucht Nichtlinearität + starke Hemmung. Ring-Anordnung → stabiler Aktivitäts-Bump
(Attraktor, z. B. Kopfrichtung).
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 9.1** — Die Gleichung τ dν/dt = −ν + F(I) beschreibt das Neuron/die Population als …

A) idealen Integrator ohne Leck
B) reines NAND-Gatter
C) reinen Hochpass
D) Tiefpass, dessen Rate F(I) verzögert folgt
:::

::: mc
**MC 9.2** — Wann zeigt ein System aus zwei sich hemmenden Populationen WTA-Verhalten?

A) nur bei linearer Aktivierungsfunktion
B) bei sehr schwacher gegenseitiger Hemmung
C) nie; WTA braucht drei Populationen
D) bei ausreichend **starker** gegenseitiger Hemmung → zwei stabile Fixpunkte
:::

::: mc
**MC 9.3** — Was leistet Winner-Takes-All funktional?

A) Es erzeugt Poisson-Statistik.
B) Es mittelt alle Eingänge gleich.
C) Es eliminiert jede Nichtlinearität.
D) Es verstärkt kleine Input-Unterschiede und selektiert den stärksten Eingang (Klassifikation).
:::

::: mc
**MC 9.4** — Die Stabilität der Fixpunkte im kompetitiven Netz bestimmt man …

A) durch Phasenraum-/Nullklinen-Analyse (Linearisierung, Eigenwerte).
B) mit dem Fano-Faktor.
C) über das Wiener-Chintschin-Theorem.
D) über die ISI-Verteilung.
:::

::: mc
**MC 9.5** — Die Impulsantwort des Systems τ dν/dt = −ν + F(I) ist …

A) eine lineare Rampe
B) eine Sinusschwingung
C) ein Dirac-Impuls
D) eine abklingende Exponentielle ∝ e<sup>−t/τ</sup>
:::

::: mc
**MC 9.6** — Bei **schwacher** gegenseitiger Hemmung (kleines c) hat das kompetitive System …

A) einen instabilen Grenzzyklus.
B) zwei stabile Fixpunkte (WTA).
C) einen einzigen, symmetrischen stabilen Fixpunkt (beide Populationen aktiv).
D) gar keinen Fixpunkt.
:::

::: mc
**MC 9.7** — Warum braucht WTA eine **nichtlineare** Aktivierungsfunktion?

A) Nur so entsteht Poisson-Statistik.
B) Nichtlinearität senkt die Feuerrate auf 0.
C) Bei rein linearer Dynamik gäbe es nur einen gemittelten Fixpunkt, keinen „Sieger".
D) Sonst wäre τ negativ.
:::

::: mc
**MC 9.8** — Ein **Ring-Attraktor** erzeugt …

A) ein reines Feed-Forward-Signal ohne Rückkopplung.
B) ausschließlich Poisson-Rauschen.
C) einen stabilen, lokal begrenzten Aktivitäts-„Bump", der wandern kann.
D) globale Synchronisation aller Neuronen.
:::

::: mc
**MC 9.9** — Die Ausgabe eines WTA-Netzes ist im Wesentlichen ein …

A) Place-Code (welches Neuron/Population gewinnt)
B) Rate-Code über alle Neuronen
C) Temporal-Code mit µs-Präzision
D) Phase-Code
:::

::: mc
**MC 9.10** — Welche zwei Zutaten sind für WTA notwendig?

A) Nichtlinearität in F und starke laterale Hemmung
B) elektrische Synapsen und kleine τ
C) NMDA-Rezeptoren und Myelin
D) Poisson-Input und Refraktärzeit
:::

## Freitext-Fragen (zum Besprechen)

1. Erkläre, warum Neuron/Population bei zeitabhängigem Reiz als Tiefpass wirken, und leite
   die exponentielle Impulsantwort aus dν/dt = −ν/τ her.
2. Skizziere die Phasenraum-/Nullklinen-Analyse zweier konkurrierender Populationen. Wie
   verändert die Hemmungsstärke c Zahl und Stabilität der Fixpunkte?
3. Warum braucht WTA sowohl Nichtlinearität als auch starke laterale Hemmung? Was passiert
   bei rein linearer Dynamik?
4. Erkläre, wie WTA kleine Input-Unterschiede verstärkt und dadurch klassifiziert. Warum
   ist die Ausgabe ein Place-Code?
5. Beschreibe den Ring-Attraktor: Wie entsteht aus lokaler Erregung + weitreichender
   Hemmung ein stabiler Bump, und wozu ist er biologisch nützlich?
6. Verknüpfe L9 mit L8: Wie hängen Tuning-Kurven, laterale Hemmung und Kontrast-/
   Kantendetektion zusammen?
