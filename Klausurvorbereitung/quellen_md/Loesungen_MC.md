# Lösungen · Multiple-Choice (alle Vorlesungen)

<p class="sub">Brain-Inspired Computing · Klausurvorbereitung · Lösungsschlüssel mit Begründungen</p>

> Nutze diese Datei erst **nach** dem Beantworten der Fragen — nicht vorher spicken.
> Die Antwortpositionen (A–D) sind bewusst gemischt.

## Vorlesung 01 · Einführung, Neuron & Membran

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 1.1 | **A** | Falsch ist: Gehirn hat Speicher & Verarbeitung *vermischt* (in-memory), nicht getrennt. |
| 1.2 | **D** | Pumpe erzeugt die Konzentrationsdifferenz unter ATP-Verbrauch (~⅔ Energie); Ladungsbeitrag vernachlässigbar. |
| 1.3 | **B** | τ<sub>m</sub> = C<sub>m</sub>/g<sub>L</sub> = R<sub>m</sub>C<sub>m</sub>. |
| 1.4 | **C** | GHK kombiniert mehrere Ionen gewichtet nach Permeabilitäten zu E<sub>L</sub> (Nernst = ein Ion). |
| 1.5 | **D** | I<sub>X</sub> = g<sub>X</sub>(u−E<sub>X</sub>): u &lt; E<sub>X</sub> ⇒ I &lt; 0. |
| 1.6 | **B** | Reines RC ist passiv/linear ohne regenerative spannungsabhängige Leitwerte → kein Spike. |
| 1.7 | **A** | Im Ruhezustand dominiert die K⁺-Permeabilität → E<sub>L</sub> nahe E<sub>K</sub>. |
| 1.8 | **B** | Patch-Clamp (einzelne Ionenkanäle): Neher & Sakmann. |
| 1.9 | **A** | Kleine τ<sub>m</sub> → schnelle Reaktion → Koinzidenzdetektor. |
| 1.10 | **C** | ~10¹¹ Neuronen, ~10¹⁵ Synapsen, ~20 W. |

## Vorlesung 02 · Aktionspotential & Hodgkin-Huxley

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 2.1 | **B** | g<sub>Na</sub> ∝ m³h (3 Aktivierungs-, 1 Inaktivierungsgate). |
| 2.2 | **C** | Absolute Refraktärzeit: h-Gates geschlossen (Na⁺-Inaktivierung) → gar kein Spike. |
| 2.3 | **A** | Keine feste Schwelle; Amplitude UND Änderungsrate zählen → Rheobase. |
| 2.4 | **A** | Ende der Inhibition deinaktiviert h → Na⁺ verfügbar → Rebound-Spike. |
| 2.5 | **B** | TTX blockiert Na⁺-Kanäle; der Kommandostrom spiegelt dann I<sub>Na</sub>. |
| 2.6 | **B** | m ist am schnellsten und dominiert den Aufstrich. |
| 2.7 | **D** | HH ist Typ II (Rate springt bei Onset auf endlichen Wert). |
| 2.8 | **B** | 5 gekoppelte ODEs (u, m, h, n + Reiz). |
| 2.9 | **B** | Na⁺-Kanal leitet, wenn alle 3 m offen UND h offen. |
| 2.10 | **B** | Undershoot: n-Gates noch offen → u Richtung E<sub>K</sub> ≈ −90 mV. |
| 2.11 | **A** | Resonanz: passend beabstandete unterschwellige Reize lösen gemeinsam einen Spike aus. |

## Vorlesung 03 · LIF & 2D-Modelle

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 3.1 | **D** | Einfaches LIF hat keinen post-inhibitorischen Rebound (fehlende 2. Variable). |
| 3.2 | **D** | Spike-Train wirkt nicht auf die Membran zurück; Info fließt Membran → Spike. |
| 3.3 | **A** | m ist quasi instantan (m ≈ m₀(u)) → 1. ODE entfällt. |
| 3.4 | **C** | BrainScaleS basiert auf AdEx (Naud 2008). |
| 3.5 | **C** | LIF ist Typ I (kontinuierlicher Anstieg ab Schwellstrom). |
| 3.6 | **C** | Maximale Rate durch τ<sub>ref</sub> begrenzt (ν<sub>max</sub> = 1/τ<sub>ref</sub>). |
| 3.7 | **B** | Feuert nie, wenn I/g<sub>L</sub> + E<sub>L</sub> die Schwelle ϑ nicht erreicht. |
| 3.8 | **B** | ω zieht u nach Spike nach unten (Adaptation) und ermöglicht Rebound. |
| 3.9 | **B** | Falsch ist: „LIF kann Rebound zeigen" — kann es nicht. |
| 3.10 | **C** | n & h werden zu ω zusammengefasst, da τ<sub>n</sub>≈τ<sub>h</sub>, n₀≈1−h₀. |

