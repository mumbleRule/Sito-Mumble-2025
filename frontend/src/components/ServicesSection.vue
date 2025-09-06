<template>
  <section id="services" class="services">
    <div class="services-container">
      <h2>Quello che sviluppiamo per te</h2>
      <p class="section-subtitle">
        Gestionali, web app e integrazioni: il software che fa crescere il tuo business
      </p>
      <div class="services-grid">
        <template v-for="(category, categoryIndex) in serviceCategories" :key="categoryIndex">
          <div class="category-section">
            <h3 class="category-header">{{ category.title }}</h3>
            <div class="category-cards">
              <router-link
                v-for="(service, serviceIndex) in category.services"
                :key="`${categoryIndex}-${serviceIndex}`"
                :to="getServiceLink(service.title)"
                class="service-card fade-in"
              >
                <div class="card-header">
                  <span class="service-tags">{{ service.subtitle }}</span>
                  <h4 class="service-title">{{ service.title }}</h4>
                </div>
                <div class="card-content">
                  <p class="service-description" v-html="service.description"></p>
                </div>
              </router-link>
            </div>
          </div>
        </template>
      </div>

      <div class="services-cta">
        <h3 class="cta-title">Hai un'idea? Realizziamola insieme.</h3>
        <p class="cta-description">
          Raccontaci il tuo progetto. Ti spieghiamo come trasformarlo in software che funziona.
        </p>
        <div class="cta-buttons">
          <router-link class="btn primary" to="/contatti">
            Contattaci
          </router-link>
          <router-link class="btn secondary" to="/servizi">
            Scopri tutti i servizi
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { apiService } from '../services/api.js'

const services = ref([])
const loading = ref(true)

// Funzione per mappare i servizi ai loro link nella pagina servizi
const getServiceLink = (serviceTitle) => {
  const serviceLinks = {
    'Development su misura': '/servizi#sviluppo',
    'UX/UI Design': '/servizi#sviluppo',
    'API e Integrazioni': '/servizi#integrazione',
    'Piattaforme B2B': '/servizi#integrazione',
    'CRM e Gestionali': '/servizi#gestione',
    'Analytics e BI': '/servizi#gestione'
  }

  return serviceLinks[serviceTitle] || '/servizi'
}

// Struttura organizzata dei servizi per categorie
const serviceCategories = ref([
  {
    title: 'SVILUPPO',
    services: [
      {
        title: 'Development su misura',
        description: 'Gestionali 100% personalizzati con tecnologie moderne e affidabili. <strong>Python, Django, Vue.js</strong>: il nostro stack preferito per applicazioni robuste e scalabili.',
        subtitle: 'PYTHON • DJANGO • VUE.JS'
      },
      {
        title: 'UX/UI Design',
        description: 'Interfacce che i tuoi utenti capiscono al primo sguardo. Design funzionale e moderno per web app che migliorano davvero la produttività.',
        subtitle: 'DESIGN • INTERFACCE • RESPONSIVE'
      }
    ]
  },
  {
    title: 'INTEGRAZIONE',
    services: [
      {
        title: 'API e Integrazioni',
        description: 'Facciamo parlare i tuoi sistemi tra loro. <strong>API sicure</strong>, sincronizzazione dati e automazione dei processi per eliminare il lavoro manuale.',
        subtitle: 'REST API • WEBHOOKS • AUTOMAZIONE'
      },
      {
        title: 'Piattaforme B2B',
        description: 'Piattaforme complete per gestire clienti e fornitori. Soluzioni che crescono con la tua azienda senza rallentamenti.',
        subtitle: 'PORTALI • SCALABILITÀ • PERFORMANCE'
      }
    ]
  },
  {
    title: 'GESTIONE',
    services: [
      {
        title: 'CRM e Gestionali',
        description: 'Sistemi di gestione che centralizzano tutto: clienti, vendite, magazzino. Un\'unica piattaforma per controllare il tuo business.',
        subtitle: 'CRM • ERP • BUSINESS LOGIC'
      },
      {
        title: 'Analytics e BI',
        description: 'Trasforma i dati in decisioni strategiche. Dashboard chiare e reportistica che ti dice cosa funziona e cosa migliorare.',
        subtitle: 'DASHBOARD • KPI • DECISIONI'
      }
    ]
  }
])

// Servizi di default per fallback
const defaultServices = ref([
  {
    title: 'CRM e ERP',
    description: 'Sistemi di gestione clienti e risorse aziendali su misura. Centralizza vendite, contatti, inventario e processi in un\'unica piattaforma efficiente.',
    subtitle: 'Gestione aziendale integrata'
  },
  {
    title: 'Development',
    description: 'Gestionali personalizzabili al 100% con codice scritto da zero. Prediligiamo <strong>Python</strong>, <strong>Django</strong>, <strong>Vue.js</strong> e <strong>PostgreSQL</strong>, ma adattiamo la tecnologia alle tue esigenze.',
    subtitle: 'Codice su misura, risultati concreti'
  },
  {
    title: 'Portali & Piattaforme',
    description: 'Progettiamo e sviluppiamo portali, aree riservate, aree clienti e piattaforme digitali complete.',
    subtitle: 'Presenza digitale strutturata'
  },
  {
    title: 'Web App & UX/UI',
    description: 'Sviluppiamo web app moderne e ottimizziamo l\'esperienza utente. Collaboriamo con designer esperti per risultati eccellenti.',
    subtitle: 'Esperienza utente ottimizzata'
  },
  {
    title: 'Integrazioni API',
    description: 'Integriamo il tuo gestionale esistente con nuove funzionalità. Reportistica avanzata e connessioni tra sistemi diversi.',
    subtitle: 'Ecosistema connesso'
  }
])

// Carica i servizi dal backend
onMounted(async () => {
  try {
    const data = await apiService.getServices()
    services.value = data
  } catch (error) {
    console.error('Error loading services:', error)
    // In caso di errore, manteniamo i servizi di default nel template
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
/* Stili per le card cliccabili */
.service-card {
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
  cursor: pointer;
}

.service-card:hover {
  text-decoration: none;
  color: inherit;
}

.service-card:visited {
  color: inherit;
}

/* Responsive Design Semplice */
/* Desktop (≥1200px) */
@media (min-width: 1200px) {
  .services-cta .cta-title {
    font-size: 28px;
  }

  .services-cta .cta-description {
    font-size: 18px;
  }
}

/* Large Desktop (≥1600px) */
@media (min-width: 1600px) {
  .services-cta .cta-title {
    font-size: 32px;
  }

  .services-cta .cta-description {
    font-size: 20px;
  }
}
</style>
