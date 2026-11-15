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
  (oggi `tracker-v3`), altrimenti il telefono può continuare a mostrare la versione vecchia.
- Prima di un push controlla l'app a larghezza telefono (circa 390 px) e il funzionamento offline.

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

## Nuovo stile "kit Ellecci" (anteprima dal 13/11/2026)
Luigi ha rinominato l'app **VaultWatch** e sta provando un nuovo stile (nero minimale come il video "Ember", pannelli in vetro scuro;
interruttore per provare il "vetro chiaro su nero", salvato in localStorage `vw_vetro`). È in `anteprima/index.html`, generata da `index.html`
con lo script del kit: stesse funzioni e stessi dati (stesso login), cambiano solo aspetto, barra laterale sul computer, numero grande del
patrimonio nella Dashboard e grafici con linee luminose. L'anteprima non registra il service worker e il service worker non la mette in cache.
Quando Luigi conferma: rigenerarla da `index.html` aggiornato (le modifiche fatte nel frattempo all'app non devono perdersi), metterla al posto
di `index.html` con i percorsi della radice, togliere `anteprima/`, aumentare `VERSIONE`. Poi lo stesso kit va adattato alle altre app
(Trading Studio, app della palestra, BandPilot, AltSonar).

## Sistema di design
Prima di toccare l'interfaccia leggi `DESIGN.md` (sistema di design comune di Ellecci Studio, 15/11/2026; stesso testo della skill personale
`ellecci-design-system`). Se una regola di questo CLAUDE.md è diversa, vince questo file.
