# 07 · Korrelationen, Renewal-Prozess, Power-Spektrum & STA

<p class="sub">Brain-Inspired Computing · Vorlesung 7 · ausführliche Zusammenfassung</p>

## 1 · Typische Fragestellungen

Um zu verstehen, welche Information ein Neuron überträgt, betrachtet man die **zeitliche
Korrelation** zwischen Reiz x(t) und Antwort ρ(t). Leitfragen der Vorlesung:

1. Welche Signale y(t) kann ein Neuron mit gegebener ISI-Statistik überhaupt **sauber
   übertragen**?
2. Ist ein Neuron gut geeignet, Information über einen Stimulus-Satz {x} zu **vermitteln**?
3. **Encoding vs. Decoding:** (A) Können wir aus der Antwort das Signal **rekonstruieren**
   (Decoding)? (B) Können wir die Antwort auf **künftige** Reize **vorhersagen** (Encoding)?

Alle drei stützen sich auf die zeitliche Korrelation von x(t) und dem Spike-Train ρ(t).

## 2 · Auto- & Kreuzkorrelationsfunktion

Für einen Satz von Signalen x<sub>i</sub>(t) definiert man die **Kreuzkorrelationsfunktion
(CCF)** als zeitgemittelte Überlappung mit Verschiebung s:

<p class="formula">C<sub>ij</sub>(s) = lim<sub>T→∞</sub> (1/2T) ∫<sub>−T</sub><sup>T</sup> x<sub>i</sub>(t) x<sub>j</sub>(t+s) dt = ⟨x<sub>i</sub>(t) x<sub>j</sub>(t+s)⟩<sub>t</sub></p>

