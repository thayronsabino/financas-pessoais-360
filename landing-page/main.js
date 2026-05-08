/* ===================================================
   MordomIA — main.js
   =================================================== */

/* ---- NAV scroll shadow + Scroll-to-top button ---- */
(function initNav() {
  const nav = document.getElementById('nav');
  const scrollBtn = document.getElementById('scrollTop');

  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    if (nav) nav.style.boxShadow = y > 40 ? '0 4px 32px rgba(0,0,0,0.5)' : 'none';
    if (scrollBtn) scrollBtn.classList.toggle('visible', y > 500);
  }, { passive: true });
})();

/* ---- Manifesto modal ---- */
function openManifesto() {
  const modal = document.getElementById('manifestoModal');
  if (!modal) return;
  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
  const panel = modal.querySelector('.modal-panel');
  if (panel) setTimeout(() => panel.focus(), 50);
}

function closeManifesto(e) {
  if (e && e.target !== document.getElementById('manifestoModal')) return;
  const modal = document.getElementById('manifestoModal');
  if (!modal) return;
  modal.classList.remove('open');
  document.body.style.overflow = '';
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const modal = document.getElementById('manifestoModal');
    if (modal && modal.classList.contains('open')) {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    }
  }
});

/* ---- Reveal on scroll (IntersectionObserver) ---- */
(function initReveal() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.10 }
  );

  // Add reveal to elements that don't already have it in HTML
  document.querySelectorAll(
    '.principle, .journey-step, .install-card, ' +
    '.quote, .section-label, .section-title, .section-sub, ' +
    '.cta-content, .footer-inner, .icp-card, .proof-grid, ' +
    '.skill-detail-card'
  ).forEach((el) => el.classList.add('reveal'));

  // Observe ALL elements with .reveal — including those set directly in HTML
  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
})();

/* ---- Copy button feedback on code blocks ---- */
(function initCopyButtons() {
  document.querySelectorAll('.code-block').forEach((block) => {
    block.title = 'Clique para copiar';
    block.addEventListener('click', function () {
      const text = this.querySelector('.code-line')?.textContent.replace(/^\$\s*/, '').trim();
      if (!text) return;
      navigator.clipboard.writeText(text).then(() => {
        const original = this.style.borderColor;
        this.style.borderColor = 'var(--gold)';
        const flash = document.createElement('div');
        flash.textContent = 'Copiado!';
        Object.assign(flash.style, {
          position: 'absolute', top: '8px', right: '12px',
          fontSize: '11px', fontWeight: '700',
          color: 'var(--gold)', pointerEvents: 'none',
          opacity: '1', transition: 'opacity 0.4s',
        });
        this.style.position = 'relative';
        this.appendChild(flash);
        setTimeout(() => { flash.style.opacity = '0'; }, 1200);
        setTimeout(() => { flash.remove(); this.style.borderColor = original; }, 1800);
      });
    });
  });
})();

/* ---- Staggered entrance for grids ---- */
(function initStagger() {
  document.querySelectorAll('.principles-grid, .install-grid, .icp-grid, .skills-detail-grid').forEach((grid) => {
    Array.from(grid.children).forEach((child, i) => {
      child.style.transitionDelay = `${i * 70}ms`;
    });
  });
  document.querySelectorAll('.journey-steps').forEach((list) => {
    Array.from(list.children).filter(c => c.classList.contains('journey-step')).forEach((child, i) => {
      child.style.transitionDelay = `${i * 100}ms`;
    });
  });
})();

/* ---- Smooth scroll for anchor links ---- */
(function initSmoothLinks() {
  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener('click', (e) => {
      const id = link.getAttribute('href').slice(1);
      const target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      const offset = 80;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
})();

/* ---- Floating particles (canvas) ---- */
(function initParticles() {
  const canvas = document.createElement('canvas');
  Object.assign(canvas.style, {
    position: 'fixed', top: '0', left: '0',
    width: '100%', height: '100%',
    pointerEvents: 'none', zIndex: '0', opacity: '0.5',
  });
  document.body.prepend(canvas);

  const ctx = canvas.getContext('2d');
  const COUNT = 22;
  let particles = [], W, H;

  function resize() { W = canvas.width = window.innerWidth; H = canvas.height = window.innerHeight; }
  resize();
  window.addEventListener('resize', resize, { passive: true });

  function rand(min, max) { return Math.random() * (max - min) + min; }

  function mkParticle() {
    return {
      x: rand(0, W), y: rand(0, H),
      r: rand(0.8, 2.0),
      dx: rand(-0.12, 0.12), dy: rand(-0.22, -0.04),
      alpha: rand(0.15, 0.65),
      dAlpha: rand(0.002, 0.005) * (Math.random() < 0.5 ? 1 : -1),
    };
  }

  particles = Array.from({ length: COUNT }, mkParticle);

  function draw() {
    ctx.clearRect(0, 0, W, H);
    particles.forEach((p) => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      const isGold = p.r > 1.4;
      ctx.fillStyle = isGold
        ? `rgba(196,152,74,${p.alpha * 0.6})`
        : `rgba(63,185,80,${p.alpha * 0.4})`;
      ctx.fill();
      p.x += p.dx; p.y += p.dy;
      p.alpha += p.dAlpha;
      if (p.alpha <= 0.1 || p.alpha >= 0.7) p.dAlpha *= -1;
      if (p.y < -10) { p.y = H + 10; p.x = rand(0, W); }
    });
    requestAnimationFrame(draw);
  }
  draw();
})();

/* ---- Journey steps entrance animation ---- */
(function initJourneyHighlight() {
  const steps = document.querySelectorAll('.journey-step');
  if (!steps.length) return;
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          steps.forEach((s, i) => setTimeout(() => s.classList.add('visible'), i * 120));
          io.disconnect();
        }
      });
    },
    { threshold: 0.15 }
  );
  const section = document.getElementById('jornada');
  if (section) io.observe(section);
})();
