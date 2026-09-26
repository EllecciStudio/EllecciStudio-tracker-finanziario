# Tracker finanziario · Ellecci Studio

App personale per tenere traccia di entrate, uscite, debiti, crediti, fondo emergenza e investimenti.
Si installa sul telefono come app (Safari → Condividi → Aggiungi a Home) e funziona anche da computer.

## Dove stanno i dati

I dati **non** sono in questo repository. Stanno in un database Supabase privato, protetto da login
e da Row Level Security: ogni account può leggere e modificare solo la propria riga.

Nel codice compaiono l'indirizzo del progetto Supabase e la chiave *publishable*: sono pubblici per
progettazione e da soli non danno accesso a nessun dato. La chiave `service_role`/`secret` non
deve mai finire qui.

## File

- `index.html` — l'app
- `sw.js` — permette di aprire l'app anche senza rete (i dati non vengono messi in cache)
- `manifest.webmanifest`, `icona-*.png` — installazione e icona
- `lib/` — Supabase JS 2.117.2 e Chart.js 4.4.1, inclusi per non dipendere da servizi esterni

Realizzato da Ellecci Studio · © 2026
