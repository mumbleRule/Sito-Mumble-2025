<template>
  <section class="work-process-section">
    <div class="work-process-container">
      <!-- Processo di lavoro -->
      <div class="process-section">
        <div class="eyebrow font-mono">Metodologia</div>
        <h2>Come lavoriamo</h2>

        <div class="process-steps">
          <div class="process-step">
            <div class="step-number">01</div>
            <div class="step-content">
              <h4>Analisi</h4>
              <p>Studiamo i tuoi processi attuali e identifichiamo le aree di miglioramento</p>
            </div>
          </div>

          <div class="process-step">
            <div class="step-number">02</div>
            <div class="step-content">
              <h4>Progettazione</h4>
              <p>Definiamo architettura, funzionalità e interfacce della soluzione</p>
            </div>
          </div>

          <div class="process-step">
            <div class="step-number">03</div>
            <div class="step-content">
              <h4>Sviluppo</h4>
              <p>Realizziamo la piattaforma con rilasci incrementali e feedback continui</p>
            </div>
          </div>

          <div class="process-step">
            <div class="step-number">04</div>
            <div class="step-content">
              <h4>Deploy & Support</h4>
              <p>Mettiamo online la soluzione e forniamo supporto per l'adozione</p>
            </div>
          </div>
        </div>
      </div>

      <!-- CTA rimossa -->
    </div>
  </section>
</template>

<script setup>
// Nessuna logica particolare necessaria per ora
</script>

<style scoped>
.work-process-section {
  padding: 80px 0;
  width: 100%;
  background: var(--chip-bg);
}

.work-process-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}

/* Process Section */
.process-section {
  margin-bottom: 0;
}

.process-section h2 {
  font-size: clamp(32px, 4vw, 40px);
  margin: 0 0 50px;
  font-weight: 400;
  line-height: 1.2;
  color: var(--fg);
  text-align: left;
}

.process-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 32px;
}

.process-step {
  display: flex;
  align-items: flex-start;
  gap: 20px;
  padding: 24px;
  background: var(--bg);
  border-radius: var(--radius);
  border: 1px solid var(--line);
  opacity: 0;
  transform: translateY(30px);
  animation: fadeInUp 0.7s ease forwards;
  transition: all 0.3s ease;
}

.process-step:nth-child(1) { animation-delay: 0.1s; }
.process-step:nth-child(2) { animation-delay: 0.25s; }
.process-step:nth-child(3) { animation-delay: 0.4s; }
.process-step:nth-child(4) { animation-delay: 0.55s; }

.process-step:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
}

.step-number {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 600;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  background: var(--fg);
  color: #fff;
  transition: all 0.3s ease;
}

.process-step:hover .step-number {
  transform: scale(1.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.step-content h4 {
  font-family: var(--font-mono);
  font-size: 16px;
  font-weight: 600;
  color: var(--fg);
  margin: 0 0 8px 0;
}

.step-content p {
  font-size: 14px;
  line-height: 1.5;
  color: var(--muted);
  margin: 0;
}

/* Stili CTA rimossi */

/* Keyframes */
@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive */
@media (max-width: 768px) {
  .work-process-container {
    padding: 0 24px;
  }

  .process-steps {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .process-step {
    flex-direction: column;
    text-align: center;
    gap: 16px;
  }

  /* Stili responsive CTA rimossi */
}
</style>
