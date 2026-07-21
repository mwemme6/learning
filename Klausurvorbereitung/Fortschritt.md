# Lernfortschritt — Brain-Inspired Computing

Legende: 🟢 sitzt · 🟡 wackelig · 🔴 wiederholen · ⬜ noch nicht geübt

> Wird von Claude nach jeder Abfrage-Session aktualisiert. Siehe `CLAUDE.md`.

| # | Thema | Status | Zuletzt geübt | Notizen |
|---|-------|:------:|---------------|---------|
| 01 | Einführung: Neuron vs. Computer, Membran, Ruhepotential, RC-Modell | 🟡 | 2026-07-20 | Von-Neumann-Flaschenhals & in-memory computing sitzt gut. RC-Modell, GHK, Tau-m verstanden. Wiederholen: dynamisches Gleichgewicht (Pumpe-Diffusion-Gleichgewicht), genaue Abgrenzung Nernst vs. GHK, Neuron-Doktrin. |
| 02 | Aktionspotential & Hodgkin-Huxley-Modell | 🟢 | 2026-07-20 | MC 10 von 11 richtig. Freitext-Fragen alle gut: positive Rückkopplung verstanden, m und h Gating, absolute und relative Refraktärzeit, post-inhibitorischer Rebound-Spike, f-I-Kurve Typ II, Rheobase als Typ-II-Eigenschaft. Voltage-Clamp komplett rausgenommen (nicht klausurrelevant). |
| 03 | LIF-Modell & 2D-Neuronmodelle | 🟡 wackelig | 2026-07-20 | MC 9 von 10 richtig (3.4 BrainScaleS außer Wertung, 3.5 falsch: Typ-I-Verwirrung geklärt). Freitext-Fragen 1-6 durchgearbeitet: Feuerrate und Gleichgewichtspotenzial gut verstanden, Aktivierungsfunktion und Sättigung durch Refraktärzeit klar, HH vs. LIF Unterschiede erfasst (Typ II vs. I, Rebound-Fähigkeit), Ein-/Ausgang elektrisch getrennt verstanden (digitales vs. analoges Signal), Omega und 2D-Reduktion nachvollzogen, relative vs. absolute Refraktärzeit differenziert. Frage 7 (Erweiterungsmodelle) als nicht prüfungsrelevant markiert. Frage 8 (Verlust relative Refraktärzeit) gut erklärt. Gating-Variablen (m, h, n) beim HH-Modell noch einmal geklärt. |
| 04 | Synapsen & synaptische Übertragung | 🟡 wackelig | 2026-07-21 | MC 9 von 10 richtig (4.4 saltatorische Leitung als nicht klausurrelevant übersprungen; 4.7 falsch: AMPA vs. NMDA verwechselt — AMPA ist die schnelle/häufigste exzitatorische Synapse, NMDA ist langsamer/spannungsabhängig). Rest sitzt gut: Transmitterfreisetzung/Ca²⁺, EPSP/IPSP über E_syn, NMDA-Koinzidenzdetektor, Gap Junctions, Shunting Inhibition, stochastische Vesikelfreisetzung, Dale's principle. Freitext-Fragen noch offen. Wiederholen: AMPA vs. NMDA klar trennen (Geschwindigkeit/Häufigkeit).|
| 05 | Synapsenmodelle: COBA/CUBA, exp. Synapsen, High-Conductance-State | 🟡 wackelig | 2026-07-21 | MC 7 von 10 richtig. Gut: COBA/CUBA-Grundunterschied (Leitwert vs. Strom, spannungsabhängig vs. nicht), Triebkraft-Argument (u−E<sub>exc</sub>), CUBA-Gefahr unphysikalischer Depolarisation, Difference-of-Exponentials (endliche Anstiegszeit), τ<sub>eff</sub>-Verkürzung bei COBA. Fehler: 5.3 + 5.6 Alpha-Funktion vs. single-exp-Kernel verwechselt (single-exp = sprunghafter Anstieg + exp. Abfall; Alpha = glatter Anstieg, Grenzfall der DoE, nicht spannungsabhängig); 5.8 High-Conductance-State funktional falsch zugeordnet (Neuron wird schneller Koinzidenzdetektor, NICHT langsamer Integrator). Freitext-Fragen noch offen. Wiederholen: Kernel-Formen (single-exp/DoE/Alpha) sauber unterscheiden; HCS-Funktionswandel (Integrator→Koinzidenzdetektor) festigen.|
| 06 | Statistik von Spike-Trains: Poisson, ISI, CV, PSTH | 🟡 wackelig | 2026-07-21 | MC 9 von 11 richtig. Gut: ISI-Verteilung (exponentiell, Maximum bei s=0), CV-Definition und Interpretation (=1 Poisson, <1 regelmäßiger/Refraktärzeit, ≈0 periodisch), Fano-Faktor, PSTH, „gedächtnislos", Top-down vs. Bottom-up. Fehler: 6.1 + 6.9 derselbe Kernpunkt verwechselt — beim Poisson-Prozess gilt ⟨N⟩ = Var(N) = νT, und genau das Produkt M·p = νT wird beim Grenzübergang Binomial→Poisson konstant gehalten. Freitext-Fragen noch offen. Wiederholen: Mittelwert=Varianz=νT beim Poisson-Prozess und der Binomial→Poisson-Grenzübergang.|
| 07 | Korrelationen, Renewal-Prozess, Power-Spektrum, STA | 🟡 wackelig | 2026-07-21 | Session vorzeitig beendet: nur MC 7.1–7.7 bearbeitet, davon 4/4 beantwortete richtig (7.1 Grenzprozess/unendliche Energie, 7.3 Renewal vs. Poisson via LIF-Reset, 7.4 STA-Definition, 7.5 Renewal-Dichte m(τ)). 7.2 (Wiener-Chintschin) und 7.6 (ACF-Symmetrie) als nicht klausurrelevant markiert. **MC 7.7–7.11 sowie alle Freitext-Fragen noch offen** — nächste Session hier fortsetzen.|
| 08 | Neuronale Codes & Feed-Forward-Netze, Turing-Vollständigkeit | ⬜ | – | |
| 09 | Tuning-Kurven, Netzdynamik, Winner-Takes-All | ⬜ | – | |
| 10 | Plastizität: STP (Tsodyks-Markram), LTP/LTD, STDP | ⬜ | – | |
| 11 | Neuromorphe Hardware & BrainScaleS | ⬜ | – | |

