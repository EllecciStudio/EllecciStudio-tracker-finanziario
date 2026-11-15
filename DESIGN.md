# Ellecci Studio · sistema di design (DESIGN.md)

Identità comune di tutte le app di Luigi (Ellecci Studio): **VaultWatch** (tracker finanziario), **Ellecci Trading Studio**, **PlateLog** (palestra), **BandPilot** (bot BTC Con banda), **AltSonar** (radar altcoin). Futuristico ma minimale: nero profondo, pochi pannelli in vetro scuro, un accento per volta, numeri in monospazio, grafici luminosi. Se un progetto ha già un CLAUDE.md con valori diversi, vincono quelli del progetto; le parole di Luigi vincono su tutto.
(Stesso testo della skill `ellecci-design-system`; copia in ogni repository con interfaccia.)

## Principi
- **Il nero è la scena, il colore è l'informazione.** Lo sfondo resta nero; il colore compare solo dove dice qualcosa (su/giù, azione, stato, scelta).
- **Un accento dominante per schermata.** Il verde acqua è l'azione principale; gli altri colori hanno un ruolo fisso e non si usano per decorare.
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
neutro:  "#9AA1AC"                                           · fondo tinta "#15181F"
```
- Verde/rosso **solo** per su/giù, guadagno/perdita, successo/errore: mai come decorazione.
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
Il vetro ha sempre un bordo di 1px e una luce sul lato in alto, mai un alone colorato. Con `prefers-reduced-transparency` si passa a `card-2` pieno.

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
- Raggi: 6px controlli e chip, 10px card, 14px pannelli e finestre, pillola solo per chip e interruttori.
- Bordi 1px `riga`; niente bordo colorato spesso a sinistra delle card.
- Profondità con superfici più chiare (sfondo → card → card-2); ombra solo su ciò che galleggia.
- Telefono prima di tutto: margini laterali 16px, aree toccabili ≥ 44px, zone sicure rispettate.

## Componenti
- **Pulsante principale:** fondo verde, testo `#05070a` 600, raggio 8px, altezza 40–44px; pressione `scale(.97)`.
- **Pulsante secondario:** fondo `card-2`, bordo `riga-forte`. **Tenue:** solo testo, hover `rgba(255,255,255,.04)`.
- **Interruttori a segmenti:** voce attiva con fondo verde tinta e testo verde.
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

## Prima di consegnare
Foto a 390px e 1440px, contrasto, stati vuoto/errore/caricamento, marchio Ellecci presente, niente testi in inglese, nessun colore fuori dal suo ruolo.
