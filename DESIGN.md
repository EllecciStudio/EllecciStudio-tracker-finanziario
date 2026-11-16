# Ellecci Studio · sistema di design (DESIGN.md)

Identità comune di tutte le app di Luigi (Ellecci Studio): **VaultWatch** (tracker finanziario), **Ellecci Trading Studio**, **Embrix** (palestra, ex IronLog), **BandPilot** (bot BTC Con banda), **AltSonar** (radar altcoin). Futuristico ma minimale: nero profondo, pochi pannelli in vetro scuro, un accento per volta, numeri in monospazio, grafici luminosi. Se un progetto ha già un CLAUDE.md con valori diversi, vincono quelli del progetto; le parole di Luigi vincono su tutto.
(Stesso testo della skill `ellecci-design-system`; copia in ogni repository con interfaccia.)

## Principi
- **Il nero è la scena, il colore è l'informazione.** Lo sfondo resta nero; il colore compare solo dove dice qualcosa (su/giù, azione, stato, scelta).
- **Un colore principale per app, uno solo per schermata** (scelta di Luigi del 15/11/2026): verde acqua per VaultWatch e Ellecci Trading Studio, arancio per Embrix e BandPilot, viola per AltSonar. Gli altri colori hanno un ruolo fisso e non si usano per decorare.
- **Grafici prima delle tabelle.** Luigi preferisce vedere l'andamento nel tempo: dove c'è una serie di numeri, prima il grafico, poi il dettaglio.
- **Marchio sempre presente.** Ogni app, pagina o file porta nome e logo "Ellecci Studio"; ogni prodotto ha il suo nome e logo, simili a quello di Ellecci.
- **Tutto in italiano**, testi brevi e concreti; i pulsanti dicono l'azione ("Salva il trade", non "OK").

## Colori
```yaml
sfondo:        "#000000"   # tela
card:          "#0B0D12"   # pannelli pieni
card-2:        "#11141B"   # pannello sopra un pannello, menu, finestre
riga:          "#1A1E27"   # bordi e separatori sottili (1px)
riga-forte:    "#262B36"
inchiostro:    "#E9ECF1"   # testo principale
inchiostro-2:  "#8A93A1"   # testo secondario
inchiostro-3:  "#5C6470"   # note, disattivato
verde:   "#4EDB9C"  # azione principale, positivo, su        · fondo tinta "#0E2A1F"
rosso:   "#FF6A5C"  # negativo, errore, giù, stop             · fondo tinta "#2E1512"
oro:     "#E8B04B"  # attenzione, in evidenza, scelte di Luigi · fondo tinta "#2B2210"
blu:     "#8FD3FF"  # informazione, link, dati neutri          · fondo tinta "#0F2230"
viola:   "#B79BEB"  # speciale (GEX, premium, IA)              · fondo tinta "#1F1A33"
arancio: "#FF7A3D"  # colore principale di Embrix e BandPilot · fondo tinta "#2E1A10"
neutro:  "#9AA1AC"                                           · fondo tinta "#15181F"
```
- Verde/rosso **solo** per su/giù, guadagno/perdita, successo/errore: mai come decorazione (anche nelle app dove il verde è il colore principale: lì il verde dei pulsanti e il verde di "su" sono lo stesso colore, quindi il segno + / − o la freccia ci sono sempre).
- **Colore principale per app** (pulsante principale, voce attiva della barra in basso, linea del grafico principale, alone):

| App | Principale | Note |
|---|---|---|
| VaultWatch (tracker) | verde `#4EDB9C` | |
| Ellecci Trading Studio | verde `#4EDB9C` | |
| Embrix (palestra) | arancio `#FF7A3D` | rosso di errore/calo → `#FF4D6D`, per non confonderlo con l'arancio |
| BandPilot (bot BTC) | arancio `#FF7A3D` | come Embrix; perdite in `#FF4D6D` |
| AltSonar (radar altcoin) | viola `#B79BEB` | il ruolo "speciale" passa al blu |
- Etichette di stato = testo colorato su "fondo tinta" dello stesso colore.
- Contrasto: testo normale ≥ 4,5:1, testo grande e icone ≥ 3:1. Il colore non è mai l'unico segnale (icona, segno + / −, parola).
- Le app sono nere per scelta di Luigi: niente tema chiaro se non lo chiede.