**Warum der Grenzprozess (1/2T)∫?** Unendlich fortlaufende Signale (Spike-Train, Sinus)
haben **unendliche Energie**; ohne die Division durch 2T würde das Integral **nicht
konvergieren**. Man bildet daher den **Zeitmittelwert** (endliche „Leistung" statt
unendlicher „Energie").

- **Symmetriebeziehung:** C<sub>ij</sub>(s) = C<sub>ji</sub>(−s).
- **Autokorrelationsfunktion (ACF):** Korreliert man ein Signal mit **sich selbst**,
  erhält man C<sub>ii</sub>(s), die **symmetrisch** ist: C<sub>ii</sub>(s) = C<sub>ii</sub>(−s).
  Sie misst, wie sehr sich ein Signal nach der Zeit s „selbst ähnelt".

## 3 · Der Renewal-Prozess

Der **Renewal-Prozess** ist der formale Rahmen für die statistische Analyse von
Spike-Trains und eine **Verallgemeinerung** des Poisson-Prozesses:

- **Poisson-Prozess:** **kein** Gedächtnis (memoryless).
- **Renewal-Prozess:** Gedächtnis reicht **bis zum jüngsten Ereignis** (dem letzten Spike).
  Danach „erneuert" sich der Prozess. Beim **LIF löscht der Reset** des Membranpotentials
  die gesamte Vergangenheit → aufeinanderfolgende ISIs sind unabhängig und identisch
  verteilt → der LIF-Output ist ein Renewal-Prozess. (Refraktärzeit, L6, ist ein Spezialfall.)

## 4 · ACF, Renewal-Dichte & Power-Spektrum

Die ACF des Spike-Trains ρ(t) zerfällt in **Selbstkorrelation** + **Renewal-Dichte**:

<p class="formula">C<sub>ρρ</sub>(τ) = ⟨ρ(t)ρ(t+τ)⟩ = ν₀ δ(τ) + ν₀ m(τ)</p>

- **ν₀ δ(τ)** — Selbstkorrelationsterm: ein Spike korreliert bei **τ=0** perfekt mit sich
  selbst (Dirac-Peak, gewichtet mit der mittleren Rate ν₀).
- **m(τ)** — **Renewal-Dichte** (intensity function) für τ &gt; 0: die bedingte
  Wahrscheinlichkeitsdichte, **irgendeinen** Folgespike zur Zeit τ nach einem Referenzspike
  zu finden — **egal, wie viele Spikes dazwischen** liegen. m(τ) folgt aus P<sub>ISI</sub>(τ)
  (Summe über 1., 2., 3. … Folgespike).

### 4.1 · Wiener-Chintschin-Theorem → Power Spectral Density

Das **Wiener-Chintschin-Theorem** besagt: Die **Power Spectral Density (PSD)** eines
**stationären** Zufallsprozesses ist die **Fourier-Transformierte seiner
Autokorrelationsfunktion**:

<p class="formula">𝒫(ω) = ∫ C<sub>ρρ</sub>(τ) e<sup>−iωτ</sup> dτ = ν₀ ( 1 + m̃(iω) + m̃*(iω) )</p>

Mit dem Zusammenhang der Fourier-Transformierten von P<sub>ISI</sub> und m — nämlich
m̃(iω) = P̃<sub>ISI</sub>(iω) / (1 − P̃<sub>ISI</sub>(iω)) — ergibt sich kompakt:

<p class="formula">𝒫(ω) = ν₀ · (1 − |P̃<sub>ISI</sub>(iω)|²) / |1 − P̃<sub>ISI</sub>(iω)|²</p>

**Bedeutung:** Aus der **ISI-Verteilung** folgt direkt das **Leistungsspektrum** des
Spike-Trains — man sieht, welche Frequenzen ein Neuron übertragen kann. **Anwendung:**
LGN-Neuronen bei natürlichem Filmreiz vs. Weißrausch-Stimulus zeigen unterschiedliche
ACFs/PSDs (Warland, Reinagel & Meister, 1997).

## 5 · Spike-Triggered Average (STA)

Werkzeug für **Encoding/Decoding**: Man mittelt den **Reiz in einem Zeitfenster vor jedem
Spike**:

<p class="formula">STA(τ) = ⟨ x(t<sub>i</sub> − τ) ⟩<sub>Spikes</sub></p>

Anschaulich: Man legt vor jeden Spike ein „Fenster" in die Reizvergangenheit und mittelt
alle diese Reizausschnitte. Ergebnis:

- der **durchschnittliche Reiz, der einem Spike vorausgeht** → schätzt das **lineare
  rezeptive Feld** / den bevorzugten Reiz des Neurons.
- **Zusammenhang mit der Korrelation:** Die STA ist (bis auf den Faktor 1/ν) die
  **Kreuzkorrelation** von Spike-Train und Reiz: STA(τ) = (1/ν)·C<sub>ρx</sub>(−τ).
- **Beispiel:** elektrosensorisches Neuron des schwach elektrischen Fisches *Eigenmannia*
  (Gabbiani et al., 1996) — die STA zeigt die charakteristische (biphasische) Reizform vor
  einem Spike → das Neuron reagiert auf eine zeitliche **Änderung**, nicht auf einen
  konstanten Wert.
- **Warnung (Stimulus-Statistik):** Die STA hängt von der **Reizstatistik** ab (man misst
  nur, was präsentiert wurde). Für eine **unverzerrte** Schätzung nutzt man daher einen
  **White-Noise-Stimulus** (alle Frequenzen gleich stark).
- **Grenze:** Die STA ist ein **lineares** Maß; stark nichtlineare Antworten (z. B.
  richtungs-/kontrastinvariante Zellen) erfasst sie nur unvollständig.

::: ref
**Verweise:** Folie L7 „Auto- and cross-correlation", „Renewal process", „ACF & PSD",
„Wiener-Chintschin", „spike-triggered average". Literatur: Gerstner et al., *Neuronal
Dynamics*, Kap. 7 (renewal, power spectrum); Dayan & Abbott, Kap. 1.4 & 2 (autocorrelation,
STA, reverse correlation). Warland, Reinagel & Meister (1997).
:::

<div class="keybox">
<strong>Kernbotschaften L7:</strong> CCF/ACF = zeitgemittelte Korrelation; Grenzprozess
(1/2T)∫ nötig wegen unendlicher Energie; ACF symmetrisch. Renewal-Prozess = Poisson mit
Gedächtnis bis zum letzten Spike (LIF-Reset!). ACF = ν₀δ(τ) + ν₀m(τ) mit Renewal-Dichte
m(τ) aus P<sub>ISI</sub>. Wiener-Chintschin: PSD = Fourier(ACF) → aus ISI-Verteilung
berechenbar. STA = mittlerer Reiz vor dem Spike → lineares rezeptives Feld (nichtlinear
begrenzt).
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 7.1** — Warum enthält die Definition der Korrelationsfunktion einen Grenzprozess
lim<sub>T→∞</sub> (1/2T)∫?

A) Wegen der Poisson-Statistik.
B) Wegen der Refraktärzeit.
C) Um die Fourier-Transformation zu vermeiden.
D) Weil fortlaufende Signale unendliche Energie haben; der Zeitmittelwert macht das Integral konvergent.
:::

::: mc
**MC 7.2** — Was besagt das Wiener-Chintschin-Theorem?

A) Der C<sub>V</sub> eines Poisson-Prozesses ist 1.
B) Die PSD ist die Ableitung der ISI-Verteilung.
C) Die PSD eines stationären Prozesses ist die Fourier-Transformierte seiner Autokorrelationsfunktion.
D) Die ACF ist immer null.
:::