## Vorlesung 04 · Synapsen & synaptische Übertragung

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 4.1 | **A** | Ca²⁺-Einstrom durch spannungsgesteuerte Kanäle löst Vesikelfusion aus. |
| 4.2 | **D** | E<sub>rev</sub> ≈ −70 mV (Cl⁻) → inhibitorisch (GABA_A). |
| 4.3 | **C** | NMDA leitet nur bei Glutamat UND postsyn. Depolarisation (Mg²⁺-Block gelöst). |
| 4.4 | **B** | Myelin isoliert; AP springt zwischen Ranvier-Schnürringen → schneller/effizienter. |
| 4.5 | **C** | Gap Junctions: schnell, bidirektional, synchronisierend. |
| 4.6 | **B** | Erregend/hemmend entscheidet E<sub>syn</sub> relativ zu Ruhe-/Schwellpotential. |
| 4.7 | **A** | AMPA: schnellste, häufigste exzitatorische Synapse. |
| 4.8 | **C** | Shunting inhibition: Hemmung durch erhöhten Leitwert, auch ohne Hyperpolarisation. |
| 4.9 | **A** | Vesikelfreisetzung ist stochastisch/probabilistisch. |
| 4.10 | **A** | NMDA: längste Zeitkonstante (~20 ms), leitet Ca²⁺. |
| 4.11 | **A** | Dale's principle: gleicher Transmitter an allen Synapsen → Neuron einheitlich exz./inh. |

## Vorlesung 05 · Synapsenmodelle COBA/CUBA

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 5.1 | **D** | COBA-Strom hängt via g·(u−E<sub>syn</sub>) vom Membranpotential ab, CUBA nicht. |
| 5.2 | **A** | τ<sub>eff</sub> = C/g<sub>eff</sub> sinkt, da g<sub>eff</sub> = g<sub>L</sub>+Σg<sub>k</sub> steigt. |
| 5.3 | **B** | Alpha = Grenzfall der Difference-of-Exponentials (τ<sub>r</sub> → τ<sub>d</sub>). |
| 5.4 | **B** | HCS: hoher Leitwert, kurzes τ<sub>eff</sub>, fluktuierendes Potential; COBA-Modell. |
| 5.5 | **C** | Nahe E<sub>exc</sub> wird die Triebkraft (u−E<sub>exc</sub>) klein → kleiner Strom. |
| 5.6 | **C** | Single-exp Kernel: sprunghafter Anstieg, exponentieller Abfall. |
| 5.7 | **C** | CUBA-Gefahr: unphysikalisch weite Depolarisation (kein Reversal begrenzt den Strom). |
| 5.8 | **C** | Im HCS wird das Neuron ein schneller Koinzidenzdetektor. |
| 5.9 | **B** | Difference-of-Exp hat eine endliche Anstiegszeit (ggü. single-exp). |
| 5.10 | **B** | CUBA: PSPs stets gleich groß; τ<sub>eff</sub> = τ<sub>m</sub>. |

## Vorlesung 06 · Statistik von Spike-Trains

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 6.1 | **B** | Poisson: ⟨N⟩ = Var(N) = νT → Fano = 1. |
| 6.2 | **B** | ISI exponentiell: ν e<sup>−νs</sup>. |
| 6.3 | **B** | Refraktärzeit → regelmäßiger → C<sub>V</sub> &lt; 1. |
| 6.4 | **C** | Fano-Faktor = Var(N)/⟨N⟩; ≈1 → Poisson-artig. |
| 6.5 | **C** | PSTH: Trial-gemittelte Rate, am Stimulus-Onset ausgerichtet. |
| 6.6 | **B** | Memoryless: Spike-Wahrscheinlichkeit unabhängig von der Vergangenheit. |
| 6.7 | **D** | C<sub>V</sub> = σ<sub>ISI</sub> / ⟨ISI⟩. |
| 6.8 | **A** | C<sub>V</sub> ≈ 0 → nahezu periodisch/sehr regelmäßig. |
| 6.9 | **B** | Binomial → Poisson: Produkt M·p = νT konstant halten. |
| 6.10 | **B** | Exp-ISI-Verteilung: Maximum bei s = 0 (kurze ISIs am wahrscheinlichsten). |
| 6.11 | **C** | Top-down = Black-Box-Charakterisierung aus Messungen (biophysik-agnostisch), vs. Bottom-up (Biophysik). |

