# 04 · Synapsen & synaptische Übertragung

<p class="sub">Brain-Inspired Computing · Vorlesung 4 · ausführliche Zusammenfassung</p>

## 1 · Signalweiterleitung am Axon

Das am Axonhügel ausgelöste Aktionspotential (AP) muss über das (bis **>1 m** lange) Axon
zu den Terminalen gelangen. Die Ausbreitung ist **aktiv und nicht-dekrementell**: An jeder
Stelle öffnen die lokale Depolarisation spannungsgesteuerte **Na⁺-Kanäle** (HH, L2), die
das Signal **regenerieren** — es klingt also nicht ab (anders als eine passive Kabel-
ausbreitung, die exponentiell dämpfen würde).

### 1.1 · Myelin & saltatorische Leitung

- Die **Myelinscheide** (gebildet von Schwann-Zellen im PNS bzw. Oligodendrocyten im ZNS)
  **isoliert** das Axon abschnittsweise und erhöht den Membranwiderstand / senkt die
  Kapazität.
- Nur an den **Ranvier-Schnürringen** ist die Membran frei und mit Na⁺-Kanälen dicht besetzt.
- → **saltatorische Leitung**: Das AP „springt" von Schnürring zu Schnürring. Vorteile:
  **deutlich schneller** (bis ~100 m/s) und **energieeffizienter** (weniger Membranfläche
  muss umgeladen werden).

## 2 · Die chemische Synapse — Ablauf

Am Axonterminal wird das **elektrische** Signal in ein **chemisches** übersetzt und wieder
zurück. Ablauf (auswendig können!):

1. **AP erreicht das präsynaptische Terminal.**
2. Öffnung **spannungsgesteuerter Ca²⁺-Kanäle** → **Ca²⁺-Einstrom** in die Präsynapse.
3. Ca²⁺ löst die **Fusion synaptischer Vesikel** mit der präsynaptischen Membran aus →
   **Neurotransmitter** werden in den **synaptischen Spalt** ausgeschüttet (Exozytose).
   **Wichtig:** Die Vesikelfreisetzung ist **stochastisch/unzuverlässig** (probabilistisch).
4. Transmitter **diffundieren** über den Spalt und binden an **Rezeptoren** der
   postsynaptischen Membran.
5. **Ligandengesteuerte Ionenkanäle öffnen** → postsynaptischer **Ionenstrom** ändert das
   Membranpotential (PSP).
6. **Beendigung:** Transmitter werden **wiederaufgenommen** (Reuptake) oder **enzymatisch
   abgebaut** → Kanäle schließen, der Strom klingt ab.

Synapsendichte: viele tausend Synapsen pro Neuron → hoher Fan-in. Die probabilistische
Freisetzung ist funktional relevant (Rauschquelle, Grundlage der Kurzzeitplastizität L10).

::: ref
**Verweise:** Folie L4 „chemical synapse", „synaptic transmission" (MPG-Animation
mpg.de/synapse). Literatur: Dayan & Abbott, Kap. 5.7–5.8; Gerstner et al., *Neuronal
Dynamics*, Kap. 3.1.
:::

## 3 · Erregung & Hemmung: EPSP / IPSP

Ob eine Synapse erregend oder hemmend wirkt, hängt **allein vom Umkehrpotential
E<sub>syn</sub>** des geöffneten Kanals relativ zur Schwelle/zum Ruhepotential ab — **nicht**
vom Transmitter an sich:

- **EPSP** (exzitatorisches postsyn. Potential): E<sub>syn</sub> **über** dem Ruhe-/
  Schwellpotential (z. B. ~0 mV, Na⁺/K⁺) → **depolarisierend**, treibt das Neuron **zum
  Feuern**.
- **IPSP** (inhibitorisches postsyn. Potential): E<sub>syn</sub> **unter** dem Ruhepotential
  (z. B. −70 mV, Cl⁻) → **hyperpolarisierend** oder **shunting** (Kurzschluss über den
  erhöhten Leitwert), **hemmt** das Feuern.

**Shunting inhibition:** Selbst wenn E<sub>syn</sub> ≈ E<sub>L</sub> (kaum Spannungs-
änderung), erhöht die offene inhibitorische Leitfähigkeit den Gesamtleitwert und
„verkürzt" damit EPSPs (teilt den Strom ab) → wirksame Hemmung ohne Hyperpolarisation.

