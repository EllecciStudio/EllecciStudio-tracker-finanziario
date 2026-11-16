/* Ellecci Studio · movimento "da dashboard" (16/11/2026, DESIGN.md > Movimento)
   Modulo unico da incollare nelle app (AltSonar, BandPilot, Trading Studio…). VaultWatch ha la sua versione dentro index.html.
   - EsMovimento.entra(radice, { blocchi, numeri }): schede a cascata + numeri che contano da 0 + grafici Chart.js che si costruiscono
     (le linee si disegnano da sinistra quando arrivano sullo schermo, barre e ciambelle rifanno la loro animazione).
   - EsMovimento.cambioPagina(cambia): cambio pagina a cerchio dal punto toccato (View Transitions; dove manca, cambio normale).
   Con "riduci movimento" del sistema non parte nulla. Se l'app riscrive un numero mentre conta, il conteggio prosegue verso il valore nuovo. */
(function(){
  if (window.EsMovimento) return;
  var FERMO = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var PASSO = 50, MAX = 12, CONTA = 1150, DISEGNA = 900;
  var puntatore = null, giro = 0;
  function ease(t){ return 1 - Math.pow(1 - t, 3); }
  document.addEventListener('pointerdown', function(e){ puntatore = { x:e.clientX, y:e.clientY, t:Date.now() }; }, true);

  var css = '@keyframes es-entra{from{opacity:0;transform:translateY(8px);filter:blur(4px)}to{opacity:1;transform:none;filter:none}}'
    + '.es-in{animation:es-entra .46s cubic-bezier(0.23,1,0.32,1) backwards;animation-delay:var(--es-ritardo,0ms)}'
    + '::view-transition-old(root){animation:none;mix-blend-mode:normal}'
    + '::view-transition-new(root){animation:es-cerchio .38s cubic-bezier(0.23,1,0.32,1) both;mix-blend-mode:normal}'
    + '@keyframes es-cerchio{from{clip-path:circle(0 at var(--es-cx,50%) var(--es-cy,100%))}to{clip-path:circle(150vmax at var(--es-cx,50%) var(--es-cy,100%))}}'
    + '@media (prefers-reduced-motion:reduce){.es-in{animation:none}::view-transition-new(root){animation:none}}';
  var st = document.createElement('style'); st.id = 'es-movimento'; st.textContent = css; document.head.appendChild(st);

  /* numero dentro un testo qualsiasi ("1.234,56 €", "42.3%", "+12.5", "$2,13 T"): si riscrive con gli stessi separatori */
  function leggi(testo){
    var m = /[-+−]?\d[\d.,]*/.exec(testo); if (!m) return null;
    var tok = m[0].replace(/[.,]+$/, ''), segno = '';
    if (/^[-+−]/.test(tok)){ segno = tok[0]; tok = tok.slice(1); }
    var ip = tok.lastIndexOf('.'), iv = tok.lastIndexOf(','), dsep = '', gsep = '';
    if (ip >= 0 && iv >= 0){ dsep = ip > iv ? '.' : ','; gsep = dsep === '.' ? ',' : '.'; }
    else if (ip >= 0 || iv >= 0){
      var c = ip >= 0 ? '.' : ',', volte = tok.split(c).length - 1, dopo = tok.length - tok.lastIndexOf(c) - 1;
      if (volte > 1 || (dopo === 3 && c === '.')) gsep = c; else dsep = c;
    }
    var parti = dsep ? tok.split(dsep) : [tok], intero = parti[0].split(gsep || '#').join(''), dec = parti[1] || '';
    var v = parseFloat(intero + (dec ? '.' + dec : '')); if (!isFinite(v)) return null;
    if (segno === '-' || segno === '−') v = -v;
    return { pre:testo.slice(0, m.index), suf:testo.slice(m.index + tok.length + (segno ? 1 : 0)), v:v, dec:dec.length, dsep:dsep || ',', gsep:gsep,
             piu:segno === '+', meno:segno === '−' ? '−' : '-', raggruppa:!!gsep };
  }
  function formatta(n, x){
    var a = Math.abs(x).toFixed(n.dec).split('.'), i = a[0];
    if (n.raggruppa) i = i.replace(/\B(?=(\d{3})+(?!\d))/g, n.gsep);
    var s = i + (n.dec ? n.dsep + a[1] : ''), zero = !/[1-9]/.test(s);
    return n.pre + (x < 0 && !zero ? n.meno : (n.piu ? '+' : '')) + s + n.suf;
  }

  function cascata(blocchi){
    blocchi.forEach(function(b, i){
      b.style.setProperty('--es-ritardo', Math.min(i, MAX) * PASSO + 'ms');
      b.classList.remove('es-in'); void b.offsetWidth; b.classList.add('es-in');
    });
  }

  function conta(voci, mio){
    var t0 = performance.now();
    voci.forEach(function(q){ q.el.textContent = q.ultimo = formatta(q.n, 0); });
    (function passo(){
      if (mio !== giro) return;
      var ora = performance.now() - t0, finito = true;
      voci.forEach(function(q){
        if (q.fatto || !q.el.isConnected) return;
        if (q.el.textContent !== q.ultimo){                              // l'app ha scritto un valore nuovo: si continua verso quello
          var nn = leggi(q.el.textContent); if (!nn){ q.fatto = true; return; }
          q.n = nn; q.testo = q.el.textContent;
        }
        var t = Math.min(1, Math.max(0, (ora - q.inizio) / CONTA));
        if (t < 1){ finito = false; q.el.textContent = q.ultimo = formatta(q.n, q.n.v * ease(t)); }
        else { q.fatto = true; q.el.textContent = q.testo; }
      });
      if (!finito) requestAnimationFrame(passo);
    })();
  }

  if (window.Chart && Chart.register){
    Chart.register({
      id:'esRivela',
      beforeDatasetsDraw:function(ch){
        if (ch.$esRivela === undefined || ch.$esRivela >= 1 || !ch.chartArea) return;
        var a = ch.chartArea; ch.ctx.save(); ch.ctx.beginPath();
        ch.ctx.rect(a.left - 4, 0, (a.right - a.left + 8) * ch.$esRivela, ch.height); ch.ctx.clip(); ch.$esClip = true;
      },
      afterDatasetsDraw:function(ch){ if (ch.$esClip){ ch.ctx.restore(); ch.$esClip = false; } }
    });
  }
  function grafici(radice){
    if (!window.Chart || !Chart.getChart) return;
    radice.querySelectorAll('canvas').forEach(function(cv){
      var ch = Chart.getChart(cv); if (!ch) return;
      if (ch.$esOss){ ch.$esOss.disconnect(); ch.$esOss = null; }
      var linea = ch.config.type === 'line';
      function parti(){
        if (linea){
          var t0 = performance.now() + 120;
          (function passo(){
            if (!ch.canvas) return;
            var t = Math.min(1, Math.max(0, (performance.now() - t0) / DISEGNA));
            ch.$esRivela = ease(t); ch.draw();
            if (t < 1) requestAnimationFrame(passo); else { ch.$esRivela = 1; ch.draw(); }
          })();
        } else {
          var anim = ch.options.animation;
          if (anim === false){ ch.options.animation = { duration:900, easing:'easeOutCubic' }; }
          try { ch.update(); } catch(e){}
          if (anim === false) ch.options.animation = false;
        }
      }
      if (linea){ ch.$esRivela = 0; ch.draw(); } else { try { ch.reset(); ch.draw(); } catch(e){} }
      var r = cv.getBoundingClientRect();
      if (!window.IntersectionObserver || (r.top < innerHeight * 0.85 && r.bottom > 0)){ parti(); return; }
      var oss = new IntersectionObserver(function(v){ if (v.some(function(x){ return x.isIntersecting; })){ oss.disconnect(); ch.$esOss = null; parti(); } }, { threshold:0.35 });
      ch.$esOss = oss; oss.observe(cv);
    });
  }

  function entra(radice, opz){
    if (FERMO || !radice) return;
    opz = opz || {};
    var mio = ++giro;
    var tutti = Array.prototype.slice.call(radice.querySelectorAll(opz.blocchi || '.card, .kpi, .panel'));
    var blocchi = tutti.filter(function(b){ return !tutti.some(function(a){ return a !== b && a.contains(b); }); });
    cascata(blocchi);
    var voci = [];
    if (opz.numeri) radice.querySelectorAll(opz.numeri).forEach(function(el){
      if (el.children.length) return;
      var testo = el.textContent, n = leggi(testo); if (!n || n.v === 0) return;
      var pos = -1; blocchi.some(function(b, i){ if (b.contains(el)){ pos = i; return true; } return false; });
      voci.push({ el:el, n:n, testo:testo, inizio:Math.max(0, Math.min(pos, MAX)) * PASSO + 80 });
    });
    if (voci.length) conta(voci, mio);
    requestAnimationFrame(function(){ grafici(radice); });
  }

  function cambioPagina(cambia){
    if (FERMO || !document.startViewTransition){ cambia(); return; }
    var p = puntatore, recente = p && Date.now() - p.t < 1500, r = document.documentElement.style;
    r.setProperty('--es-cx', (recente ? p.x : innerWidth / 2) + 'px'); r.setProperty('--es-cy', (recente ? p.y : innerHeight) + 'px');
    try { document.startViewTransition(cambia); } catch(e){ cambia(); }
  }

  window.EsMovimento = { entra:entra, cambioPagina:cambioPagina, grafici:grafici, fermo:FERMO, _leggi:leggi, _formatta:formatta };
})();