## Vetro (kit Ellecci, da VaultWatch)
Pannelli in vetro solo per gli elementi che galleggiano o vanno in risalto (barra laterale, numero grande del patrimonio, finestre), non per ogni scheda.
```css
/* vetro scuro (predefinito) */
--vetro: rgba(255,255,255,.028); --vetro-forte: rgba(255,255,255,.048);
--vetro-bordo: rgba(255,255,255,.075); --vetro-sfoca: 18px;
/* vetro chiaro su nero (variante) */
--vetro: linear-gradient(160deg, rgba(255,255,255,.14), rgba(255,255,255,.05) 55%, rgba(255,255,255,.08));
--vetro-bordo: rgba(255,255,255,.2); --vetro-sfoca: 30px;
--ombra: 0 14px 40px rgba(0,0,0,.5);
```
Il vetro ha sempre un bordo di 1px e una luce sul lato in alto (bordo più chiaro). Con `prefers-reduced-transparency` o su dispositivi lenti si passa a `card-2` pieno.
**Alone di luce** (dai riferimenti del 15/11/2026): una sola macchia sfocata del colore principale dietro la scheda più importante della schermata (`radial-gradient` del colore a ~35% → trasparente, `filter: blur(28px)`, opacità ~.5, in basso a sinistra della scheda); mai su altre schede, mai dietro al testo lungo. Le schede in risalto possono avere un vetro leggermente sfumato: `linear-gradient(170deg, rgba(255,255,255,.055), rgba(255,255,255,.015))` + bordo `rgba(255,255,255,.07)`.

## Tipografia
- **Unbounded** (500/600): titoli, nomi dei prodotti, numeri grandi. Mai per testi lunghi.
- **IBM Plex Sans** (400/500/600): tutto il testo, pulsanti, etichette.
- **IBM Plex Mono** (400/500): prezzi, percentuali, date, quantità; `font-variant-numeric: tabular-nums` nelle colonne.

| Ruolo | Dimensione | Peso | Interlinea | Spaziatura |
|---|---|---|---|---|
| numero eroe | 2.5–3.5rem (clamp) | Unbounded 600 | 1.0 | -0.02em |
| titolo pagina | 1.5–1.75rem | Unbounded 600 | 1.15 | -0.01em |
| titolo sezione | 1.125rem | Unbounded 500 | 1.25 | 0 |
| corpo | 1rem (min 15px sul telefono) | Plex Sans 400 | 1.55 | 0 |
| piccolo | 0.8125rem | Plex Sans 400 | 1.45 | 0 |
| etichetta di sezione | 0.6875rem MAIUSCOLO | Plex Sans 600 | 1.2 | +0.08em |
| numeri | come il contesto | Plex Mono 500 | — | 0 |

## Spazi, forme, profondità
- Scala da 4: **4 · 8 · 12 · 16 · 24 · 32 · 48 · 64**. Gruppi stretti dentro, separazioni larghe fuori; più spazio sopra un titolo che sotto.
- Raggi (più tondi dal 15/11/2026): 6px controlli piccoli, 16px schede piccole, **24px** schede principali e pannelli, 28px finestre; pillola per pulsanti a segmenti, chip e barra in basso. Disposizione a mattonelle (bento): schede di misure diverse sulla stessa griglia, 12px di spazio tra l'una e l'altra.
- Bordi 1px `riga`; niente bordo colorato spesso a sinistra delle card.
- Profondità con superfici più chiare (sfondo → card → card-2); ombra solo su ciò che galleggia.
- Telefono prima di tutto: margini laterali 16px, aree toccabili ≥ 44px, zone sicure rispettate.