## Session-Log
_(neuste_zuerst)
- 2026-07-21, Sprach-Session mit Claude — Kapitel 7 (Korrelationen, Renewal, PSD, STA), MC-Fragen 7.1-7.7 angefangen, Session vorzeitig beendet. 4/4 beantwortete richtig (7.2, 7.6 als nicht klausurrelevant markiert). MC 7.7-7.11 und Freitext-Fragen offen für nächstes Mal.
- 2026-07-21, Sprach-Session mit Claude — Kapitel 6 (Statistik von Spike-Trains: Poisson, ISI, CV, PSTH), MC-Fragen. 9/11 richtig. Fehler bei ⟨N⟩=Var(N)=νT und dem Binomial→Poisson-Grenzübergang (6.1, 6.9 — derselbe Kernpunkt). Freitext-Fragen noch offen.
- 2026-07-21, Sprach-Session mit Claude — Kapitel 5 (Synapsenmodelle COBA/CUBA, High-Conductance-State), MC-Fragen. 7/10 richtig. Fehler bei Kernel-Formen (Alpha vs. single-exp, 5.3+5.6) und HCS-Funktionswandel (5.8, Integrator vs. Koinzidenzdetektor). Freitext-Fragen noch offen.
- 2026-07-21, Sprach-Session mit Claude — Kapitel 4 (Synapsen & synaptische Übertragung), MC-Fragen. 9/10 richtig (4.4 übersprungen als nicht klausurrelevant, 4.7 AMPA/NMDA-Verwechslung korrigiert). Freitext-Fragen noch offen für nächste Session.
- 2026-07-20, Sprach-Session mit Claude — Kapitel 3 (LIF & 2D-Modelle) durchgearbeitet. Freitext-Fragen 1-8 besprochen. Starke Verbesserung bei Verständnis von Gleichgewichtspotenzial, Aktivierungsfunktion, HH vs. LIF, digitale Spike-Representation, Adaptation/Rebound, 2D-Reduktion (m instantan, n+h→omega), und Refraktärzeiten. Frage 7 aus Priorisierung herausgenommen. Gating-Variablen des HH-Modells geklärt.
- 2026-07-20, Sprach-Session mit Claude — Kapitel 2 durchgearbeitet. MC-Fragen übersprungen (bereits 10/11 richtig, nur 2.8 wiederholt). Freitext-Fragen: alle 5 Fragen gut beantwortet (positive Rückkopplung, m/h-Gating, Refraktärzeiten, Rebound-Spike, f-I-Kurve Typ II, Rheobase). Voltage-Clamp aus Priorisierung rausgenommen.
- **_(noch keine Session)_** — Material erstellt am 2026-07-20.
- 2026-07-20, Sprach-Session mit Claude — Kapitel 1 durchgearbeitet. MC-Fragen übersprungen (bereits bearbeitet). Freitext-Fragen: 5 von 8 gut beantwortet (Fragen 1, 3, 4, 6, 7). Fragen 2, 5, 8 wiederholen.


## Priorität für Wiederholung
_(Claude trägt hier die 🔴/🟡-Themen ein)_
- Kapitel 4: AMPA vs. NMDA klar trennen (AMPA = schnell/häufig, NMDA = langsam/spannungsabh.); Freitext-Fragen noch nachholen.
- Kapitel 5: Kernel-Formen sauber trennen (single-exp = Sprung+Abfall; DoE = Anstieg+Abfall; Alpha = Grenzfall der DoE, glatt, symmetrisch); HCS macht Neuron zum schnellen Koinzidenzdetektor (nicht langsamen Integrator). Freitext-Fragen noch nachholen.
- Kapitel 6: ⟨N⟩ = Var(N) = νT beim Poisson-Prozess festigen; Binomial→Poisson-Grenzübergang (M·p = νT konstant halten) verinnerlichen. Freitext-Fragen noch nachholen.
- Kapitel 7: MC 7.7–7.11 noch nachholen (STA-Grenzen, White-Noise-Stimulus, PSD aus ISI-Verteilung), danach Freitext-Fragen.