**Integration:** Ein Neuron summiert viele EPSPs/IPSPs in **Raum** (verschiedene Dendriten)
und **Zeit**. Überschreitet die Summe die Schwelle, entsteht ein Spike → das Neuron ist ein
räumlich-zeitlicher **Koinzidenzdetektor** (L11).

## 4 · Wichtige Synapsentypen

| Rezeptor | Transmitter | Ionen | E<sub>rev</sub> | τ<sub>open</sub> | Bemerkung |
|----------|-------------|-------|-----------------|------------------|-----------|
| **AMPA** | Glutamat | Na⁺, K⁺, (Ca²⁺) | ≈ 0 mV | ≈ 1–2 ms | häufigste **exzitatorische** Synapse; schnell |
| **NMDA** | Glutamat | Na⁺, K⁺, Ca²⁺ | ≈ 0 mV | ≈ 20 ms | **spannungsabhängig** (Mg²⁺-Block), langsam, **Koinzidenzdetektor**, Ca²⁺-Einstrom |
| **GABA_A** | GABA | Cl⁻ | ≈ −70 mV | ≈ 5 ms | häufigste **inhibitorische** Synapse |
| **Ach** (nikotin.) | Acetylcholin | Na⁺, K⁺ | – | ≈ 1 ms | Motoneuron → Muskelkontraktion (neuromuskuläre Endplatte) |

Abkürzungen: AMPA = α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid; NMDA =
N-methyl-D-aspartat; GABA = γ-Aminobuttersäure.

**Der NMDA-Rezeptor** ist besonders: Er leitet nur, wenn **gleichzeitig** (1) Glutamat
präsynaptisch gebunden ist **und** (2) die Postsynapse ausreichend **depolarisiert** ist
(die Depolarisation löst den **Mg²⁺-Block** im Kanal). Damit ist er ein molekularer
**Koinzidenzdetektor** von Prä- und Postaktivität und der zentrale Baustein für Lernen/
Plastizität (L10). Seine lange Zeitkonstante (~20 ms) macht ihn zudem zu einem
Integrator über längere Zeitfenster.

## 5 · Elektrische Synapsen (Gap Junctions)

Neben chemischen gibt es **elektrische Synapsen** (Gap Junctions): direkte, von
Connexinen gebildete Kanäle, die das Zytoplasma zweier Zellen verbinden.

- **sehr schnell**, praktisch **verzögerungsfrei**, **bidirektional**.
- keine Transmitter, keine Verstärkung.
- Funktion v. a. **Synchronisation** von Neuronenpopulationen (z. B. schnelle Oszillationen).
- Nachteile: kaum **Plastizität**, keine Vorzeichenumkehr (nur elektrische Kopplung),
  wenig rechnerische Flexibilität.

<div class="keybox">
<strong>Kernbotschaften L4:</strong> Axon leitet aktiv/regenerativ; Myelin + Ranvier →
schnelle, effiziente saltatorische Leitung. Chemische Synapse: AP → Ca²⁺-Einstrom →
Vesikel/Transmitter (stochastisch!) → Rezeptor → postsyn. Strom → Reuptake/Abbau.
EPSP (depol.) vs. IPSP (hyperpol./shunt), bestimmt allein durch E<sub>syn</sub>.
Typen: AMPA (schnell exz.), NMDA (langsam, spannungsabh., Ca²⁺-Koinzidenzdetektor),
GABA_A (inh., Cl⁻), Ach (Muskel). Elektrische Synapsen: schnell, bidirektional,
synchronisierend, aber kaum plastisch.
</div>

---

## Multiple-Choice-Fragen (Lösungen in `Loesungen_MC.pdf`)

::: mc
**MC 4.1** — Was löst die Transmitterfreisetzung im präsynaptischen Terminal unmittelbar aus?

A) Ca²⁺-Einstrom durch spannungsgesteuerte Kanäle
B) das Schließen der Na⁺-Kanäle
C) K⁺-Ausstrom
D) Cl⁻-Einstrom
:::

::: mc
**MC 4.2** — Eine Synapse mit E<sub>rev</sub> ≈ −70 mV (Cl⁻) wirkt typischerweise …

