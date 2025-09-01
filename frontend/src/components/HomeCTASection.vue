<template>
  <section class="home-cta-section">
    <div class="container">
      <div class="home-cta">
        <h2>Hai un progetto in mente?</h2>
        <p>
          Raccontaci la tua sfida e troviamo insieme la soluzione migliore
          per la tua azienda.
        </p>
        <div class="cta-button">
          <router-link to="/contatti" class="btn primary large">
            Parliamo del tuo progetto
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
  background: linear-gradient(135deg, var(--sage) 0%, var(--warm-clay) 100%);
  padding: 80px 0;
  width: 100%;
  position: relative;
  overflow: hidden;
}

.home-cta-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.95);
  z-index: 1;
}

.container {
  position: relative;
  z-index: 2;
}

.home-cta {
  text-align: left;
  max-width: 600px;
}

.home-cta h2 {
  font-size: clamp(32px, 4vw, 40px);
  margin: 0 0 24px;
  color: var(--fg);
  font-weight: 400;
  line-height: 1.2;
}

.home-cta p {
  font-size: 18px;
  color: var(--muted);
  margin: 0 0 32px;
  line-height: 1.6;
}

.cta-button {
  display: flex;
  justify-content: flex-start;
}

.btn.primary {
  font-size: 16px;
  padding: 14px 32px;
  transition: all 0.3s ease;
}

.btn.primary.large {
  font-size: 18px;
  padding: 18px 40px;
  font-weight: 600;
}

.btn.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

/* Responsive */
@media (max-width: 768px) {
  .home-cta-section {
    padding: 60px 0;
  }
  
  .home-cta {
    padding: 0 24px;
  }
  
  .home-cta h2 {
    font-size: clamp(28px, 6vw, 32px);
    margin-bottom: 20px;
  }
  
  .home-cta p {
    font-size: 16px;
    margin-bottom: 28px;
  }
}
</style>
