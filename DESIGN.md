# Ellecci Studio · sistema di design (DESIGN.md)

Identità comune di tutte le app di Luigi (Ellecci Studio): **VaultWatch** (tracker finanziario), **Ellecci Trading Studio**, **Embrix** (palestra, ex IronLog), **BandPilot** (bot BTC Con banda), **AltSonar** (radar altcoin). Futuristico ma minimale: quasi nero tinto, schede piene e linee sottili, un accento per volta, numeri grandi, grafici chiari (Kit Ellecci 2 dal 21/11/2026). Se un progetto ha già un CLAUDE.md con valori diversi, vincono quelli del progetto; le parole di Luigi vincono su tutto.
(Stesso testo della skill `ellecci-design-system`; copia in ogni repository con interfaccia.)

## Kit Ellecci 2 (dal 21/11/2026, scelta di Luigi: vince sulle regole più sotto)
Molti dettagli del primo kit (luci dietro le schede, vetro ovunque, scritte in maiuscolo distanziate…) sono gli stessi che i modelli di IA mettono in quasi
ogni design: confronto con le regole di Hallmark (secondo cervello, video 124; pagina «Kit Ellecci 2» in `artefatti.md`). Da oggi:
- **Niente luci, aloni, aurora, bagliori** dietro le schede o sul fondo, né fermi né animati; niente ombra colorata «a bagliore» (nemmeno sulla voce attiva della barra).
  Niente sfumature viola-blu, viola-rosa o azzurro su scuro; un colore principale per app, sempre pieno.
- **Fascia in cima con gli archi della C** (scelta di Luigi, 21/11/2026 sera, «vetro sul colore» + «archi della C»): dietro il titolo di ogni pagina una fascia
  in sfumatura di **un solo colore, quello dell'app** (dalla tinta piena a una più scura fino al fondo; ~540 px sul computer, ~430 sul telefono), con **una C grande**
  fatta di 8 archi concentrici fermi aperti a destra: linee sottili, due un po' più spesse, quelle esterne che si assottigliano; sta a destra della fascia, sfumata verso
  il basso, in parte dietro le schede di vetro, che sfocano poco (~8 px) perché la C si veda attenuata (Luigi, 21/11/2026 sera: la C piccola e intera è stata scartata, «bruttissima»). La fascia non segue i dati: è sempre del colore dell'app.
  Esempio funzionante: CycleDial (`.banda` in `index.html`).
- **Vetro smerigliato solo dove dietro c'è colore**: le schede del primo blocco che stanno sopra la fascia e la barra in basso del telefono (che galleggia sopra il contenuto).
  **Contrasto sul vetro**: sopra il colore i grigi del tema scuro non si leggono; dentro le schede di vetro testo secondario, numeri degli assi e link diventano bianco
  attenuato (~82% e ~62%) o una tinta chiara del colore dell'app. Controllare sempre le scritte nelle schede di vetro.
- **Barra in alto fissa sul computer**: un rettangolo di vetro trasparente su tutta la larghezza (compare quando la pagina scorre) con il logo a sinistra e il tema a destra,
  e l'«isola» delle sezioni al centro che quando la pagina scorre diventa anche lei un po' trasparente, con un'ombra leggera. Controllare il contrasto delle voci.
- **Cambio sezione a cerchio dal centro della C** della fascia (non dal punto toccato), lento abbastanza da far vedere da dove nasce (~1,1 s). Le schede sono piene, un gradino più chiare del fondo,
  bordo 1px; nessuna scheda «in vetro colorato». La profondità si fa con fondi più chiari, non con bagliori.
- **Fondo quasi nero tinto** verso il colore dell'app (mai `#000` o `#fff` puri come superficie; i numeri sotto sono OKLCH L 15/19/22/27/32%):

| App | sfondo | card | card-2 | riga | riga-forte |
|---|---|---|---|---|---|
| VaultWatch, Trading Studio (verde) | `#080C0A` | `#101512` | `#171C19` | `#222824` | `#2E3531` |
| CycleDial (azzurro) | `#080C0E` | `#101517` | `#161B1F` | `#21272C` | `#2D3438` |
| BandPilot, Embrix (arancio) | `#0E0A08` | `#171310` | `#1F1916` | `#2B2521` | `#38312D` |
| AltSonar (viola) | `#0B0B0E` | `#141317` | `#1B1A1F` | `#27252C` | `#333238` |
  Tema chiaro: fondo `#F1F4F6` tinto, schede bianche piene con bordo 1px (niente bianco smerigliato).
