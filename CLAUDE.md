# EllecciStudio-tracker-finanziario

Tracker delle finanze personali di Luigi (Ellecci Studio): entrate e uscite, conti, debiti,
crediti, fondo emergenza, investimenti, patrimonio, previsione, simulatore ETF.
È una PWA pubblicata con **GitHub Pages** da questo repository (pubblico) e si installa sull'iPhone
da Safari → Condividi → Aggiungi a Home.

Luigi la sta **testando su se stesso**; l'obiettivo a lungo termine è renderla abbastanza completa
da **venderla**. Luigi non è uno sviluppatore: spiega le modifiche in italiano semplice.

## Regole
- Il repository è **pubblico**: niente dati personali, esportazioni, backup o CSV di transazioni qui dentro.
- In `index.html` stanno solo l'URL Supabase e la chiave *publishable* (pubbliche per progettazione).
  La chiave `service_role`/`secret` **non deve mai** finire nel codice o nel repository.
- Nessun passaggio di build: tutto è in `index.html` (HTML, CSS e JS insieme). Librerie incluse in `lib/`
  (Supabase JS 2.117.2, Chart.js 4.4.1), per non dipendere da CDN.
- Quando cambi i file del "guscio" (index.html, icone, lib), **aumenta `VERSIONE` in `sw.js`**
  (oggi `tracker-v8`), altrimenti il telefono può continuare a mostrare la versione vecchia.
- Prima di un push controlla l'app a larghezza telefono (circa 390 px) e il funzionamento offline.
- Aggiornamenti (16/11/2026): il service worker chiede sempre la pagina alla rete con `cache: 'no-cache'` (GitHub Pages la terrebbe in cache 10 minuti)
  e controlla nuove versioni all'apertura, al ritorno sulla scheda e ogni 30 minuti; quando una nuova versione prende il controllo compare l'avviso
  `#vw-nuova` con "Aggiorna" (niente ricarica automatica, per non perdere un modulo a metà).

## Dati e sincronizzazione
- Supabase, progetto `EllecciStudio-tracker-finanziario` (regione Frankfurt), organizzazione "Ellecci Studio".
- Tabella `tracker_data`: **una riga per utente** (`user_id`, `transactions` JSON, `settings` JSON,
  `updated_at`), protetta da login (email + password) e Row Level Security. Nessuna cifratura lato client.
- `unisci()` fonde le modifiche locali con la versione del server: aggiunte, modifiche e cancellazioni
  locali vincono, il resto arriva dal server. Ogni transazione ha un `id`: non cambiarne il formato.
- Copia locale in `localStorage` (`ellecci_tracker_cache_<user_id>`) per aprire l'app senza rete;
  il service worker non mette mai in cache le risposte di Supabase.
- Backup/esportazione in JSON dalla scheda "Backup" (`versione: 1`): se cambi la struttura dei dati,
  gestisci la migrazione dei backup e delle righe esistenti.

## Schede
dashboard · log · conti · debiti · crediti · fondo · investimenti · patrimonio · previsione · etf · backup

## Stile Ellecci Studio (riusalo anche negli altri progetti)
- Sfondo nero, stile futuristico ma minimale. Colori (`:root`): `--bg #000000`, `--card #0B0D12`,
  `--ink #E9ECF1`, `--ink-soft #8A93A1`, `--line #1A1E27`, `--teal #4EDB9C`, `--gold #E8B04B`,
  `--red #FF6A5C`, `--blue #8FD3FF`, `--purple #B79BEB`.
- Font: Unbounded (titoli), IBM Plex Sans (testo), IBM Plex Mono (numeri).
- Logo: `icona-192.png` / `icona-512.png` (anche incorporato in `index.html` come immagine base64).
  Ogni app, pagina o file deve portare nome e logo "Ellecci Studio".
- Luigi preferisce i **grafici nel tempo** ai soli numeri e tabelle.

## Se diventerà un prodotto da vendere
Servirà ripensare: account multipli e onboarding, pagamenti (su iPhone di norma acquisti in-app Apple),
privacy/GDPR per dati finanziari di altre persone, backup e supporto. Per la pubblicazione sugli store
Luigi ha salvato come riferimento un corso su React Native + Expo + Supabase.

## Stile "kit Ellecci" (nell'app dal 15/11/2026)
Luigi ha rinominato l'app **VaultWatch** e il 15/11/2026 ha messo il nuovo stile al posto di quello vecchio ("anche se ci sono modifiche da fare,
le vediamo nei prossimi giorni"). Segue `DESIGN.md`: solo vetro scuro, colore principale verde, angoli 16/24 px, alone verde dietro il patrimonio,
pulsanti attivi bianchi, pulsante principale verde; sul telefono barra in basso a pillola con Dashboard / Transazioni / + (apre Transazioni sul
campo Importo) / Conti / Altro (pannello con tutte le sezioni), sul computer barra laterale; nei grafici a linea punto evidenziato sull'ultimo
valore con fumetto chiaro.
- Il kit è già dentro `index.html` (blocco `<style id="vw-kit">` e script della barra): **i ritocchi si fanno direttamente in `index.html`**.
  Non rilanciare `strumenti/kit-ellecci/genera.py` su `index.html` (applicherebbe il kit due volte): quello script e `kit.css` restano come
  riferimento per portare lo stesso stile nelle altre app (Trading Studio, Embrix, BandPilot, AltSonar).
- **Movimento** (16/11/2026, regole in `DESIGN.md` > Movimento): blocco "MOVIMENTO" in fondo allo script principale di `index.html` + CSS `vw-entra`/`vw-cerchio`.
  Ogni volta che si apre una sezione (scelta di Luigi, 16/11/2026; non quando i dati si aggiornano nella sezione aperta): schede a cascata, numeri `.hero-val`/`.kpi-val`/`.disp` che contano da 0, grafici a linea che si disegnano quando
  arrivano sullo schermo; cambio pagina a cerchio (View Transitions) dal punto toccato; schede che si sollevano col mouse. `renderAll` è avvolta per far
  continuare l'animazione se i dati arrivano a metà. Con "riduci movimento" del sistema non parte nulla.
- **Tema chiaro** (16/11/2026, richiesta di Luigi per quando le app saranno in vendita): predefinito **scuro**; pulsante luna/sole accanto a "Esci"
  (`#vw-tema`), scelta salvata in `localStorage` `vw_tema` e applicata da uno script in `<head>` prima del disegno. Colori in `<style id="vw-chiaro">`
  (`html[data-tema="chiaro"]`), grafici con `COLORS_SCURO`/`COLORS_CHIARO` + `vwApplicaTemaGrafici()`. Ogni nuovo colore scritto a mano va previsto anche lì.
- La versione prima del kit è nel commit precedente a quello del 15/11/2026 ("VaultWatch: nuovo stile…"), se servisse tornare indietro.

## Sistema di design
Prima di toccare l'interfaccia leggi `DESIGN.md` (sistema di design comune di Ellecci Studio, 15/11/2026; stesso testo della skill personale
`ellecci-design-system`). Se una regola di questo CLAUDE.md è diversa, vince questo file.