A) als elektrische Synapse
B) gar nicht auf das Potential
C) stark exzitatorisch
D) inhibitorisch/hyperpolarisierend (GABA_A)
:::

::: mc
**MC 4.3** — Warum gilt der NMDA-Rezeptor als Koinzidenzdetektor?

A) Er ist eine elektrische Synapse.
B) Er ist besonders schnell.
C) Er leitet nur bei gleichzeitig präsyn. Glutamat **und** ausreichender postsyn. Depolarisation (Mg²⁺-Block gelöst).
D) Er reagiert nur auf Cl⁻.
:::

::: mc
**MC 4.4** — Welche Aussage zur saltatorischen Leitung ist korrekt?

A) Sie funktioniert nur ganz ohne Ionenkanäle.
B) Myelin isoliert; das AP „springt" zwischen Ranvier-Schnürringen → schneller und effizienter.
C) Das AP wird zwischen den Schnürringen aktiv regeneriert und dabei langsamer.
D) Elektrische Synapsen sind dafür verantwortlich.
:::

::: mc
**MC 4.5** — Ein Merkmal **elektrischer** Synapsen (Gap Junctions) ist:

A) chemische Transmitter im Spalt
B) langsame, unidirektionale Übertragung
C) schnelle, bidirektionale Kopplung, gut zur Synchronisation
D) starke Langzeitplastizität und Signalverstärkung
:::

::: mc
**MC 4.6** — Wodurch entscheidet sich, ob eine Synapse erregend oder hemmend wirkt?

A) durch den Transmitter allein
B) durch das Umkehrpotential E<sub>syn</sub> relativ zu Ruhe-/Schwellpotential
C) durch die Membrankapazität
D) durch die Länge des Axons
:::

::: mc
**MC 4.7** — Welche Synapse ist die **schnellste, häufigste exzitatorische** im Cortex?

A) AMPA
B) GABA_A
C) Gap Junction
D) NMDA
:::

::: mc
**MC 4.8** — „Shunting inhibition" bedeutet …

A) eine Form der elektrischen Synapse.
B) Verstärkung von EPSPs.
C) Hemmung durch erhöhten Leitwert (Stromabzweig), auch wenn E<sub>syn</sub> ≈ E<sub>L</sub> und kaum Spannungsänderung entsteht.
D) starke Hyperpolarisation weit unter E<sub>L</sub>.
:::

::: mc
**MC 4.9** — Die Vesikelfreisetzung an chemischen Synapsen ist …

A) stochastisch/probabilistisch (unzuverlässig).
B) exakt deterministisch bei jedem AP.
C) nur bei elektrischen Synapsen vorhanden.
D) unabhängig von Ca²⁺.
:::

::: mc
**MC 4.10** — Welcher Rezeptor hat die **längste** Zeitkonstante (~20 ms) und leitet Ca²⁺?

A) NMDA
B) GABA_A
C) Ach
D) AMPA
:::

## Freitext-Fragen (zum Besprechen)

1. Beschreibe die chemische synaptische Übertragung Schritt für Schritt (AP → Ca²⁺ →
   Vesikel → Rezeptor → PSP → Beendigung). An welchen Stellen ist sie stochastisch und
   warum ist das funktional relevant?
2. Erkläre saltatorische Leitung und den Beitrag von Myelin/Ranvier. Wie hängt sie mit den
   HH-Kanälen aus L2 zusammen?
3. Wodurch entscheidet sich EPSP vs. IPSP? Erkläre „shunting inhibition" und warum Hemmung
   nicht immer Hyperpolarisation bedeutet.
4. Vergleiche AMPA und NMDA hinsichtlich Kinetik, Ionen, Spannungsabhängigkeit und
   Funktion. Warum ist NMDA für Lernen (L10) so zentral?
5. Erkläre den Mg²⁺-Block des NMDA-Rezeptors und wie er die Koinzidenzdetektion
   mechanistisch realisiert.
6. Vergleiche chemische und elektrische Synapsen entlang der Achsen Geschwindigkeit,
   Richtung, Plastizität und Rechenleistung.
7. Warum ist die räumlich-zeitliche Integration vieler EPSPs/IPSPs die Grundlage der
   Koinzidenzdetektion? Verknüpfe mit τ<sub>m</sub> (L1).
