<template>
  <section class="why-choose-section">
    <div class="why-choose-container">
      <!-- Perché Mumble -->
      <div class="why-mumble-section">
        <div class="eyebrow font-mono">Perché Mumble</div>
        <h2>Perché scegliere noi</h2>
        <p class="section-intro">Tre motivi per cui i nostri clienti ci scelgono</p>

        <div class="principles-content">
          <div class="principle-main">
            <h3>Software su misura</h3>
            <p><strong>Zero template. Solo codice tuo.</strong> Ogni riga di codice è scritta per le tue esigenze specifiche. Nessun compromesso.</p>
          </div>

          <div class="principles-highlights">
            <div class="highlight-item">
              <h3>Esperti del B2B</h3>
              <p><strong>Capiamo il business.</strong> Sviluppiamo gestionali che migliorano davvero i processi aziendali. Software che fa crescere le aziende.</p>
            </div>

            <div class="highlight-item">
              <h3>Stack affidabile</h3>
              <p><strong>Django + Vue.js + PostgreSQL.</strong> Tecnologie mature e performanti per applicazioni che durano nel tempo.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sezione processo di lavoro spostata nella pagina progetti -->

      <!-- CTA rimossa -->
    </div>
  </section>
</template>

<script setup>
// Nessuna logica particolare necessaria per ora
</script>

<style scoped>
.why-choose-section {
  padding: 80px 0;
  width: 100%;
  background: var(--bg);
}

.why-choose-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}





/* Why Mumble Section */
.why-mumble-section {
  margin-bottom: 0;
}

.why-mumble-section h2 {
  font-size: clamp(32px, 4vw, 40px);
  margin: 0 0 16px;
  font-weight: 400;
  line-height: 1.2;
  color: var(--fg);
  text-align: left;
}

.section-intro {
  font-size: 18px;
  color: var(--muted);
  margin: 0 0 50px;
  text-align: left;
  font-weight: 400;
}

.principles-content {
  max-width: none;
  margin: 0;
}

.principle-main {
  margin-bottom: 40px;
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
  animation-delay: 0.1s;
}

.principle-main h3 {
  font-size: 28px;
  margin: 0 0 20px;
  color: var(--fg);
  font-family: var(--font-mono);
  font-weight: 600;
  position: relative;
  padding-bottom: 12px;
}

.principle-main h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 60px;
  height: 3px;
  background: var(--sage);
  border-radius: 2px;
}

.principle-main p {
  font-size: 18px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
  text-align: left;
  font-weight: 400;
}

.principles-content .principle-main p strong {
  font-weight: 700 !important;
  color: var(--fg) !important;
}

.principles-highlights {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
}

.highlight-item {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.highlight-item:nth-child(1) { animation-delay: 0.2s; }
.highlight-item:nth-child(2) { animation-delay: 0.3s; }

.highlight-item h3 {
  font-size: 22px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
  font-weight: 600;
  position: relative;
  padding-bottom: 10px;
}

.highlight-item:first-child h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 40px;
  height: 3px;
  background: var(--warm-clay);
  border-radius: 2px;
}

.highlight-item:last-child h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 40px;
  height: 3px;
  background: var(--muted);
  border-radius: 2px;
}

.highlight-item p {
  font-size: 16px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
  text-align: left;
  font-weight: 400;
}

.principles-content .highlight-item p strong {
  font-weight: 700 !important;
  color: var(--fg) !important;
}

/* Rimosso: Geometric Graphics non più necessarie */



/* Stili processo di lavoro spostati in WorkProcessSection.vue */

/* Stili CTA rimossi */

/* Keyframes */
@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Rimosso: Animazioni geometriche non più necessarie */

/* Responsive */
@media (max-width: 768px) {
  .why-choose-container {
    padding: 0 24px;
  }

  .principle-main {
    margin-bottom: 24px;
  }

  .principle-main h3 {
    font-size: 24px;
  }

  .principle-main p {
    font-size: 16px;
  }

  .principles-highlights {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .highlight-item h3 {
    font-size: 20px;
  }

  .highlight-item p {
    font-size: 15px;
  }

  /* Stili responsive processo di lavoro spostati in WorkProcessSection.vue */



  /* Stili responsive CTA rimossi */
}


</style>