## Vorlesung 07 · Korrelation, Renewal, PSD & STA

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 7.1 | **D** | Fortlaufende Signale haben unendliche Energie → Zeitmittel (1/2T)∫ macht das Integral konvergent. |
| 7.2 | **C** | PSD = Fourier-Transformierte der Autokorrelationsfunktion (stationär). |
| 7.3 | **A** | Renewal: Gedächtnis bis zum jüngsten Ereignis (LIF-Reset). |
| 7.4 | **D** | STA = mittlerer Reiz im Fenster vor jedem Spike → lineares rezeptives Feld. |
| 7.5 | **B** | m(τ) = Renewal-Dichte: bedingte Dichte eines Folgespikes τ nach Referenzspike. |
| 7.6 | **C** | ACF ist symmetrisch: C<sub>ii</sub>(s) = C<sub>ii</sub>(−s). |
| 7.7 | **D** | ν₀δ(τ): jeder Spike korreliert bei τ=0 perfekt mit sich selbst. |
| 7.8 | **D** | Reset löscht die Vergangenheit → aufeinanderfolgende ISIs unabhängig → Renewal. |
| 7.9 | **A** | STA ist ein lineares Maß → stark nichtlineare Antworten nur unvollständig erfasst. |
| 7.10 | **B** | Aus der ISI-Verteilung P<sub>ISI</sub>(τ) folgt via Wiener-Chintschin die PSD. |
| 7.11 | **C** | White Noise enthält alle Frequenzen gleich → unverzerrte STA (hängt sonst von der Reizstatistik ab). |

## Vorlesung 08 · Neuronale Codes & Netze

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 8.1 | **B** | Place-Code nutzt die Identität des feuernden Neurons (Ortszellen). |
| 8.2 | **D** | On-Center-Felder → Difference of Gaussians (DoG). |
| 8.3 | **A** | Kleines Rate-Netz realisiert NAND; NAND funktional vollständig → Turing-vollständig. |
| 8.4 | **A** | Delay-Line + Koinzidenzdetektor = Temporal-Code (µs-Präzision). |
| 8.5 | **C** | ν<sub>out</sub> = F(Σw<sub>j</sub>ν<sub>j</sub>): Brücke zu Perzeptron/Deep Learning. |
| 8.6 | **D** | NOT(x) = NAND(x, x). |
| 8.7 | **C** | Diffuses Licht: erregendes Zentrum und hemmendes Umfeld heben sich auf. |
| 8.8 | **D** | Temporal-Code hat die höchste zeitliche Auflösung. |
| 8.9 | **C** | Phase Precession = Phase-Code (relativ zur Theta-Oszillation). |
| 8.10 | **B** | Rule-based ist möglich (Turing-vollständig), aber nicht der natürliche/effiziente Modus. |
| 8.11 | **B** | NOT = 1 Neuron (Gewicht −1, Bias H+L); NAND = zweistufiges Netz (Nichtlinearität an z₁). |
| 8.12 | **A** | Rekurrentes Rate-Netz: F = Aktivierungsfunktion, b<sub>k</sub> = Bias, mit Rückkopplung w<sub>kj</sub>z<sub>j</sub>. |

