"""Applica il kit Ellecci (pilota VaultWatch) a una copia di index.html.
Uso: python3 genera.py <index.html sorgente> <uscita> <percorso relativo della radice: '' oppure '../'>"""
import re, sys, pathlib

src, out, radice = sys.argv[1], sys.argv[2], sys.argv[3]
h = pathlib.Path(src).read_text(encoding='utf-8')
kit = pathlib.Path(__file__).with_name('kit.css').read_text(encoding='utf-8')


def sost(vecchio, nuovo, conta=1):
    global h
    n = h.count(vecchio)
    if n != conta:
        raise SystemExit(f'atteso {conta} volte, trovato {n}: {vecchio[:80]!r}')
    h = h.replace(vecchio, nuovo)


# --- percorsi (solo per l'anteprima in una sottocartella) ---
if radice:
    sost('href="manifest.webmanifest"', f'href="{radice}manifest.webmanifest"')
    sost('href="icona-180.png"', f'href="{radice}icona-180.png"')
    sost('href="icona-192.png"', f'href="{radice}icona-192.png"')
    sost('src="lib/chart.umd.js"', f'src="{radice}lib/chart.umd.js"')
    sost('src="lib/supabase.js"', f'src="{radice}lib/supabase.js"')
    # l'anteprima non registra il service worker (lo fa già l'app principale)
    h = re.sub(r"<script>\s*if\('serviceWorker' in navigator\)\{.*?</script>\s*", '', h, flags=re.S)
    sost('<title>Tracker finanziario · Ellecci Studio</title>', '<title>VaultWatch · anteprima · Ellecci Studio</title>')
else:
    sost('<title>Tracker finanziario · Ellecci Studio</title>', '<title>VaultWatch · Ellecci Studio</title>')

sost('family=IBM+Plex+Mono:wght@500;600', 'family=IBM+Plex+Mono:wght@400;500;600')

# --- accesso ---
m = re.search(r'(<main id="accesso"[^>]*>\s*)(<img class="logo"[^>]*>)\s*<div class="firma">Ellecci Studio</div>\s*<h1 id="acc-titolo">Tracker finanziario</h1>', h)
assert m, 'accesso'
h = h[:m.start()] + m.group(1) + '<div class="acc-vetro vw-vetro">\n  ' + m.group(2) + \
    '\n  <div class="firma">Ellecci Studio</div>\n  <h1 id="acc-titolo">Vault<span>Watch</span></h1>' + h[m.end():]
sost('  <div id="accesso-errore" role="alert"></div>\n</main>', '  <div id="accesso-errore" role="alert"></div>\n  </div>\n</main>')

# --- kit CSS dopo i due blocchi di stile esistenti ---
sost('<div id="ft-root" class="hidden">', kit + '\n<div id="ft-root" class="hidden">')

# --- intestazione + schede → barra laterale ---
i = h.index('  <div class="app-header">')
j = h.index('  <div class="tab-panel active" id="panel-dashboard"></div>')
vecchio = h[i:j]
logo = re.search(r'<img src="data:image/png;base64,[^"]+"[^>]*>', vecchio).group(0)
schede = re.search(r'(<div class="tabs" id="ft-tabs">)(.*?)(</div>)', vecchio, re.S)
nuovo = f'''  <aside class="lato vw-vetro">
    <div class="app-header">
      <div class="marchio">
        {logo}
        <div>
          <h1 class="wordmark">Vault<span>Watch</span></h1>
          <div class="occhiello">Ellecci Studio</div>
        </div>
      </div>
      <div class="stato-righe">
        <div class="app-sub" id="ft-lastupdate">Caricamento...</div>
        <div class="app-sub" id="ft-syncstatus"></div>
      </div>
    </div>

    <nav class="tabs vw-vetro" id="ft-tabs" aria-label="Sezioni">{schede.group(2)}</nav>

    <div class="lato-piede">
      <span class="save-flag" id="ft-saveflag" role="status" aria-live="polite">Salvato</span>
      <div class="bottoni">
        <button class="btn-esci" id="ft-esci" type="button">Esci</button>
      </div>
    </div>
  </aside>

  <div class="contenuto">
  <div class="testata">
    <div><div class="occhiello">VaultWatch</div><h2 id="vw-titolo">Dashboard</h2></div>
    <div class="testata-data num" id="vw-data"></div>
  </div>
'''
h = h[:i] + nuovo + h[j:]
# chiudi .contenuto dopo la firma in fondo
k = h.index('<div class="firma-piede">')
# la firma è una sola riga: <div class="firma-piede"><img ...>…</div>
riga_fine = h.index('\n', k)
ICO = {
    'casa': '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    'lista': '<path d="M8 6h13M8 12h13M8 18h13"/><circle cx="3.5" cy="6" r="1"/><circle cx="3.5" cy="12" r="1"/><circle cx="3.5" cy="18" r="1"/>',
    'piu': '<path d="M12 5v14M5 12h14"/>',
    'conti': '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h3"/>',
    'altro': '<rect x="4" y="4" width="6" height="6" rx="1.5"/><rect x="14" y="4" width="6" height="6" rx="1.5"/><rect x="4" y="14" width="6" height="6" rx="1.5"/><rect x="14" y="14" width="6" height="6" rx="1.5"/>',
}
def ico(k):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICO[k]}</svg>'
barra = f'''
  <nav class="barra-basso vw-vetro" id="vw-barra" aria-label="Sezioni principali">
    <button type="button" data-vai="dashboard" aria-label="Dashboard" title="Dashboard">{ico('casa')}</button>
    <button type="button" data-vai="log" aria-label="Transazioni" title="Transazioni">{ico('lista')}</button>
    <button type="button" class="principale" data-vai="nuova" aria-label="Aggiungi una transazione" title="Aggiungi una transazione">{ico('piu')}</button>
    <button type="button" data-vai="conti" aria-label="Conti" title="Conti">{ico('conti')}</button>
    <button type="button" data-vai="altro" aria-label="Altre sezioni" title="Altre sezioni" aria-expanded="false" aria-controls="ft-tabs">{ico('altro')}</button>
  </nav>'''