- **Etichette in testo normale**: niente MAIUSCOLO né spaziatura tra le lettere in etichette, intestazioni di tabella, chip, voci di menu
  (carattere del testo, un gradino più piccolo, colore secondario: «Rischio attuale»). Il maiuscolo resta solo nei loghi.
- **Niente scritta piccola sopra i titoli** che ripete il titolo. Sopra un numero l'etichetta resta (dice cos'è il numero).
- **Niente puntino di mezzo come separatore** (`A · B · C`) né freccia attaccata ai link (`Tutto lo storico ›`): a capo, colonne, virgole; il link è un verbo
  («Apri lo storico»). Nemmeno nel nome dentro l'app (Luigi, 21/11/2026): nome del prodotto e «Ellecci Studio» su due righe. Il puntino resta solo nel nome della finestra e dell'app installata («CycleDial · Ellecci Studio»), finché Luigi non decide altro.
- **Niente riquadro dentro un riquadro**: una nota dentro una scheda si separa con una linea sottile sopra, non con un secondo box.
- **Pillole solo per pulsanti, filtri e la barra**; chip con angoli piccoli (6 px) e nel carattere del testo. Il monospazio solo per i numeri.
- **Solo ciò che si clicca reagisce al mouse** (una scheda che porta a una sezione si solleva; le altre no). Niente pallini che pulsano all'infinito.
- **Il segno nuovo delle app Ellecci**:
  - **numeri protagonisti**: il numero eroe più grande (Unbounded 600, fino a 4–4,5rem sul computer), il resto della scheda calmo intorno;
  - **l'arco della «C» di Ellecci come forma**: quadranti, anelli di avanzamento, bande ad arco dove il dato lo permette (mai come decorazione vuota);
  - **linee sottili al posto dei riquadri**: meno schede chiuse, più righe e colonne separate da filetti 1px (`riga`);
  - **grana finissima sul fondo** (rumore SVG in `body`, opacità 3–5%, ferma), al posto della luce.
- Il movimento «da dashboard» a ogni sezione resta (decisione di Luigi del 16/11/2026), più corto: cascata entro ~0,5 s, numeri che contano ~0,8 s.

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

## Vetro (kit Ellecci, da VaultWatch) — superato dal Kit Ellecci 2: vetro solo sulla barra in basso del telefono, niente alone
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
| etichetta di sezione | 0.8125rem, testo normale (Kit 2) | Plex Sans 500 | 1.3 | 0 |
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
  - **schede che si sollevano** di 3–5 px al passaggio del mouse (solo con puntatore, non sul telefono; dal Kit 2 solo le schede cliccabili).
  Tutto questo **ogni volta che si apre una sezione** (decisione di Luigi del 16/11/2026, vale più della regola sopra sul cambio scheda); non quando i dati
  si aggiornano dentro la sezione già aperta.
  Con "riduci movimento" del sistema: niente conteggi, niente cerchio, solo dissolvenze brevi.
- **Movimento "da trading"** (17/11/2026, riferimento "Orderlume", `riferimenti-design/2026-11-17-movimento-studio-e-trading.md` nel secondo cervello; nel Trading Studio):
  prezzo vivo (scorrono solo le cifre cambiate, lampo verde se sale e rosso se scende), la posizione appena disegnata si costruisce (entrata, poi target e stop, poi le scritte),
  i risultati scorrono dal valore di prima a quello nuovo. Candele e indicatori non si animano. Per le app di studio vale il riferimento "Campus" (stessa nota): anelli, serie di giorni, punti.

## Due temi: vetro scuro e vetro chiaro (dal 20/11/2026, scelta di Luigi) — dal 21/11/2026 senza luce e senza vetro sulle schede (Kit Ellecci 2): restano due temi, scuro tinto e chiaro
Il tema "vetro" (19/11/2026, diverso in ogni app: aurora in VaultWatch, terminale nel Trading Studio, quadrante acceso in BandPilot, sonar in AltSonar)
è diventato il **tema scuro predefinito**; il vecchio scuro senza luce non c'è più. Il chiaro è la **versione chiara dello stesso vetro**: stessa luce dell'app
più tenue su fondo `#F3F4F6`, la scheda principale in vetro colorato chiaro (sfumatura del colore principale al ~13%, bordo del colore al ~22%), le altre schede
bianche smerigliate (`rgba(255,255,255,.72)` + `backdrop-filter: blur(22px)`). Il pulsante del tema passa solo tra i due (sole = vai al chiaro, luna = torna allo scuro);
lo script in `<head>` mette sempre `data-tema="vetro"` oppure `data-tema="chiaro"` (una vecchia scelta "scuro" salvata diventa vetro).
Con "riduci trasparenza" o "riduci movimento" le schede tornano piene e la luce sta ferma, in tutti e due i temi.

