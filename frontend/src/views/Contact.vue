<template>
  <div class="contact-page">
    <div class="contact-hero">
      <div class="eyebrow font-mono">Contattaci</div>
      <h1>Parliamo del tuo progetto</h1>
      <p class="lead">
        Hai un'idea, una sfida da risolvere o vuoi saperne di più sui nostri servizi?
        Siamo qui per ascoltarti e trovare insieme la soluzione migliore.
      </p>
    </div>

    <div class="contact-content">
      <div class="contact-grid">
        <!-- Form di contatto -->
        <div class="contact-form-section">
          <h2>Invia un messaggio</h2>
          <ContactForm />
        </div>

        <!-- Informazioni di contatto -->
        <div class="contact-info">
          <h2>Altre informazioni</h2>

          <div class="info-card">
            <h3>Email</h3>
            <p>{{ contactEmail }}</p>
          </div>

          <div class="info-card" v-if="contactPhone">
            <h3>Telefono</h3>
            <p>{{ contactPhone }}</p>
          </div>

          <div class="info-card">
            <h3>Tempi di risposta</h3>
            <p>Ti rispondiamo entro 24 ore nei giorni lavorativi.</p>
          </div>

          <div class="info-card">
            <h3>Cosa aspettarsi</h3>
            <p>
              Dopo il primo contatto, organizziamo una chiamata per capire meglio
              le tue esigenze e valutare come possiamo aiutarti.
            </p>
          </div>
        </div>
      </div>
    </div>
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
.contact-page {
  padding-top: 40px;
}

.contact-hero {
  text-align: center;
  margin-bottom: 60px;
}

.contact-hero h1 {
  font-size: clamp(32px, 5vw, 48px);
  margin: 0 0 24px;
  font-weight: 400;
}

.contact-content {
  max-width: 1200px;
  margin: 0 auto;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: start;
}

.contact-form-section h2,
.contact-info h2 {
  font-size: 24px;
  margin-bottom: 24px;
  font-weight: 400;
  font-family: var(--font-mono);
}

.info-card {
  background: var(--chip-bg);
  border-radius: var(--radius);
  padding: 24px;
  margin-bottom: 20px;
}

.info-card h3 {
  font-size: 16px;
  margin: 0 0 8px;
  font-weight: 400;
  color: var(--fg);
  font-family: var(--font-mono);
}

.info-card p {
  font-size: 14px;
  color: var(--muted);
  margin: 0;
  line-height: 1.6;
}

/* Responsive */
@media (max-width: 768px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .contact-hero {
    text-align: left;
    margin-bottom: 40px;
  }
}
</style>