h = h[:riga_fine] + '\n  </div>' + barra + h[riga_fine:]

# --- grafici: stile, bagliore sulle linee, riempimento sfumato ---
sost("""if(typeof Chart !== 'undefined'){
  Chart.defaults.color = '#8A93A1';
  Chart.defaults.borderColor = '#1A1E27';
  Chart.defaults.font.family = "'IBM Plex Sans', sans-serif";
}""", """if(typeof Chart !== 'undefined'){
  Chart.defaults.color = '#8A93A1';
  Chart.defaults.borderColor = 'rgba(255,255,255,0.05)';
  Chart.defaults.font.family = "'IBM Plex Mono', monospace";
  Chart.defaults.font.size = 10.5;
  try{
    Chart.defaults.set('scale', { grid:{ color:'rgba(255,255,255,0.045)' }, border:{ display:false } });
    Chart.defaults.set('scales.category', { grid:{ display:false } });
    Chart.defaults.elements.line.borderWidth = 2;
    Chart.defaults.elements.point.hoverRadius = 5;
    Chart.defaults.elements.point.borderWidth = 0;
    Chart.defaults.interaction.mode = 'index';
    Chart.defaults.interaction.intersect = false;
    var tt = Chart.defaults.plugins.tooltip;
    tt.backgroundColor = '#E9ECF1'; tt.borderWidth = 0; tt.titleColor = '#05070a'; tt.bodyColor = '#05070a';
    tt.padding = { x:12, y:8 }; tt.cornerRadius = 14; tt.boxPadding = 4; tt.usePointStyle = true; tt.caretSize = 0;
    Chart.defaults.elements.bar.borderRadius = 6;
    Chart.defaults.datasets.bar.maxBarThickness = 18;
    tt.titleFont = { family:"'IBM Plex Sans', sans-serif", weight:'600', size:12 };
    tt.bodyFont = { family:"'IBM Plex Mono', monospace", size:11.5 };
    var lg = Chart.defaults.plugins.legend.labels;
    lg.usePointStyle = true; lg.pointStyle = 'circle'; lg.boxHeight = 6; lg.boxWidth = 6;
  }catch(e){ console.error('stile grafici', e); }
  function vwRgba(hex, a){
    if(typeof hex !== 'string' || hex.charAt(0) !== '#' || hex.length !== 7) return hex;
    return 'rgba(' + parseInt(hex.slice(1,3),16) + ',' + parseInt(hex.slice(3,5),16) + ',' + parseInt(hex.slice(5,7),16) + ',' + a + ')';
  }
  Chart.register({
    id:'vwKit',
    beforeUpdate:function(chart){
      if(chart.config.type !== 'line') return;
      chart.data.datasets.forEach(function(ds){
        if(ds._vw) return; ds._vw = true;
        var col = ds.borderColor;
        if(ds.data && ds.data.length > 8 && ds.pointRadius) ds.pointRadius = 0;
        if(ds.fill && typeof col === 'string'){
          ds.backgroundColor = function(c){
            var a = c.chart.chartArea; if(!a) return vwRgba(col, 0.12);
            var g = c.chart.ctx.createLinearGradient(0, a.top, 0, a.bottom);
            g.addColorStop(0, vwRgba(col, 0.28)); g.addColorStop(1, vwRgba(col, 0));
            return g;
          };
        }
      });
    },
    beforeDatasetDraw:function(chart, args){
      if(args.meta.type !== 'line') return;
      var ds = chart.data.datasets[args.index];
      chart.ctx.save(); chart.ctx.shadowColor = ds.borderColor; chart.ctx.shadowBlur = 12;
    },
    afterDatasetDraw:function(chart, args){ if(args.meta.type === 'line') chart.ctx.restore(); }
  });
  /* punto evidenziato: l'ultimo valore (o quello toccato) con linea tratteggiata e fumetto chiaro */
  function vwTesto(chart, v){
    var cb = chart.scales.y && chart.scales.y.options.ticks && chart.scales.y.options.ticks.callback;
    var t = (typeof cb === 'function') ? String(cb.call(chart.scales.y, v, 0, [])) : String(v);
    if(t.charAt(0) === '\\u20ac' && typeof fmt === 'function') return fmt(v, Math.abs(v) >= 1000 ? 0 : 2);
    return t;
  }
  Chart.register({
    id:'vwPunto',
    afterDatasetsDraw:function(chart){
      if(chart.config.type !== 'line' || !chart.chartArea) return;
      var attivi = chart.getActiveElements ? chart.getActiveElements() : [];
      var di = 0, i;
      if(attivi.length){ di = attivi[0].datasetIndex; i = attivi[0].index; }
      var meta = chart.getDatasetMeta(di); if(!meta || meta.hidden || !meta.data.length) return;
      var ds = chart.data.datasets[di];
      if(i === undefined){
        if(chart.data.datasets.length > 2) return;
        for(i = meta.data.length - 1; i >= 0 && (ds.data[i] === null || ds.data[i] === undefined); i--);
        if(i < 0) return;
      }
      var p = meta.data[i]; if(!p || isNaN(p.x) || isNaN(p.y)) return;
      var col = typeof ds.borderColor === 'string' ? ds.borderColor : '#4EDB9C';
      var a = chart.chartArea, ctx = chart.ctx;
      ctx.save();
      ctx.strokeStyle = col; ctx.globalAlpha = .7; ctx.lineWidth = 1; ctx.setLineDash([2, 4]);
      ctx.beginPath(); ctx.moveTo(p.x, p.y); ctx.lineTo(p.x, a.bottom); ctx.stroke();
      ctx.setLineDash([]); ctx.globalAlpha = .25; ctx.fillStyle = col;
      ctx.beginPath(); ctx.arc(p.x, p.y, 8, 0, Math.PI * 2); ctx.fill();
      ctx.globalAlpha = 1; ctx.fillStyle = '#000'; ctx.lineWidth = 2; ctx.strokeStyle = col;
      ctx.beginPath(); ctx.arc(p.x, p.y, 4, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
      if(!attivi.length){
        var v = typeof ds.data[i] === 'object' && ds.data[i] !== null ? ds.data[i].y : ds.data[i];
        var testo = vwTesto(chart, v);
        ctx.font = "500 11px 'IBM Plex Mono', monospace";
        var w = ctx.measureText(testo).width + 20, hh = 22;
        var x = Math.min(Math.max(p.x - w / 2, a.left), a.right - w), y = p.y - hh - 12;
        if(y < a.top - 6) y = p.y + 12;
        ctx.fillStyle = '#E9ECF1';
        ctx.beginPath(); if(ctx.roundRect) ctx.roundRect(x, y, w, hh, hh / 2); else ctx.rect(x, y, w, hh); ctx.fill();
        ctx.fillStyle = '#05070a'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText(testo, x + w / 2, y + hh / 2 + .5);
      }
      ctx.restore();
    }
  });
}""")
sost("borderColor:'#0B0D12', borderWidth:2", "borderWidth:0, spacing:2, cutout:'72%'", conta=3)

