<template>
  <div class="contact-page">
    <!-- Hero Section -->
    <section class="contact-hero">
      <div class="container">
        <div class="hero-content">
          <div class="eyebrow font-mono">Contattaci</div>
          <h1>Parliamo del tuo progetto</h1>
          <p class="hero-subtitle">
            Hai un'idea, una sfida da risolvere o vuoi saperne di più sui nostri servizi?
            Siamo qui per ascoltarti e trovare insieme la soluzione migliore.
          </p>
          <div class="typing-indicator">
            <div class="typing-dots">
              <span class="dot"></span>
              <span class="dot"></span>
              <span class="dot"></span>
            </div>
          </div>
        </div>
      </div>
    </section>



    <!-- Contact Form Section -->
    <section class="contact-form-section">
      <div class="container">
        <div class="form-card">
          <div class="form-layout">
            <div class="form-content">
              <div class="form-header">
                <h2>Iniziamo insieme</h2>
                <p>Compila il form qui sotto con i dettagli del tuo progetto.</p>
              </div>
              <ContactForm />
            </div>

            <div class="form-sidebar">
              <div class="process-card">
                <h3>Il nostro processo</h3>
                <div class="process-steps">
                  <div class="process-step">
                    <div class="step-number">1</div>
                    <div class="step-content">
                      <h4>Ascoltiamo</h4>
                      <p>Analizziamo le tue esigenze e obiettivi</p>
                    </div>
                  </div>
                  <div class="process-step">
                    <div class="step-number">2</div>
                    <div class="step-content">
                      <h4>Progettiamo</h4>
                      <p>Creiamo la soluzione su misura per te</p>
                    </div>
                  </div>
                  <div class="process-step">
                    <div class="step-number">3</div>
                    <div class="step-content">
                      <h4>Realizziamo</h4>
                      <p>Sviluppiamo e consegniamo il tuo progetto</p>
                    </div>
                  </div>
                </div>
              </div>

              <div class="info-card">
                <h3>Contatti diretti</h3>
                <div class="contact-direct">
                  <a :href="`mailto:${contactEmail}`" class="contact-link">
                    {{ contactEmail }}
                  </a>
                </div>
              </div>

              <div class="info-card">
                <h3>Cosa aspettarsi</h3>
                <p>Dopo il primo contatto, organizziamo una <strong>chiamata conoscitiva</strong> per capire meglio le tue esigenze e valutare come possiamo aiutarti.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ContactForm from '../components/ContactForm.vue'
import { apiService } from '../services/api.js'

const contactEmail = ref('info@mumble.group')
const contactPhone = ref('')

// Carica le informazioni di contatto
onMounted(async () => {
  try {
    const settings = await apiService.getSiteSettings()
    if (settings.contact_email) {
      contactEmail.value = settings.contact_email
    }
    if (settings.contact_phone) {
      contactPhone.value = settings.contact_phone
    }
  } catch (error) {
    console.error('Error loading contact settings:', error)
  }
})
</script>

<style scoped>
/* Contact Page */
.contact-page {
  background: var(--bg);
}

/* Hero Section */
.contact-hero {
  background: var(--bg);
  padding: 120px 0 20px;
  text-align: left;
}

.hero-content {
  max-width: 800px;
}

.hero-content h1 {
  font-size: clamp(40px, 5vw, 56px);
  margin: 0 0 24px;
  font-weight: 400;
  line-height: 1.1;
  color: var(--fg);
}

.hero-subtitle {
  font-size: 20px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0 0 32px;
}

/* Typing Indicator Animation - INVADENTE */
.typing-indicator {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin-top: 40px;
}

.typing-dots {
  display: flex;
  align-items: center;
  gap: 12px;
}

.dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  animation: typingBounceInvadente 1.2s infinite ease-in-out;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.dot:nth-child(1) {
  background: var(--sage);
  animation-delay: 0s;
}

.dot:nth-child(2) {
  background: var(--warm-clay);
  animation-delay: 0.15s;
}

.dot:nth-child(3) {
  background: var(--muted);
  animation-delay: 0.3s;
}

@keyframes typingBounceInvadente {
  0%, 70%, 100% {
    transform: translateY(0) scale(1);
    opacity: 0.6;
  }
  35% {
    transform: translateY(-20px) scale(1.3);
    opacity: 1;
  }
}

/* Nessuna animazione container - focus solo sui puntini */

/* Contact Form Section - inizia direttamente dopo l'hero */

/* Contact Form Section */
.contact-form-section {
  background: var(--bg);
  padding: 20px 0 100px;
}

.form-card {
  background: var(--chip-bg);
  border-radius: 16px;
  padding: 60px;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
}

.form-layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 60px;
  align-items: start;
}

.form-header {
  margin-bottom: 40px;
}

.form-header h2 {
  font-size: 32px;
  margin: 0 0 16px;
  font-weight: 400;
  color: var(--fg);
}

.form-header p {
  font-size: 16px;
  color: var(--muted);
  margin: 0;
  line-height: 1.6;
}

/* Form Sidebar */
.form-sidebar {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.process-card {
  background: var(--bg);
  border-radius: 12px;
  padding: 32px;
}

.process-card h3 {
  font-family: var(--font-mono);
  font-size: 16px;
  font-weight: 600;
  margin: 0 0 24px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--fg);
}

.process-steps {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.process-step {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.step-number {
  width: 32px;
  height: 32px;
  background: var(--sage);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 600;
  flex-shrink: 0;
}

.step-content h4 {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 600;
  margin: 0 0 4px;
  color: var(--fg);
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.step-content p {
  font-size: 14px;
  color: var(--muted);
  margin: 0;
  line-height: 1.5;
}

.info-card {
  background: var(--bg);
  border-radius: 12px;
  padding: 24px;
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.info-card h3 {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 600;
  margin: 0 0 12px;
  color: var(--fg);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.info-card p {
  font-size: 14px;
  color: var(--muted);
  margin: 0;
  line-height: 1.6;
}

.info-card strong {
  color: var(--fg);
}

/* Contact Direct Links */
.contact-direct {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.contact-link {
  display: block;
  text-decoration: none;
  font-size: 14px;
  padding: 8px 0;
  transition: color 0.3s ease;
}

/* Email in warm clay e grassetto */
.contact-link[href^="mailto:"] {
  color: var(--warm-clay);
  font-weight: 600;
}

.contact-link:hover {
  color: var(--warm-clay);
  opacity: 0.8;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .form-layout {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .form-sidebar {
    order: -1;
  }
}

@media (max-width: 768px) {
  .contact-hero {
    padding: 80px 0 15px;
  }

  .contact-form-section {
    padding: 15px 0 80px;
  }

  .form-card {
    padding: 40px;
  }

  .process-steps {
    gap: 16px;
  }

  .process-step {
    gap: 12px;
  }

  .step-number {
    width: 28px;
    height: 28px;
    font-size: 12px;
  }
}

@media (max-width: 480px) {
  .contact-hero {
    padding: 60px 0 10px;
  }

  .contact-form-section {
    padding: 10px 0 60px;
  }

  .form-card {
    padding: 24px;
    border-radius: 12px;
  }

  .process-card,
  .info-card {
    padding: 20px;
  }
}
</style>
