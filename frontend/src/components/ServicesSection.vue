<template>
  <section id="services" class="services">
    <div class="services-container">
      <h2>I nostri servizi</h2>
      <p class="section-subtitle">
        Soluzioni digitali complete per automatizzare e ottimizzare i processi della tua azienda
      </p>
      <div class="services-grid">
        <template v-for="(category, categoryIndex) in serviceCategories" :key="categoryIndex">
          <div class="category-section">
            <h3 class="category-header">{{ category.title }}</h3>
            <div class="category-cards">
              <div
                v-for="(service, serviceIndex) in category.services"
                :key="`${categoryIndex}-${serviceIndex}`"
                class="service-card fade-in"
              >
                <div class="card-header">
                  <h4 class="service-title">{{ service.title }}</h4>
                  <span class="service-tags">{{ service.subtitle }}</span>
                </div>
                <div class="card-content">
                  <p class="service-description" v-html="service.description"></p>
                </div>
              </div>
            </div>
          </div>
        </template>
      </div>

      <div class="services-cta">
        <h3 class="cta-title">Pronto a trasformare i tuoi processi?</h3>
        <p class="cta-description">
          Parliamo del tuo progetto e scopriamo insieme come possiamo aiutarti a crescere.
        </p>
        <div class="cta-buttons">
          <router-link class="btn primary" to="/contatti">
            Richiedi consulenza
          </router-link>
          <router-link class="btn secondary" to="/progetti">
            Vedi i nostri progetti
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

// Struttura organizzata dei servizi per categorie
const serviceCategories = ref([
  {
    title: 'SVILUPPO',
    services: [
      {
        title: 'Development',
        description: 'Gestionali personalizzabili al 100% con codice scritto da zero. Prediligiamo <strong>Python</strong>, <strong>Django</strong>, <strong>Vue.js</strong> e <strong>PostgreSQL</strong>, ma adattiamo la tecnologia alle tue esigenze.',
        subtitle: 'PYTHON • DJANGO • VUE.JS'
      },
      {
        title: 'Web App & UX/UI',
        description: 'Interfacce intuitive e responsive che migliorano l\'esperienza utente. Design moderno e funzionale per web app che i tuoi utenti ameranno utilizzare.',
        subtitle: 'DESIGN • UX/UI • RESPONSIVE'
      }
    ]
  },
  {
    title: 'INTEGRAZIONE',
    services: [
      {
        title: 'Integrazioni API',
        description: 'Colleghiamo i tuoi sistemi esistenti attraverso API robuste e sicure. Sincronizzazione dati, automazione processi e comunicazione tra piattaforme diverse.',
        subtitle: 'REST API • WEBHOOKS • SYNC'
      },
      {
        title: 'Portali & Piattaforme',
        description: 'Piattaforme web complete per gestire clienti, fornitori e processi aziendali. Soluzioni scalabili che crescono con la tua azienda.',
        subtitle: 'PORTALI • B2B • SCALABILITÀ'
      }
    ]
  },
  {
    title: 'GESTIONE',
    services: [
      {
        title: 'CRM e ERP',
        description: 'Sistemi di gestione clienti e risorse aziendali su misura. Centralizza vendite, contatti, inventario e processi in un\'unica piattaforma efficiente.',
        subtitle: 'CRM • ERP • GESTIONALE'
      },
      {
        title: 'Business Intelligence',
        description: 'Dashboard interattive e reportistica avanzata per trasformare i tuoi dati in decisioni strategiche. Analisi predittive e KPI personalizzati per monitorare le performance aziendali.',
        subtitle: 'DASHBOARD • ANALYTICS • REPORTING'
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
/* Gli stili sono già definiti nel CSS globale */
</style>