## Tema chiaro (a scelta, dal 16/11/2026; dal 20/11/2026 è il "vetro chiaro" qui sopra)
Luigi usa solo il tema scuro, che resta il **predefinito**; il chiaro serve a chi comprerà le app. Ogni app ha un pulsante luna/sole (o "◐ Tema") in testata;
la scelta si salva sul dispositivo (`localStorage`) e uno script in `<head>` mette `data-tema="chiaro"` su `<html>` prima del disegno.
- Fondo `#F3F4F6`, schede bianche con bordo `rgba(15,23,42,.08)` e ombra morbida al posto del vetro; testo `#0E1116`, secondario `#5B6472`.
- Colori più scuri per reggere sul bianco: verde `#0E9F63`, rosso `#D93A2B`, oro `#A8700F`, blu `#1F78B4`, viola `#6E4FC0`, arancio `#E2621F`.
- Pulsante attivo: scuro con testo bianco (il contrario dello scuro). Fumetti dei grafici scuri con testo bianco. Alone dietro la scheda principale più tenue.
- Il logo Ellecci (bianco) si inverte con `filter:invert(1)`.
- Ogni colore scritto a mano (CSS, grafici, canvas) va previsto in entrambi i temi; foto di controllo in tutti e due prima di consegnare.

## Regole fisse dopo la revisione del 17/11/2026
- **Computer**: l'app riempie la finestra (niente colonna stretta al centro con i lati vuoti); sugli schermi larghi i blocchi si affiancano.
- **iPhone**: ogni campo dove si scrive ha testo da **16 px** in su, altrimenti Safari ingrandisce la pagina e non torna indietro.
- **Tendine**: elenco nello stile dell'app (vetro, voce scelta nel colore principale con la spunta), mai il menu grigio del sistema. Modello: VaultWatch (`vw-menu`).
- **Moduli**: campi tutti alti uguali (44 px), `min-width:0` nelle griglie perché nessun campo esca dalla sua casella (la data di iOS lo faceva).
- **Ritmo**: stessa distanza (12–14 px) tra tutti i blocchi, note comprese. Etichette dei grafici dritte, mai inclinate.
- **Elenchi**: nome corto + al massimo una riga di descrizione; i dettagli stanno nelle impostazioni.
- Numeri grandi sempre in Unbounded, in tutte le app.
- **Numeri all'italiana ovunque** (aggiunta del pomeriggio del 17/11/2026): punto delle migliaia anche a 4 cifre (4.380,00 €) e virgola dei decimali,
  anche nelle percentuali (+1,20%), negli assi e nei fumetti dei grafici e nelle date (04/11, non 11-04). Mai fidarsi di `Intl` it-IT da solo: non raggruppa le 4 cifre.
- **Niente emoji come icone** (sull'iPhone diventano grosse e colorate): icone disegnate a tratto sottile, stesso colore del testo.
- **La barra in alto del computer deve stare tutta nello schermo già a 1280 px**: ciò che serve di rado va in un menu o diventa un'icona.
- **Tabelle sul telefono**: se le colonne non ci stanno, ogni riga diventa una scheda (niente importi tagliati a destra).
- **Caratteri dei grafici sempre con riserva** (`'IBM Plex Sans', system-ui, sans-serif`): senza, il canvas usa un carattere con le grazie finché il font non arriva.

## Prima di consegnare
Foto a 390px e 1440px, contrasto, stati vuoto/errore/caricamento, marchio Ellecci presente, niente testi in inglese, nessun colore fuori dal suo ruolo.

## Riferimenti scelti da Luigi
- 15/11/2026, 12 esempi da Pinterest (copie e analisi nel secondo cervello, `riferimenti-design/2026-11-15-pinterest.md`). Confronto A/B/C su VaultWatch: Luigi ha scelto
  un colore principale per app (tabella sopra), **numeri grandi spessi come prima** (Unbounded, niente numeri sottili né a puntini) e tutto il resto dello stile B:
  angoli più tondi, alone di luce dietro la scheda principale, pulsante attivo bianco, barra in basso che galleggia, punto del grafico con fumetto, barre a stanghette.
  Il più vicino allo stile voluto: "Cash Management" (verde menta su nero, area sfumata, fumetto pieno).