# --- dashboard: numero grande del patrimonio + variazioni ---
sost("""  var html = '';
  html += '<div class="kpi-grid">';
  html += kpiCard('Contanti', fmt(c.saldoContanti), '');""", """  var html = '';
  var mesePrima = (function(){ var p = curMonth.split('-'); var y = +p[0], mm = +p[1] - 1; if(mm < 1){ mm = 12; y--; } return y + '-' + (mm < 10 ? '0' : '') + mm; })();
  var varSaldo = cent(saldoContoAlMese(curMonth) - saldoContoAlMese(mesePrima));
  var nettoMese = cent(entrateMese - usciteMese);
  function vwDelta(v, et){ return '<div class="delta ' + (v >= 0 ? 'pos' : 'neg') + '"><b>' + (v >= 0 ? '\\u25B2 +' : '\\u25BC ') + fmt(v) + '</b><small>' + et + '</small></div>'; }
  var pn = fmt(c.patrimonioNetto), pnVirg = pn.lastIndexOf(',');
  var pnHtml = pnVirg > 0 ? escapeHtml(pn.slice(0, pnVirg)) + '<span class="dec">' + escapeHtml(pn.slice(pnVirg)) + '</span>' : escapeHtml(pn);
  var vivo = (loadStatus.tx === 'ok' || loadStatus.tx === 'empty') ? '<span class="vivo"><i></i>Sincronizzato</span>' : '<span class="vivo off"><i></i>Copia locale</span>';
  html += '<div class="hero vw-vetro ' + (c.patrimonioNetto >= 0 ? 'pos' : 'neg') + '">'
    + '<div class="hero-testa"><div class="kpi-label" style="margin:0">Patrimonio netto</div>' + vivo + '</div>'
    + '<div class="hero-val">' + pnHtml + '</div>'
    + '<div class="hero-righe">' + vwDelta(varSaldo, 'Conto vs mese scorso') + vwDelta(nettoMese, 'Entrate \\u2212 uscite del mese') + '</div>'
    + '</div>';
  html += '<div class="kpi-grid">';
  html += kpiCard('Contanti', fmt(c.saldoContanti), '');""")
