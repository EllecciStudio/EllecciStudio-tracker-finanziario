/* Tracker finanziario · Ellecci Studio — service worker
   L'app si apre anche senza rete; i dati passano sempre da Supabase e non vengono messi in cache qui. */
const VERSIONE = 'tracker-v1';
const GUSCIO = ['./', 'index.html', 'manifest.webmanifest', 'icona-180.png', 'icona-192.png', 'icona-512.png', 'lib/chart.umd.js', 'lib/supabase.js'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSIONE).then(c => c.addAll(GUSCIO)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(chiavi => Promise.all(chiavi.filter(k => k !== VERSIONE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // Font Google: usa la copia salvata e aggiornala in background
  if (url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com') {
    e.respondWith(caches.open(VERSIONE).then(async c => {
      const salvata = await c.match(req);
      const rete = fetch(req).then(r => { if (r.ok || r.type === 'opaque') c.put(req, r.clone()); return r; }).catch(() => salvata);
      return salvata || rete;
    }));
    return;
  }

  // Tutto il resto fuori dal sito (Supabase compreso) va sempre in rete, mai in cache
  if (url.origin !== self.location.origin) return;

  // Pagina: prima la rete (così ricevi gli aggiornamenti), se manca la rete la copia salvata
  if (req.mode === 'navigate' || url.pathname.endsWith('/') || url.pathname.endsWith('index.html')) {
    e.respondWith(fetch(req).then(r => {
      const copia = r.clone();
      caches.open(VERSIONE).then(c => c.put('index.html', copia));
      return r;
    }).catch(() => caches.match('index.html')));
    return;
  }

  // Librerie e icone: prima la copia salvata
  e.respondWith(caches.match(req).then(salvata => salvata || fetch(req)));
});