::: mc
**MC 7.3** — Ein Renewal-Prozess unterscheidet sich vom Poisson-Prozess dadurch, dass …

A) sein Gedächtnis bis zum jüngsten Ereignis reicht (z. B. durch den LIF-Reset).
B) er keine ISI-Verteilung besitzt.
C) er stets streng periodisch feuert.
D) er gar kein Gedächtnis hat.
:::

::: mc
**MC 7.4** — Der Spike-Triggered Average (STA) …

A) ist die Fourier-Transformierte der ISI-Verteilung.
B) misst die Refraktärzeit.
C) ist die Autokorrelation des Spike-Trains.
D) mittelt den Reiz in einem Fenster vor jedem Spike und schätzt das lineare rezeptive Feld.
:::

::: mc
**MC 7.5** — In der ACF C<sub>ρρ</sub>(τ) = ν₀δ(τ) + ν₀m(τ) beschreibt m(τ) …

A) das Reset-Potential.
B) die Renewal-Dichte: bedingte Dichte eines Folgespikes τ nach einem Referenzspike.
C) die Membranzeitkonstante.
D) den Fano-Faktor.
:::

::: mc
**MC 7.6** — Für die ACF eines Signals gilt allgemein …

A) C<sub>ii</sub>(s) = 0 für alle s.
B) C<sub>ii</sub>(s) = −C<sub>ii</sub>(−s) (antisymmetrisch).
C) C<sub>ii</sub>(s) = C<sub>ii</sub>(−s) (symmetrisch).
D) C<sub>ii</sub>(s) ist komplexwertig.
:::

::: mc
**MC 7.7** — Der Term ν₀δ(τ) in der ACF entsteht, weil …

A) das Neuron nie feuert.
B) zwei verschiedene Neuronen korreliert werden.
C) die Rate zeitabhängig ist.
D) jeder Spike bei τ = 0 perfekt mit sich selbst korreliert (Selbstkorrelation).
:::

::: mc
**MC 7.8** — Warum ist der LIF-Neuronen-Output ein Renewal-Prozess?

A) Weil er kein Reset besitzt.
B) Weil er keine Refraktärzeit hat.
C) Weil er streng periodisch ist.
D) Weil der Reset die Vergangenheit löscht → aufeinanderfolgende ISIs sind unabhängig.
:::

::: mc
**MC 7.9** — Eine wesentliche **Grenze** der STA ist, dass sie …

A) ein lineares Maß ist und stark nichtlineare Antworten nur unvollständig erfasst.
B) nur bei Poisson-Neuronen definiert ist.
C) das Power-Spektrum nicht kennt.
D) nur nach dem Spike mittelt.
:::

::: mc
**MC 7.10** — Aus welcher Größe lässt sich mit Wiener-Chintschin das Leistungsspektrum
eines Renewal-Spike-Trains berechnen?

A) aus dem Reset-Potential
B) aus der ISI-Verteilung P<sub>ISI</sub>(τ)
C) aus der Membrankapazität
D) aus der Schwelle ϑ
:::

::: mc
**MC 7.11** — Warum verwendet man zur STA-Messung bevorzugt einen **White-Noise-Stimulus**?

A) Weil White Noise die Feuerrate maximiert.
B) Weil die STA sonst gar nicht definiert ist.
C) Weil White Noise alle Frequenzen gleich enthält → unverzerrte Schätzung (STA hängt von der Reizstatistik ab).
D) Weil nur so die Refraktärzeit sichtbar wird.
:::

## Freitext-Fragen (zum Besprechen)

1. Erkläre den Unterschied zwischen Encoding und Decoding und welche Werkzeuge (CCF, STA,
   PSD) jeweils helfen.
2. Warum braucht die Korrelationsfunktion den Grenzprozess (1/2T)∫? Was ist der Unterschied
   zwischen „Energie-" und „Leistungssignalen"?
3. Warum ist der LIF-Output ein Renewal-Prozess? Welche Rolle spielt der Reset, und wie
   grenzt sich Renewal vom Poisson-Prozess ab?
4. Skizziere die Kette P<sub>ISI</sub> → m(τ) → C<sub>ρρ</sub>(τ) → 𝒫(ω). Was besagt
   Wiener-Chintschin und wozu ist das nützlich?
5. Erkläre die STA-Berechnung anschaulich (Fenster vor jedem Spike, mitteln). Was verrät
   sie über die Funktion eines sensorischen Neurons, und wo liegen ihre Grenzen?
6. Interpretiere: Was bedeutet es, wenn die ACF eines Neurons einen Nebengipfel bei
   τ ≈ 1/f zeigt? (Hinweis: Oszillation/Rhythmus im Feuern.)