sost("""  html += kpiCard('Patrimonio netto', fmt(c.patrimonioNetto), c.patrimonioNetto >= 0 ? 'pos':'neg');
  html += '</div>';""", """  html += '</div>';""")

# --- schede: titolo in testata, torna su, interruttore del vetro, data ---
sost("""  btn.classList.add('active');
  document.getElementById('panel-' + btn.dataset.tab).classList.add('active');
});""", """  btn.classList.add('active');
  document.getElementById('panel-' + btn.dataset.tab).classList.add('active');
  var t = document.getElementById('vw-titolo'); if(t) t.textContent = btn.textContent;
  if(window.vwBarra) window.vwBarra(btn.dataset.tab);
  if(window.scrollY > 0) window.scrollTo(0, 0);
});

/* barra in basso sul telefono: 3 sezioni principali, "+" per aggiungere, "Altro" per le altre */
(function(){
  var barra = document.getElementById('vw-barra');
  if(!barra) return;
  var PRINCIPALI = ['dashboard', 'log', 'conti'];
  function apri(sez){ var b = document.querySelector('#ft-tabs .tab-btn[data-tab="' + sez + '"]'); if(b) b.click(); }
  function chiudiAltro(){ document.documentElement.classList.remove('vw-altro'); barra.querySelector('[data-vai="altro"]').setAttribute('aria-expanded', 'false'); }
  window.vwBarra = function(sez){
    barra.querySelectorAll('button').forEach(function(b){ b.classList.remove('on'); b.removeAttribute('aria-current'); });
    var chi = barra.querySelector('[data-vai="' + (PRINCIPALI.indexOf(sez) >= 0 ? sez : 'altro') + '"]');
    if(chi){ chi.classList.add('on'); chi.setAttribute('aria-current', 'page'); }
    chiudiAltro();
  };
  barra.addEventListener('click', function(e){
    var b = e.target.closest('button'); if(!b) return;
    var v = b.dataset.vai;
    if(v === 'altro'){
      var aperto = document.documentElement.classList.toggle('vw-altro');
      b.setAttribute('aria-expanded', aperto ? 'true' : 'false');
      return;
    }
    if(v === 'nuova'){
      apri('log');
      setTimeout(function(){ var f = document.getElementById('tx-amount'); if(f){ f.scrollIntoView({ block:'center' }); f.focus(); } }, 60);
      return;
    }
    apri(v);
  });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') chiudiAltro(); });
  document.addEventListener('click', function(e){
    if(document.documentElement.classList.contains('vw-altro') && !e.target.closest('#ft-tabs') && !e.target.closest('#vw-barra')) chiudiAltro();
  });
  window.vwBarra('dashboard');
})();""")
sost("""    document.getElementById('ft-lastupdate').textContent = 'Dati aggiornati al ' + d.toLocaleDateString('it-IT');""",
     """    document.getElementById('ft-lastupdate').textContent = 'Dati aggiornati al ' + d.toLocaleDateString('it-IT');
    var vd = document.getElementById('vw-data'); if(vd) vd.textContent = d.toLocaleDateString('it-IT', { weekday:'short', day:'2-digit', month:'short', year:'numeric' });""")

pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
pathlib.Path(out).write_text(h, encoding='utf-8')
print('ok', out, len(h))