## Componenti
- **Pulsante principale:** fondo del colore principale dell'app, testo `#05070a` 600, raggio 8px, altezza 40–44px; pressione `scale(.97)`.
- **Pulsante secondario:** fondo `card-2`, bordo `riga-forte`. **Tenue:** solo testo, hover `rgba(255,255,255,.04)`.
- **Pulsanti a segmenti** (es. 1M · 3M · 1A · Tutto, Lista / Mappa): pillole con bordo `rgba(255,255,255,.08)`, testo `inchiostro-2`; quella attiva è **bianca piena** (`inchiostro`) con testo nero `#05070a`.
- **Barra in basso sul telefono:** pillola che galleggia a 16px dal fondo (vetro scuro `rgba(20,22,28,.75)` + `backdrop-filter: blur(18px)`, bordo `rgba(255,255,255,.09)`), icone in cerchi da 42px con bordo sottile; la voce principale o attiva è un cerchio pieno del colore principale con bagliore `0 0 18px` dello stesso colore.
- **Card numero:** etichetta in alto, numero grande, variazione con segno colorata, mini grafico sotto.
- **Campi:** fondo `card`, bordo `riga-forte`, focus bordo verde + anello `0 0 0 3px rgba(78,219,156,.18)`.
- **Stati vuoti, caricamento, errore:** sempre disegnati (frase utile + azione).
- Icone: un solo set SVG (tratto 1.5–1.8px), niente emoji al posto delle icone.
- Selezione del testo, barre di scorrimento e anelli di focus con i colori della palette.

## Grafici
- Linea 2px luminosa (bagliore 8–12px dello stesso colore), area sotto con sfumatura a trasparente.
- Su = verde, giù = rosso; più serie: blu, oro, viola, con legenda.
- Griglia `#11151c` solo orizzontale, numeri in Plex Mono, tooltip in vetro scuro, periodo selezionabile (1M · 3M · 1A · Tutto).

## Movimento
- `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)`; 120–160ms pressioni, 150–250ms menu, fino a 400ms finestre.
- Solo `transform` e `opacity`; ingresso da `scale(.96)` + `opacity:0`; niente animazioni su ciò che si usa di continuo; `prefers-reduced-motion` rispettato.
- **Movimento "da dashboard" scelto da Luigi** (16/11/2026, riferimento "Dashboard V15" nel secondo cervello, `riferimenti-design/2026-11-16-movimento-dashboard.md`):
  - **numeri che contano** da 0 al valore in ~0,8–1 s con la curva ease-out (veloci all'inizio, lenti alla fine), cifre in Plex Mono/Unbounded a larghezza fissa;
  - **grafici che si costruiscono**: linea che si disegna da sinistra (`stroke-dashoffset` o animazione di Chart.js), barre che crescono dal basso, archi che si riempiono;
  - **schede a cascata**: `opacity 0 → 1`, `translateY(8px) → 0`, sfocatura `4px → 0`, 40–60 ms tra una scheda e l'altra, poi le righe delle liste;
  - **cambio pagina a cerchio** (`clip-path: circle()` che si allarga dal pulsante toccato), al massimo 350–400 ms;
  - **schede che si sollevano** di 3–5 px al passaggio del mouse (solo con puntatore, non sul telefono).
  Tutto questo solo **la prima volta che si apre una sezione** in una sessione: ai ritorni successivi i numeri sono già al loro posto (la regola sopra resta).
  Con "riduci movimento" del sistema: niente conteggi, niente cerchio, solo dissolvenze brevi.

## Prima di consegnare
Foto a 390px e 1440px, contrasto, stati vuoto/errore/caricamento, marchio Ellecci presente, niente testi in inglese, nessun colore fuori dal suo ruolo.

## Riferimenti scelti da Luigi
- 15/11/2026, 12 esempi da Pinterest (copie e analisi nel secondo cervello, `riferimenti-design/2026-11-15-pinterest.md`). Confronto A/B/C su VaultWatch: Luigi ha scelto
  un colore principale per app (tabella sopra), **numeri grandi spessi come prima** (Unbounded, niente numeri sottili né a puntini) e tutto il resto dello stile B:
  angoli più tondi, alone di luce dietro la scheda principale, pulsante attivo bianco, barra in basso che galleggia, punto del grafico con fumetto, barre a stanghette.
  Il più vicino allo stile voluto: "Cash Management" (verde menta su nero, area sfumata, fumetto pieno).
