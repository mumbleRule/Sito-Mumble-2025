<template>
  <section class="why-choose-section">
    <div class="why-choose-container">
      <!-- Perché Mumble -->
      <div class="why-mumble-section">
        <div class="eyebrow font-mono">Perché Mumble</div>
        <h2>Perché scegliere noi</h2>
        <p class="section-intro">Tre motivi per cui i nostri clienti ci scelgono</p>

        <div class="principles-cards">
          <div class="principle-card">
            <div class="card-number sage">01</div>
            <h3>Software su misura</h3>
            <p><strong>Zero template. Solo codice tuo.</strong> Ogni riga di codice è scritta per le tue esigenze specifiche. Nessun compromesso.</p>
          </div>

          <div class="principle-card">
            <div class="card-number warm-clay">02</div>
            <h3>Esperti del B2B</h3>
            <p><strong>Capiamo il business.</strong> Sviluppiamo gestionali che migliorano davvero i processi aziendali. Software che fa crescere le aziende.</p>
          </div>

          <div class="principle-card">
            <div class="card-number muted">03</div>
            <h3>Stack affidabile</h3>
            <p><strong>Django + Vue.js + PostgreSQL.</strong> Tecnologie mature e performanti per applicazioni che durano nel tempo.</p>
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

.why-mumble-section .eyebrow {
  font-size: 14px;
  margin-bottom: 16px;
}

.why-mumble-section h2 {
  font-size: 32px;
  margin: 0 0 12px;
  font-weight: 500;
  font-family: var(--font-mono);
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

.principles-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: clamp(24px, 4vw, 40px);
  margin: 0;
}

.principle-card {
  background: var(--chip-bg);
  border-radius: 20px;
  padding: 40px;
  text-align: left;
  border: 1px solid var(--line);
  transition: all 0.4s ease;
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
  position: relative;
  overflow: hidden;
}

.principle-card:nth-child(1) { animation-delay: 0.1s; }
.principle-card:nth-child(2) { animation-delay: 0.3s; }
.principle-card:nth-child(3) { animation-delay: 0.5s; }

.principle-card:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
}

.card-number {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 24px;
  animation: tagPulse 2s infinite;
}

.card-number.sage {
  background: var(--sage);
  animation-delay: 0.2s;
}

.card-number.warm-clay {
  background: var(--warm-clay);
  animation-delay: 0.5s;
}

.card-number.muted {
  background: var(--muted);
  animation-delay: 0.8s;
}

.principle-card h3 {
  font-size: 24px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
  font-weight: 600;
  line-height: 1.2;
}

.principle-card p {
  font-size: 16px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
  text-align: left;
  font-weight: 400;
}

.principle-card p strong {
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

@keyframes tagPulse {
  0%, 100% {
    opacity: 0.7;
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(1.05);
  }
}

/* Rimosso: Animazioni geometriche non più necessarie */

/* Responsive */
@media (max-width: 768px) {
  .why-choose-container {
    padding: 0 24px;
  }

  .principles-cards {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .principle-card {
    padding: 32px;
  }

  .card-number {
    width: 40px;
    height: 40px;
    font-size: 18px;
    margin-bottom: 20px;
  }

  .principle-card h3 {
    font-size: 20px;
    margin-bottom: 12px;
  }

  .principle-card p {
    font-size: 15px;
  }
}


</style>
