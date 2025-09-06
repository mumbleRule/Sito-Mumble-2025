<template>
  <section class="home-cta-section">
    <div class="container">
      <div class="home-cta">
        <h2>Il tuo prossimo progetto inizia qui</h2>
        <p>
          Raccontaci la tua idea. Ti spieghiamo come trasformarla in software che risolve problemi reali.
        </p>
        <div class="cta-buttons">
          <router-link to="/contatti" class="btn primary large">
            Parliamo del tuo progetto
          </router-link>
          <router-link to="/servizi" class="btn secondary large">
            Scopri i nostri servizi
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// Nessuna logica particolare necessaria
</script>

<style scoped>
.home-cta-section {
  background: var(--chip-bg);
  padding: 100px 0;
  width: 100%;
}

.home-cta {
  text-align: left;
  max-width: 700px;
}

.home-cta h2 {
  font-size: 32px;
  margin: 0 0 12px;
  color: var(--fg);
  font-weight: 500;
  line-height: 1.2;
  font-family: var(--font-mono);
}

.home-cta p {
  font-size: 18px;
  color: var(--muted);
  margin: 0 0 32px;
  line-height: 1.6;
  max-width: 60ch;
}

.cta-buttons {
  display: flex;
  gap: 16px;
  justify-content: flex-start;
  flex-wrap: wrap;
}

.btn.large {
  font-size: 18px;
  padding: 18px 36px;
  font-weight: 600;
  border-radius: 12px;
}

.btn.primary.large {
  background: #00000020;
  color: var(--fg);
  border-color: var(--line);
}

.btn.primary.large:hover {
  background: #00000030;
  border-color: var(--muted);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.btn.secondary.large {
  background: var(--sage);
  color: #fff;
  border-color: var(--sage);
}

.btn.secondary.large:hover {
  background: #8fa373;
  border-color: #8fa373;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(163, 177, 138, 0.3);
}

/* Responsive */
@media (max-width: 768px) {
  .home-cta-section {
    padding: 80px 0;
  }

  .home-cta {
    padding: 0 24px;
  }

  .home-cta h2 {
    font-size: clamp(28px, 6vw, 36px);
    margin-bottom: 24px;
  }

  .home-cta p {
    font-size: 18px;
    margin-bottom: 32px;
  }

  .cta-buttons {
    flex-direction: column;
    gap: 12px;
  }

  .btn.large {
    width: 100%;
    text-align: center;
    padding: 16px 32px;
  }
}

/* Responsive breakpoints per allineamento su schermi grandi */
/* Large screens - Desktop (≥1200px) */
@media (min-width: 1200px) {
  .home-cta {
    max-width: 800px;
  }

  .home-cta h2 {
    max-width: 50ch;
  }

  .home-cta p {
    max-width: 60ch;
  }
}

/* Extra Large screens - Large Desktop (≥1400px) */
@media (min-width: 1400px) {
  .home-cta {
    max-width: 900px;
  }

  .home-cta h2 {
    max-width: 55ch;
  }

  .home-cta p {
    max-width: 65ch;
  }
}

/* Ultra Wide screens (≥1800px) */
@media (min-width: 1800px) {
  .home-cta {
    max-width: 1000px;
  }

  .home-cta h2 {
    max-width: 60ch;
  }

  .home-cta p {
    max-width: 70ch;
  }
}
</style>