## Vorlesung 09 · Tuning, Netzdynamik & WTA

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 9.1 | **B** | Skalarprodukt **V**<sub>k</sub>·**x** maximal, wenn Input parallel zu **V**<sub>k</sub> (bei fester ‖**x**‖). |
| 9.2 | **C** | **V**<sub>k</sub> = bevorzugtes Eingangsmuster / räumlicher Kernel → Template-Matching. |
| 9.3 | **C** | Feed-forward-Neuron = Tiefpass, Green-Funktion G(t)=Θ(t)e<sup>−t/τ</sup>. |
| 9.4 | **D** | Zwei kaskadierte Exponential-Tiefpässe → Difference of Exponentials. |
| 9.5 | **A** | Konkurrenz über eine gemeinsame inhibitorische Population (geteilte Hemmung). |
| 9.6 | **C** | Schwacher symmetrischer Input (V=4) → drei stabile Fixpunkte (symmetrisch + zwei Gewinner). |
| 9.7 | **B** | Asymmetrischer Input (\|V<sub>1</sub>−V<sub>2</sub>\|>δ) → ein Fixpunkt, stärkerer Kanal gewinnt. |
| 9.8 | **B** | V≳4,7 → Saddle-node-Bifurkation; kleinste Anfangsunterschiede entscheiden. |
| 9.9 | **D** | Critical slowing down: langes Verharren im labilen Zustand, dann abrupte Umschaltung. |
| 9.10 | **C** | Tuning + mehrere WTA-Populationen = Klassifikator (Detektion + eindeutiger Output-Code). |

## Vorlesung 10 · Plastizität: STP, LTP/LTD, STDP

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 10.1 | **D** | Tsodyks-Markram: R + E + I = 1. |
| 10.2 | **A** | Depression: R zwischen Spikes nicht erholt (hohe Rate) → kleinere PSPs. |
| 10.3 | **C** | pre vor post (Δt &gt; 0) → LTP. |
| 10.4 | **D** | NMDAR = Koinzidenzdetektor (Glutamat + Depol.), steuert Ca²⁺-Einstrom. |
| 10.5 | **A** | LTP und LTD über (teils) verschiedene biochemische Pfade. |
| 10.6 | **C** | Facilitation: adaptiver, mit jedem Spike steigender Freisetzungsparameter U(t). |
| 10.7 | **D** | Hochfrequente Stimulation (~100 Hz) → LTP. |
| 10.8 | **C** | Hohe [Ca²⁺] → LTP, moderate [Ca²⁺] → LTD. |
| 10.9 | **B** | Postsyn. Timing-Signal via rückwärtslaufende AP (bAP). |
| 10.10 | **B** | Hebb: A kausal am Feuern von B beteiligt → Verbindung A→B verstärkt. |
| 10.11 | **B** | STDP hat verschiedene Formen, ist nichtlinear/orts-/frequenzabhängig → nicht universell. |
| 10.12 | **C** | Speicher-Argument: ~10¹⁵ Synapsen ≫ ~10¹⁰ Basenpaare (≈ 2 GB) → nicht genetisch kodierbar. |

## Vorlesung 11 · Neuromorphe Hardware & BrainScaleS

| Frage | Antwort | Begründung |
|:-----:|:-------:|------------|
| 11.1 | **A** | Flaschenhals = ständiger Datentransport zwischen getrenntem Speicher und CPU. |
| 11.2 | **C** | Physikalisches Modell: Parameter = physikalische Größen; die Schaltung ist das Modell. |
| 11.3 | **B** | BrainScaleS setzt AdEx um. |
| 11.4 | **C** | BrainScaleS ist analog und stark beschleunigt (~1000–10 000×); andere digital. |
| 11.5 | **A** | Hybrid Plasticity: analoge Korrelationsmessung + digitale PPU. |
| 11.6 | **D** | Zwei Klassen: Deep Learning (Backprop) vs. lokale Plastizität (Biologie). |
| 11.7 | **B** | In-Memory: Gewichte lokal am Rechenort (MAC an der Synapse), keine Trennung. |
| 11.8 | **D** | ~10⁶ aus viel höherer Spannungsänderungsrate (V/s) kleiner VLSI-Bauelemente. |
| 11.9 | **C** | Spike-Netze trainierbar via Surrogate Gradients / Backprop-through-time. |
| 11.10 | **C** | Loihi: digital, LIF, programmierbares lokales Lernen, nicht Echtzeit. |
| 11.11 | **C** | Lokale Plastizitätsregeln justieren Parameter selbst („Lernen ersetzt Kalibrieren"). |
| 11.12 | **D** | PPU = digitale SIMD-Einheit, führt Plastizitätsregeln über Gewichte/Struktur/Raten aus. |
