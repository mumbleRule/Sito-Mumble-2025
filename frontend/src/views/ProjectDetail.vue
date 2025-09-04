<template>
  <div class="project-detail-page">
    <!-- Sezione Hero -->
    <section class="project-hero-section">
      <div class="container">
        <div v-if="loading" class="loading">
          Caricamento progetto...
        </div>

        <div v-else-if="error" class="error-state">
          <h2>Progetto non trovato</h2>
          <p>Il progetto che stai cercando non esiste o è stato rimosso.</p>
          <router-link to="/progetti" class="btn primary">
            Torna ai progetti
          </router-link>
        </div>

        <div v-else-if="project" class="project-detail">
          <!-- Breadcrumb -->
          <nav class="breadcrumb">
            <router-link to="/" class="breadcrumb-link">Home</router-link>
            <span class="breadcrumb-separator">/</span>
            <router-link to="/progetti" class="breadcrumb-link">Progetti</router-link>
            <span class="breadcrumb-separator">/</span>
            <span class="breadcrumb-current">{{ project.title }}</span>
          </nav>

          <!-- Hero del progetto -->
          <div class="project-hero">
            <div class="project-hero-content">
              <div class="project-meta-header">
                <span class="project-category" v-if="project.category">{{ project.category }}</span>
                <span class="project-client" v-if="project.client">{{ project.client }}</span>
              </div>

              <h1 class="hero-title">{{ project.title }}</h1>
              <p class="project-lead">{{ project.description }}</p>

              <div class="project-tech-header" v-if="project.technologies">
                <h3>Tecnologie utilizzate</h3>
                <div class="tech-tags">
                  <span
                    v-for="tech in getTechnologies(project.technologies)"
                    :key="tech"
                    class="tech-tag"
                  >
                    {{ tech }}
                  </span>
                </div>
              </div>

              <div class="project-actions">
                <a v-if="project.url" :href="project.url" target="_blank" class="btn primary">
                  Visita il progetto
                </a>
                <router-link to="/contatti" class="btn secondary">
                  Parliamo del tuo progetto
                </router-link>
              </div>
            </div>

            <div class="project-hero-image" v-if="getProjectImage(project.title)">
              <img
                :src="getProjectImage(project.title)"
                :alt="project.title"
                class="hero-image"
              >
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sezione Storia -->
    <section class="project-story-section">
      <div class="container">
        <div v-if="project">
          <div class="project-story" v-if="getProjectContent(project.title)">
              <div class="story-content">
                <div class="story-section story-challenge">
                  <h2>La sfida</h2>
                  <p>{{ getProjectContent(project.title).challenge }}</p>
                </div>

                <div class="story-highlights">
                  <div class="highlight-item">
                    <h2>L'obiettivo</h2>
                    <p>{{ getProjectContent(project.title).objective }}</p>
                  </div>

                  <div class="highlight-item">
                    <h2>La soluzione</h2>
                    <p>{{ getProjectContent(project.title).solution }}</p>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </section>

    <!-- Sezione Funzionalità -->
    <section class="project-features-section">
      <div class="container">
        <div v-if="project">
          <div class="project-features" v-if="getProjectContent(project.title)?.features">
              <h2>Funzionalità principali</h2>
              <p class="features-subtitle" v-if="project.title === 'Hotel Target'">Esplora le funzionalità del CRM Hotel Target attraverso le schermate dell'interfaccia</p>
              <p class="features-subtitle" v-else-if="project.title === 'IF65'">Scopri le funzionalità della piattaforma di project management attraverso le schermate del sistema</p>
              <p class="features-subtitle" v-else>Esplora le funzionalità principali attraverso le schermate dell'interfaccia</p>

              <div class="features-with-images">
                <div
                  v-for="(feature, index) in getProjectContent(project.title).features"
                  :key="feature.title"
                  class="feature-with-image"
                  :class="{
                    'reverse': index % 2 === 1 && !isVerticalLayout(index),
                    'vertical': isVerticalLayout(index)
                  }"
                >
                  <div class="feature-screenshot" v-if="getMatchingScreenshot(feature.title)">
                    <div
                      class="screenshot-container"
                      @click="openLightbox(getMatchingScreenshot(feature.title))"
                    >
                      <img
                        :src="getMatchingScreenshot(feature.title).src"
                        :alt="getMatchingScreenshot(feature.title).title"
                        class="screenshot-image"
                      />
                      <div class="screenshot-overlay">
                        <span class="zoom-icon">Clicca per ingrandire</span>
                      </div>
                    </div>
                  </div>

                  <div class="feature-content">
                    <h3>{{ feature.title }}</h3>
                    <p>{{ getShortFeatureDescription(feature.description) }}</p>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </section>

    <!-- Sezione Prossimi Sviluppi -->
    <section class="project-next-steps-section">
      <div class="container">
        <div v-if="project">
          <div class="project-next-steps" v-if="getProjectContent(project.title)?.nextStepsItems">
            <h2>Prossimi sviluppi <span class="animated-dots"><span class="dot dot-1"></span><span class="dot dot-2"></span><span class="dot dot-3"></span></span></h2>
            <p class="next-steps-intro">Clicca su ogni elemento per scoprire i dettagli della roadmap futura:</p>

            <div class="accordion-container">
              <div
                v-for="(step, index) in getProjectContent(project.title).nextStepsItems"
                :key="index"
                class="accordion-item"
                :class="{ 'is-open': openAccordion === index }"
              >
                <button
                  class="accordion-header"
                  @click="toggleAccordion(index)"
                >
                  <span class="accordion-title">{{ step.title }}</span>
                  <span class="accordion-icon">+</span>
                </button>

                <div class="accordion-content">
                  <div class="accordion-body">
                    <p>{{ step.description }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sezione CTA -->
    <section class="project-cta-section">
      <div class="container">
        <div class="project-cta">
          <h2>Hai un progetto simile in mente?</h2>
          <p>Contattaci per discutere come possiamo aiutarti a realizzare la tua visione.</p>
          <div class="cta-buttons">
            <router-link to="/contatti" class="btn primary">
              Iniziamo a parlarne
            </router-link>
            <router-link to="/progetti" class="btn secondary">
              Vedi altri progetti
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Lightbox Modal -->
    <div v-if="showLightbox" class="lightbox-overlay" @click="closeLightbox">
      <div class="lightbox-content" @click.stop>
        <button class="lightbox-close" @click="closeLightbox">&times;</button>
        <img :src="selectedImage?.src" :alt="selectedImage?.title" class="lightbox-image" />
        <div class="lightbox-info">
          <h3>{{ selectedImage?.title }}</h3>
          <p>{{ selectedImage?.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { apiService } from '../services/api.js'

const route = useRoute()
const project = ref(null)
const loading = ref(true)
const error = ref(false)
const selectedImage = ref(null)
const showLightbox = ref(false)
const openAccordion = ref(null)

// Mapping delle immagini per progetto
const projectImages = {
  'Pinbowl': '/src/assets/images/pinbowl.jpg',
  'Hotel Target': '/src/assets/images/hoteltarget_hotel_management.jpg',
  'Vinovero': '/src/assets/images/vinovero_wine_bottles.jpg',
  'IF65': '/src/assets/images/if65_project_management.jpg',
  'CreJob': '/src/assets/images/crejob-students.jpg',
  'Roda': '/src/assets/images/roda_1.png'
}

// Gallery immagini per progetti specifici
const projectGalleries = {
  'Hotel Target': [
    {
      src: '/src/assets/images/hotel-target/LeadBoard.png',
      title: 'LeadBoard Dashboard',
      description: 'Interfaccia principale per la gestione e il tracking dei leads in tempo reale'
    },
    {
      src: '/src/assets/images/hotel-target/Richieste.png',
      title: 'Gestione Richieste',
      description: 'Hub centralizzato per tutte le richieste di prenotazione dai diversi canali'
    },
    {
      src: '/src/assets/images/hotel-target/Preventivi.png',
      title: 'Sistema Preventivi',
      description: 'Template intelligenti per la creazione rapida di preventivi personalizzati'
    },
    {
      src: '/src/assets/images/hotel-target/Prenotazioni.png',
      title: 'Gestione Prenotazioni',
      description: 'Controllo completo del processo di booking e gestione clienti'
    },
    {
      src: '/src/assets/images/hotel-target/Settings.png',
      title: 'Catalogo Strutture',
      description: 'Database completo delle strutture partner con listini e disponibilità'
    }
  ],
  'IF65': [
    {
      src: '/src/assets/images/if65/progetti.png',
      title: 'Command Center Progetti',
      description: 'Dashboard executive per la gestione centralizzata di tutti i progetti del gruppo con vista strategica'
    },
    {
      src: '/src/assets/images/if65/tasks.png',
      title: 'Workflow Engine Tasks',
      description: 'Sistema avanzato di gestione task con automazione e template personalizzabili per processi ricorrenti'
    },
    {
      src: '/src/assets/images/if65/alert.png',
      title: 'Priority Matrix Alert',
      description: 'Sistema di prioritizzazione dinamica con algoritmi intelligenti e visualizzazione heat-map'
    },
    {
      src: '/src/assets/images/if65/avanzamento.png',
      title: 'Business Intelligence Dashboard',
      description: 'Analytics predittive con KPI personalizzati e report automatici per ogni business unit'
    },
    {
      src: '/src/assets/images/if65/tasks_ore.png',
      title: 'Resource Optimization Center',
      description: 'Sistema di allocazione intelligente con time tracking automatico e analisi costi-benefici'
    },
    {
      src: '/src/assets/images/if65/assegnazione.png',
      title: 'Enterprise Risk Management',
      description: 'Piattaforma di risk management con monitoraggio proattivo e piani di contingenza automatizzati'
    }
  ],
  'Roda': [
    {
      src: '/src/assets/images/roda/dati.png',
      title: 'Sistema Gestione Dati',
      description: 'Database relazionale complesso per gestire prodotti, collezioni e varianti con categorizzazione intelligente'
    },
    {
      src: '/src/assets/images/roda/logica.png',
      title: 'Engine Configurazione',
      description: 'Logica sofisticata per selezione opzioni e generazione combinazioni con regole di compatibilità avanzate'
    },
    {
      src: '/src/assets/images/roda/front.png',
      title: 'API Gateway Performance',
      description: 'Sistema di elaborazione richieste ottimizzato per gestire configurazioni e calcolo prezzi in tempo reale'
    },
    {
      src: '/src/assets/images/roda/scalabilita.png',
      title: 'Architettura Scalabile',
      description: 'Infrastruttura enterprise con caching avanzato, load balancing e monitoring per performance costanti'
    }
  ],
  'Vinovero': [
    {
      src: '/src/assets/images/vinovero/produttori.png',
      title: 'Anagrafica Produttori Unificata',
      description: 'Sistema centralizzato per gestire produttori e distributori di vini naturali con condivisione automatica del know-how'
    },
    {
      src: '/src/assets/images/vinovero/ordini.png',
      title: 'Sistema Ordini ERP',
      description: 'Workflow di autorizzazione ordini con permessi granulari e dashboard unificata per tutti i punti vendita'
    },
    {
      src: '/src/assets/images/vinovero/magazzino.png',
      title: 'Gestione Magazzino Digitale',
      description: 'Mappatura completa del magazzino con indicazioni precise di scaffale, colonna e ubicazione per ogni prodotto'
    },
    {
      src: '/src/assets/images/vinovero/fatturato.png',
      title: 'Centro Controllo Finanziario',
      description: 'Dashboard analytics con differenziazione centri di costo e separazione incassi negozi fisici ed e-commerce'
    },
    {
      src: '/src/assets/images/vinovero/barcode.png',
      title: 'AI Wine Recognition',
      description: 'Sistema di riconoscimento automatico etichette tramite webcam per monitoraggio vendita al bicchiere'
    }
  ],
  'CreJob': [
    {
      src: '/src/assets/images/crejob/ricerca.png',
      title: 'Motore Ricerca Avanzato',
      description: 'Sistema di ricerca intelligente per esplorare soggiorni, tirocini e corsi all\'estero con filtri avanzati'
    },
    {
      src: '/src/assets/images/crejob/risultati.png',
      title: 'Sistema Carrello Prenotazioni',
      description: 'Esperienza di prenotazione fluida con carrello multi-selezione e validazione in tempo reale'
    },
    {
      src: '/src/assets/images/crejob/accommodation.png',
      title: 'Engine Regole Business',
      description: 'Backend sofisticato con logiche personalizzate per gestione automatica intervalli e compatibilità'
    },
    {
      src: '/src/assets/images/crejob/adminpanel.png',
      title: 'Dashboard Gestione Utenti',
      description: 'Pannello di controllo personalizzato per visualizzazione e gestione completa delle prenotazioni'
    }
  ],
  'Pinbowl': [
    {
      src: '/src/assets/images/pinbowl/calendario.png',
      title: 'Sistema Gestione Lezioni',
      description: 'Pianificazione intelligente di lezioni con gestione orari, istruttori e aree specifiche dello skatepark'
    },
    {
      src: '/src/assets/images/pinbowl/skaters.png',
      title: 'Database Clienti CRM',
      description: 'Sistema CRM completo per gestire dati clienti, feedback e relazioni con assistenza dedicata'
    },
    {
      src: '/src/assets/images/pinbowl/viola.png',
      title: 'Engine Marketing Comunicazione',
      description: 'Piattaforma integrata per campagne email marketing, social media e strategie multi-canale'
    },
    {
      src: '/src/assets/images/pinbowl/login.png',
      title: 'Sistema Fatturazione Automatizzato',
      description: 'Automazione completa fatturazione con gestione pagamenti online e controllo flusso di cassa'
    }
  ]
}

// Funzione per ottenere l'immagine del progetto
const getProjectImage = (projectTitle) => {
  return projectImages[projectTitle] || null
}

// Funzione per dividere le tecnologie in array
const getTechnologies = (techString) => {
  if (!techString) return []
  return techString.split(',').map(tech => tech.trim())
}

// Funzioni per la gallery
const getProjectGallery = (projectTitle) => {
  return projectGalleries[projectTitle] || []
}

// Funzione per matchare le schermate con le funzionalità
const getMatchingScreenshot = (featureTitle) => {
  const gallery = getProjectGallery(project.value?.title)

  // Mapping tra titoli delle funzionalità e schermate
  const featureToScreenshot = {
    // Hotel Target
    'LeadBoard': 'LeadBoard Dashboard',
    'Gestione Richieste Centralizzata': 'Gestione Richieste',
    'Sistema di Preventivazione Avanzato': 'Sistema Preventivi',
    'Gestione Prenotazioni Completa': 'Gestione Prenotazioni',
    'Catalogo Strutture Dinamico': 'Catalogo Strutture',
    // IF65 - Mapping 1:1 tra funzionalità e schermate
    'Gestione Progetti Centralizzata': 'Command Center Progetti',
    'Sistema Task Intelligente': 'Workflow Engine Tasks',
    'Gestione Priorità Avanzata': 'Priority Matrix Alert',
    'Monitoraggio e Analytics': 'Business Intelligence Dashboard',
    'Gestione Risorse e Ore': 'Resource Optimization Center',
    'Risk Management Integrato': 'Enterprise Risk Management',
    // Roda - Mapping 1:1 tra funzionalità e schermate
    'Sistema Gestione Dati Avanzato': 'Sistema Gestione Dati',
    'Engine di Configurazione Intelligente': 'Engine Configurazione',
    'API Gateway Performante': 'API Gateway Performance',
    'Architettura Scalabile Enterprise': 'Architettura Scalabile',
    // Vinovero - Mapping 1:1 tra funzionalità e schermate
    'Anagrafica Unificata Produttori': 'Anagrafica Produttori Unificata',
    'Sistema Ordini Intelligente': 'Sistema Ordini ERP',
    'Gestione Magazzino Avanzata': 'Gestione Magazzino Digitale',
    'Centro Controllo Finanziario': 'Centro Controllo Finanziario',
    'AI-Powered Wine Recognition': 'AI Wine Recognition',
    // CreJob - Mapping 1:1 tra funzionalità e schermate
    'Motore di Ricerca Avanzato': 'Motore Ricerca Avanzato',
    'Sistema Carrello Intelligente': 'Sistema Carrello Prenotazioni',
    'Engine Regole Business': 'Engine Regole Business',
    'Dashboard Gestione Prenotazioni': 'Dashboard Gestione Utenti',
    // Pinbowl - Mapping 1:1 tra funzionalità e schermate
    'Sistema Gestione Lezioni Avanzato': 'Sistema Gestione Lezioni',
    'Database Clienti Centralizzato': 'Database Clienti CRM',
    'Engine Marketing e Comunicazione': 'Engine Marketing Comunicazione',
    'Sistema Fatturazione Automatizzato': 'Sistema Fatturazione Automatizzato'
  }

  const screenshotTitle = featureToScreenshot[featureTitle]
  return gallery.find(img => img.title === screenshotTitle)
}

const openLightbox = (image) => {
  selectedImage.value = image
  showLightbox.value = true
}

const closeLightbox = () => {
  showLightbox.value = false
  selectedImage.value = null
}

// Funzione per determinare se usare layout verticale
const isVerticalLayout = (index) => {
  // Layout verticale per le funzionalità più importanti (indici 0, 2, 4)
  return index % 2 === 0
}

// Funzione per accorciare le descrizioni delle funzionalità
const getShortFeatureDescription = (description) => {
  // Limite più generoso per mantenere il senso completo
  if (description.length > 200) {
    // Trova l'ultimo punto o virgola prima del limite per non tagliare a metà frase
    const cutPoint = description.lastIndexOf('.', 200) || description.lastIndexOf(',', 200) || 200
    return description.substring(0, cutPoint) + '...'
  }
  return description
}

// Funzione per gestire l'accordion
const toggleAccordion = (index) => {
  if (openAccordion.value === index) {
    openAccordion.value = null // Chiude se è già aperto
  } else {
    openAccordion.value = index // Apre il nuovo
  }
}

// Contenuti specifici per ogni progetto
const getProjectContent = (projectTitle) => {
  const contents = {
    'Hotel Target': {
      challenge: 'Hotel Target è una realtà dinamica e in continua crescita specializzata nella consulenza per strutture alberghiere. Marco, il fondatore, si trovava ad affrontare una sfida critica: l\'organizzazione efficiente del lavoro in un settore che richiede la gestione simultanea di attività di marketing e sales.',
      objective: 'Sviluppare un prodotto web proprietario che potesse offrire funzionalità specifiche per il settore alberghiero, superando i limiti dei software CRM standard e centralizzando tutti i processi aziendali.',
      solution: 'Un CRM (Customer Relationship Management) su misura per il settore della consulenza alberghiera, integrando funzionalità specifiche che rispondono alle esigenze uniche di Hotel Target.',
      features: [
        {
          title: 'LeadBoard',
          description: 'Dashboard intelligente per tracciare ogni lead in tempo reale attraverso tutte le fasi del customer journey, con automazione delle notifiche per ottimizzare le conversioni.'
        },
        {
          title: 'Gestione Richieste Centralizzata',
          description: 'Hub unificato che raccoglie automaticamente tutte le richieste di prenotazione dai diversi canali digitali, garantendo zero opportunità perse.'
        },
        {
          title: 'Sistema di Preventivazione Avanzato',
          description: 'Template intelligenti per email, proposte e contratti che riducono del 70% il tempo di risposta mantenendo consistenza nella comunicazione.'
        },
        {
          title: 'Gestione Prenotazioni Completa',
          description: 'Controllo totale del processo di booking con registrazione automatica delle informazioni clienti e storico completo sempre aggiornato.'
        },
        {
          title: 'Catalogo Strutture Dinamico',
          description: 'Database completo delle strutture partner con listini, promozioni e gallerie fotografiche aggiornate in tempo reale.'
        }
      ],
      results: [
        '+150% efficienza nella gestione dei lead',
        '-70% tempo di risposta alle richieste clienti',
        '+200% organizzazione dei processi interni',
        'Zero richieste perse grazie alla centralizzazione'
      ],
      nextStepsItems: [
        {
          title: 'Dashboard Analytics Avanzate',
          description: 'Report dettagliati su performance dell\'agenzia, analisi dei trend di prenotazione e monitoraggio dei ricavi in tempo reale.'
        },
        {
          title: 'Intelligenza Artificiale',
          description: 'Sistema di raccomandazioni automatiche per ottimizzare le proposte ai clienti e migliorare il tasso di conversione.'
        },
        {
          title: 'App Mobile',
          description: 'Applicazione mobile nativa per gestire leads, richieste e prenotazioni direttamente da smartphone e tablet.'
        },
        {
          title: 'Integrazione Booking Engine',
          description: 'Connessione diretta con i principali booking engine del settore per sincronizzazione automatica di disponibilità e prezzi.'
        }
      ],
      testimonial: {
        text: 'Il CRM sviluppato da Mumble ha rivoluzionato il nostro modo di lavorare. Quello che prima richiedeva ore di lavoro manuale, ora viene gestito automaticamente. La nostra produttività è aumentata drasticamente.',
        author: 'Marco, Fondatore Hotel Target'
      }
    },
    'IF65': {
      challenge: 'IF65, gruppo aziendale italiano con diverse società operative in settori complementari, si trovava ad affrontare la sfida della gestione frammentata dei progetti. Ogni divisione utilizzava strumenti diversi, creando inefficienze e perdita di visibilità sui processi trasversali.',
      objective: 'Creare un ecosistema digitale unificato che permettesse ai project manager di orchestrare progetti complessi attraverso multiple business unit, garantendo trasparenza, controllo delle risorse e allineamento strategico a livello di gruppo.',
      solution: 'Una piattaforma enterprise di project management progettata per gestire la complessità organizzativa di un gruppo multi-business, con dashboard centralizzate, workflow automatizzati e intelligence operativa avanzata.',
      features: [
        {
          title: 'Gestione Progetti Centralizzata',
          description: 'Dashboard unificata per monitorare tutti i progetti del gruppo in tempo reale. Visibilità completa su stato, risorse e milestone con controllo granulare per ogni divisione aziendale.'
        },
        {
          title: 'Sistema Task Intelligente',
          description: 'Creazione, assegnazione e tracciamento avanzato di task con template personalizzabili. Automazione dei flussi di lavoro ricorrenti e notifiche smart per il team.'
        },
        {
          title: 'Gestione Priorità Avanzata',
          description: 'Sistema di prioritizzazione intelligente che bilancia urgenza, impatto business e disponibilità risorse. Indicatori visivi per identificare immediatamente i progetti critici.'
        },
        {
          title: 'Monitoraggio e Analytics',
          description: 'Dashboard avanzate con KPI personalizzati e analytics predittive per ogni business unit. Report automatici che identificano trend, colli di bottiglia e opportunità di miglioramento.'
        },
        {
          title: 'Gestione Risorse e Ore',
          description: 'Sistema di allocazione ottimizzata delle risorse tra progetti e divisioni. Time tracking dettagliato con analisi costi-benefici e previsioni budget accurate.'
        },
        {
          title: 'Risk Management Integrato',
          description: 'Monitoraggio proattivo di rischi operativi, dipendenze critiche e impatti cross-business. Sistema di allerta automatico con piani di contingenza predefiniti.'
        }
      ],
      results: [
        '+65% efficienza nella gestione progetti cross-divisionale',
        '-50% tempo di coordinamento tra business unit',
        '+200% visibilità operativa a livello di gruppo',
        '90% riduzione errori di allocazione risorse',
        'ROI del 300% nel primo anno di implementazione'
      ],
      nextStepsItems: [
        {
          title: 'Integrazione Sistemi Tempo',
          description: 'Connessione con strumenti di time tracking per automatizzare la registrazione delle ore e migliorare la precisione del controllo costi.'
        },
        {
          title: 'Strumenti Comunicazione',
          description: 'Integrazione con piattaforme di comunicazione aziendale per centralizzare discussioni e decisioni all\'interno dei progetti.'
        },
        {
          title: 'Condivisione Documenti',
          description: 'Sistema avanzato di document management con versioning, permessi granulari e sincronizzazione cloud per collaborazione seamless.'
        },
        {
          title: 'Analytics Predittive',
          description: 'Algoritmi di machine learning per prevedere ritardi, identificare colli di bottiglia e suggerire ottimizzazioni dei processi.'
        }
      ],
      testimonial: {
        text: 'Mumble ha creato per noi molto più di una piattaforma di project management: un vero sistema nervoso digitale che connette tutte le nostre divisioni. La trasformazione operativa è stata straordinaria.',
        author: 'Chief Operations Officer, IF65 Group'
      }
    },
    'Roda': {
      challenge: 'Roda, eccellenza del made in Italy nel settore dell\'arredamento outdoor, necessitava di un configuratore web avanzato per valorizzare i propri prodotti di alta gamma, creando un\'esperienza digitale che permettesse personalizzazione e visualizzazione di combinazioni uniche.',
      objective: 'Sviluppare un sistema backend robusto per un configuratore web che permettesse personalizzazione intuitiva di mobili e accessori, semplificazione del processo di selezione e visualizzazione chiara dei prodotti configurati.',
      solution: 'Un backend enterprise progettato per gestire la complessità di un configuratore di arredamento di lusso, con architettura scalabile, logiche di configurazione avanzate e integrazione seamless con il frontend per performance ottimali.',
      features: [
        {
          title: 'Sistema Gestione Dati Avanzato',
          description: 'Database relazionale complesso per gestire prodotti, collezioni e varianti con tutte le opzioni di personalizzazione. Categorizzazione intelligente con relazioni ottimizzate per performance.'
        },
        {
          title: 'Engine di Configurazione Intelligente',
          description: 'Logica sofisticata per selezione opzioni e generazione combinazioni validate. Gestione automatica delle relazioni tra elementi con regole di compatibilità avanzate.'
        },
        {
          title: 'API Gateway Performante',
          description: 'Sistema di elaborazione richieste ottimizzato per gestire selezioni, modifiche e calcolo prezzi in tempo reale. Architettura RESTful per comunicazione fluida.'
        },
        {
          title: 'Architettura Scalabile Enterprise',
          description: 'Infrastruttura per traffico elevato con caching avanzato, ottimizzazione query e load balancing. Monitoring e auto-scaling per performance costanti.'
        }
      ],
      results: [
        '+300% engagement utenti sul configuratore',
        '-60% tempo di configurazione prodotti',
        '99.9% uptime anche con picchi di traffico',
        '+150% conversioni da configurazione ad acquisto',
        'Scalabilità testata fino a 10.000 utenti simultanei'
      ],
      nextStepsItems: [
        {
          title: 'Integrazione Sistema Ordini',
          description: 'Connessione diretta con il sistema di gestione ordini per automatizzare il processo di acquisto dalle configurazioni salvate, con workflow di approvazione e tracking.'
        },
        {
          title: 'Gestione Inventario Real-time',
          description: 'Integrazione con sistema di inventario per verificare disponibilità effettiva dei prodotti selezionati e aggiornare automaticamente le opzioni disponibili.'
        },
        {
          title: 'Visualizzazione 3D Avanzata',
          description: 'Implementazione di rendering 3D fotorealistico per permettere ai clienti di visualizzare le configurazioni in ambienti virtuali realistici.'
        },
        {
          title: 'AI-Powered Recommendations',
          description: 'Sistema di intelligenza artificiale per suggerire combinazioni ottimali basate su preferenze utente, trend di mercato e compatibilità estetica.'
        }
      ],
      testimonial: {
        text: 'Il configuratore sviluppato da Mumble ha trasformato completamente la nostra esperienza di vendita online. I clienti ora possono creare le loro composizioni ideali con una facilità incredibile.',
        author: 'Digital Manager, Roda'
      }
    },
    'Vinovero': {
      challenge: 'VinoVero, punto di riferimento per vini naturali, stava espandendo con nuovi punti vendita in Italia, Portogallo e Spagna. La crescita geografica richiedeva gestione unificata dei flussi di lavoro e controllo centralizzato delle operazioni multi-location.',
      objective: 'Sviluppare un sistema ERP completo per unificare i processi tra tutti i punti vendita, centralizzare l\'anagrafica produttori, automatizzare le autorizzazioni ordini e implementare il monitoraggio innovativo della vendita al bicchiere.',
      solution: 'Un ERP enterprise su misura che integra tutti i flussi operativi: dalla gestione acquisti alla contabilità, dal controllo magazzino alla cassa, fino al monitoraggio della vendita al bicchiere tramite intelligenza artificiale.',
      features: [
        {
          title: 'Anagrafica Unificata Produttori',
          description: 'Sistema centralizzato per gestire produttori e distributori di vini naturali con condivisione automatica del know-how. Alert intelligenti per evidenziare le new entry del settore.'
        },
        {
          title: 'Sistema Ordini Intelligente',
          description: 'Workflow di autorizzazione ordini con permessi granulari. Dashboard unificata con visualizzazione stato in tempo reale: programmato, autorizzato, consegnato e fatturato.'
        },
        {
          title: 'Gestione Magazzino Avanzata',
          description: 'Mappatura digitale completa con indicazioni precise di scaffale, colonna e ubicazione. Sistema ottimizzato per alta rotazione con ricerca rapida e gestione automatica giacenze.'
        },
        {
          title: 'Centro Controllo Finanziario',
          description: 'Dashboard analytics per risultati dell\'attività con differenziazione centri di costo. Separazione intelligente tra incassi negozi fisici e revenue e-commerce.'
        },
        {
          title: 'AI-Powered Wine Recognition',
          description: 'Tecnologia innovativa che combina intelligenza artificiale e web app per monitoraggio vendita al bicchiere. Riconoscimento automatico etichette tramite webcam.'
        }
      ],
      results: [
        '100% unificazione processi tra tutti i punti vendita',
        '-70% tempo gestione ordini e autorizzazioni',
        '+200% efficienza nella gestione magazzino',
        'Real-time tracking vendite al bicchiere',
        'ROI 250% nel primo anno di implementazione'
      ],
      nextStepsItems: [
        {
          title: 'E-commerce Avanzato',
          description: 'Integrazione piattaforma e-commerce con sincronizzazione automatica inventario, gestione spedizioni e sistema di raccomandazioni personalizzate per clienti.'
        },
        {
          title: 'Sistema Fidelizzazione',
          description: 'Programma loyalty multi-location con punti, sconti personalizzati e eventi esclusivi per valorizzare i clienti più fedeli della community vini naturali.'
        },
        {
          title: 'Analytics Predittive',
          description: 'Algoritmi di machine learning per prevedere domanda, ottimizzare stock e suggerire acquisti basati su stagionalità e trend del mercato vini naturali.'
        },
        {
          title: 'Marketplace B2B',
          description: 'Piattaforma per connettere direttamente produttori e rivenditori specializzati, facilitando scoperta di nuovi vini e ottimizzazione della supply chain.'
        }
      ],
      testimonial: {
        text: 'Mumble ha creato per noi molto più di un gestionale: un vero ecosistema digitale che ha unificato tutte le nostre location. Ora gestiamo l\'espansione internazionale con la stessa facilità di un singolo negozio.',
        author: 'Founder, VinoVero'
      }
    },
    'CreJob': {
      challenge: 'CreJob, azienda di consulenza specializzata in esperienze formative all\'estero per giovani studenti, gestiva un network consolidato di opportunità in tutta Europa ma necessitava di una piattaforma digitale per automatizzare il processo di prenotazione.',
      objective: 'Sviluppare una piattaforma online completa per semplificare prenotazioni e gestione soggiorni, migliorare l\'esperienza utente, automatizzare i flussi operativi e centralizzare la gestione di opportunità formative europee.',
      solution: 'Una piattaforma web moderna che integra ricerca avanzata, sistema di prenotazione intelligente, gestione automatizzata delle regole business e pannello di controllo completo, ottimizzando l\'intero customer journey delle esperienze internazionali.',
      features: [
        {
          title: 'Motore di Ricerca Avanzato',
          description: 'Sistema di ricerca intelligente per esplorare soggiorni, tirocini e corsi all\'estero. Filtri avanzati per tipologia, settore, località e durata con dettagli completi e immagini.'
        },
        {
          title: 'Sistema Carrello Intelligente',
          description: 'Esperienza di prenotazione fluida con carrello multi-selezione. Gestione automatica disponibilità e validazione in tempo reale delle combinazioni selezionate.'
        },
        {
          title: 'Engine Regole Business',
          description: 'Backend sofisticato con logiche personalizzate per esigenze operative. Gestione automatica intervalli prenotazioni e validazione compatibilità alloggi.'
        },
        {
          title: 'Dashboard Gestione Prenotazioni',
          description: 'Pannello di controllo personalizzato per utenti registrati con visualizzazione completa prenotazioni. Funzionalità di modifica, cancellazione e tracking stato.'
        }
      ],
      results: [
        '+400% efficienza nel processo di prenotazione',
        '-80% tempo gestione amministrativa',
        '95% soddisfazione utenti sulla piattaforma',
        '+250% crescita prenotazioni online',
        'Automazione completa delle regole business'
      ],
      nextStepsItems: [
        {
          title: 'Modulo Marketing Avanzato',
          description: 'Sistema di acquisizione utenti con campagne mirate, referral program e strumenti di engagement per attrarre nuovi studenti e aumentare le conversioni.'
        },
        {
          title: 'Sistema Recensioni e Rating',
          description: 'Piattaforma di feedback per valutare esperienze, alloggi e tirocini con sistema di rating che aiuti futuri utenti nelle decisioni di prenotazione.'
        },
        {
          title: 'Pagamenti Internazionali',
          description: 'Integrazione gateway di pagamento multi-valuta con supporto per metodi di pagamento locali europei e gestione automatica dei cambi.'
        },
        {
          title: 'Analytics e Ottimizzazione',
          description: 'Dashboard business intelligence per analizzare performance, trend di prenotazione e comportamenti utenti per ottimizzazione continua della piattaforma.'
        }
      ],
      testimonial: {
        text: 'La piattaforma sviluppata da Mumble ha rivoluzionato il nostro modo di operare. Quello che prima richiedeva giorni di lavoro manuale, ora viene gestito automaticamente con un\'esperienza utente eccezionale.',
        author: 'Team Lead, CreJob'
      }
    },
    'Pinbowl': {
      challenge: 'Pinbowl, il più grande skatepark indoor d\'Europa gestito da Fabio e Viola, necessitava di un sistema completo per ottimizzare la gestione di corsi, insegnanti, campus estivi e tutta la complessa amministrazione di una struttura sportiva di questa portata.',
      objective: 'Sviluppare un gestionale modulare per monitorare le prestazioni del parco, ottimizzare la gestione di corsi e istruttori, automatizzare i processi amministrativi e migliorare l\'esperienza cliente con analisi del flusso di cassa.',
      solution: 'Un sistema gestionale modulare costruito nel tempo, dove ogni modulo si integra perfettamente: gestione lezioni, clienti, marketing, amministrazione, reporting, risorse umane e servizio clienti per una gestione completa dello skatepark.',
      features: [
        {
          title: 'Sistema Gestione Lezioni Avanzato',
          description: 'Pianificazione intelligente di lezioni con gestione orari, istruttori e aree specifiche. Prevenzione automatica sovrapposizioni e tracking completo partecipanti con storico.'
        },
        {
          title: 'Database Clienti Centralizzato',
          description: 'Sistema CRM completo per gestire dati clienti con funzionalità feedback integrata. Gestione relazioni ottimizzata con assistenza dedicata e supporto tecnico.'
        },
        {
          title: 'Engine Marketing e Comunicazione',
          description: 'Piattaforma integrata per promuovere lezioni attraverso campagne email marketing automatizzate, gestione social media e strategie multi-canale.'
        },
        {
          title: 'Sistema Fatturazione Automatizzato',
          description: 'Automazione completa fatturazione con gestione pagamenti online integrata. Miglioramento gestione finanziaria e controllo ottimale del flusso di cassa.'
        }
      ],
      results: [
        '+300% efficienza nella gestione lezioni e istruttori',
        '-70% tempo processi amministrativi',
        '+150% engagement clienti tramite marketing automation',
        '99% accuratezza nella fatturazione automatizzata',
        'Real-time monitoring delle performance del parco'
      ],
      nextStepsItems: [
        {
          title: 'Analytics Avanzate Performance',
          description: 'Sistema di reporting dettagliato per analizzare performance del parco, trend di utilizzo e insights operativi per decisioni strategiche data-driven.'
        },
        {
          title: 'App Mobile Clienti',
          description: 'Applicazione mobile per prenotazione lezioni, tracking progressi personali, community features e notifiche push per eventi e promozioni.'
        },
        {
          title: 'Sistema Loyalty Program',
          description: 'Programma fedeltà integrato con punti, rewards e sconti personalizzati per incentivare la frequentazione e premiare i clienti più assidui.'
        },
        {
          title: 'IoT e Sensori Smart',
          description: 'Integrazione sensori IoT per monitoraggio automatico utilizzo aree, sicurezza e manutenzione predittiva delle attrezzature dello skatepark.'
        }
      ],
      testimonial: {
        text: 'Il gestionale sviluppato da Mumble ha trasformato completamente la nostra operatività. Ora possiamo concentrarci su quello che amiamo di più: far crescere la community dello skateboard.',
        author: 'Fabio & Viola, Founders Pinbowl'
      }
    }
  }

  return contents[projectTitle] || null
}

// Carica il progetto dal backend
onMounted(async () => {
  try {
    const projectId = route.params.id
    const data = await apiService.getProjects()
    const foundProject = data.find(p => p.id.toString() === projectId)

    if (foundProject) {
      project.value = foundProject
    } else {
      error.value = true
    }
  } catch (err) {
    console.error('Error loading project:', err)
    error.value = true
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
.project-detail-page {
  min-height: 100vh;
}

/* Sezioni con sfondi alternati */
.project-hero-section {
  background: var(--bg);
  padding: 80px 0;
}

.project-story-section {
  background: var(--chip-bg);
  padding: 60px 0;
}

.project-features-section {
  background: var(--bg);
  padding: 60px 0;
}

.project-next-steps-section {
  background: var(--chip-bg);
  padding: 60px 0;
}

.project-cta-section {
  background: var(--bg);
  padding: 80px 0;
}

.loading, .error-state {
  text-align: center;
  padding: 80px 20px;
  color: var(--muted);
}

.error-state h2 {
  color: var(--fg);
  margin-bottom: 16px;
}

/* Breadcrumb */
.breadcrumb {
  margin-bottom: 40px;
  font-family: var(--font-mono);
  font-size: 14px;
}

.breadcrumb-link {
  color: var(--muted);
  text-decoration: none;
  transition: color 0.2s ease;
}

.breadcrumb-link:hover {
  color: var(--fg);
}

.breadcrumb-separator {
  margin: 0 8px;
  color: var(--muted);
}

.breadcrumb-current {
  color: var(--fg);
  font-weight: 500;
}

/* Hero del progetto */
.project-hero {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 80px;
  align-items: center;
  margin-bottom: 100px;
}

.project-meta-header {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
}

.project-category {
  background: var(--sage);
  color: white;
  padding: 6px 16px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 500;
  font-family: var(--font-mono);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.project-client {
  background: var(--warm-clay);
  color: white;
  padding: 6px 16px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 500;
  font-family: var(--font-mono);
}

.hero-title {
  font-size: clamp(48px, 8vw, 64px);
  margin: 0 0 24px;
  font-weight: 300;
  line-height: 1.1;
  color: var(--fg);
  letter-spacing: -0.01em;
}

.project-lead {
  font-size: 22px;
  line-height: 1.5;
  color: var(--muted);
  margin: 0 0 40px;
  max-width: 90%;
}

.project-tech-header {
  margin-bottom: 40px;
}

.project-tech-header h3 {
  font-size: 16px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
  font-weight: 500;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 0;
}

.tech-tag {
  background: var(--line);
  color: var(--muted);
  padding: 6px 12px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 500;
  font-family: var(--font-mono);
  transition: all 0.2s ease;
}

.tech-tag:hover {
  background: var(--sage);
  color: white;
}

.project-actions {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

.project-hero-image {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-image {
  width: 100%;
  height: 400px;
  object-fit: cover;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

/* Sezione storia del progetto */
.project-story {
  /* Background e padding gestiti dalla sezione esterna */
}

.story-content {
  max-width: none;
  margin: 0;
}

.story-challenge {
  margin-bottom: 40px;
}

.story-challenge h2 {
  font-size: 28px;
  margin: 0 0 20px;
  color: var(--fg);
  font-family: var(--font-mono);
  font-weight: 600;
  position: relative;
  padding-bottom: 12px;
}

.story-challenge h2::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 60px;
  height: 3px;
  background: var(--sage);
  border-radius: 2px;
}

.story-challenge p {
  font-size: 18px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
  text-align: left;
  font-weight: 400;
}

.story-highlights {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
}

.highlight-item h2 {
  font-size: 22px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
  font-weight: 600;
  position: relative;
  padding-bottom: 10px;
}

.highlight-item:first-child h2::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 40px;
  height: 3px;
  background: var(--warm-clay);
  border-radius: 2px;
}

.highlight-item:last-child h2::after {
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

/* Sezione funzionalità con schermate */
.project-features {
  background: var(--chip-bg);
  border-radius: 24px;
  padding: 60px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  border: 1px solid var(--line);
}

.project-features h2 {
  font-size: 32px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
  text-align: center;
}

.features-subtitle {
  font-size: 18px;
  color: var(--muted);
  text-align: center;
  margin: 0 0 60px;
  max-width: 60ch;
  margin-left: auto;
  margin-right: auto;
}

.features-with-images {
  display: flex;
  flex-direction: column;
  gap: 60px;
}

.feature-with-image {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: center;
}

.feature-with-image.reverse {
  direction: rtl;
}

.feature-with-image.reverse > * {
  direction: ltr;
}

/* Allineamento specifico per le card orizzontali */
.feature-with-image:not(.vertical) {
  align-items: stretch;
}

.feature-with-image:not(.vertical) .feature-content,
.feature-with-image:not(.vertical) .feature-screenshot {
  display: flex;
  flex-direction: column;
}

.feature-with-image:not(.vertical) .screenshot-container {
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* Layout verticale per funzionalità importanti */
.feature-with-image.vertical {
  grid-template-columns: 1fr;
  gap: 30px;
  text-align: center;
  max-width: 700px;
  margin: 0 auto;
}

.feature-with-image.vertical .feature-screenshot {
  order: -1;
}

.feature-with-image.vertical .screenshot-container {
  max-width: 600px;
  margin: 0 auto;
}

.feature-with-image.vertical .feature-content {
  padding: 32px 40px;
}

.feature-content {
  padding: 32px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
}

.feature-content h3 {
  font-size: 22px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
  font-weight: 600;
}

.feature-content p {
  font-size: 18px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
}

.feature-screenshot {
  position: relative;
}

.screenshot-container {
  position: relative;
  cursor: pointer;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  transition: all 0.3s ease;
  background: white;
  padding: 20px;
}

.screenshot-container:hover {
  transform: translateY(-8px);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.2);
}

.screenshot-image {
  width: 100%;
  height: auto;
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.screenshot-container:hover .screenshot-image {
  transform: scale(1.02);
}

.screenshot-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 12px;
}

.screenshot-container:hover .screenshot-overlay {
  opacity: 1;
}

.zoom-icon {
  color: white;
  font-size: 16px;
  font-family: var(--font-mono);
  font-weight: 500;
  text-align: center;
  padding: 12px 24px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  backdrop-filter: blur(10px);
}

/* Sezione gallery */
.project-gallery {
  background: var(--bg);
  padding: 80px 0;
  margin: 80px 0;
}

.project-gallery h2 {
  font-size: 32px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
  text-align: center;
}

.gallery-subtitle {
  font-size: 18px;
  color: var(--muted);
  text-align: center;
  margin: 0 0 48px;
  max-width: 60ch;
  margin-left: auto;
  margin-right: auto;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 24px;
}

.gallery-item {
  cursor: pointer;
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.gallery-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
}

.gallery-image {
  position: relative;
  background: white;
  border-radius: 12px;
  overflow: hidden;
}

.gallery-image img {
  width: 100%;
  height: 250px;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.gallery-item:hover .gallery-image img {
  transform: scale(1.05);
}

.gallery-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
  color: white;
  padding: 24px;
  transform: translateY(100%);
  transition: transform 0.3s ease;
}

.gallery-item:hover .gallery-overlay {
  transform: translateY(0);
}

.gallery-overlay h4 {
  font-size: 18px;
  margin: 0 0 8px;
  font-family: var(--font-mono);
  font-weight: 600;
}

.gallery-overlay p {
  font-size: 14px;
  margin: 0 0 8px;
  line-height: 1.4;
}

.gallery-zoom {
  font-size: 12px;
  opacity: 0.8;
  font-family: var(--font-mono);
}

/* Lightbox */
.lightbox-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 20px;
}

.lightbox-content {
  position: relative;
  max-width: 800px;
  max-height: 600px;
  width: 90vw;
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.lightbox-close {
  position: absolute;
  top: 16px;
  right: 16px;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 24px;
  cursor: pointer;
  z-index: 1001;
  transition: background 0.2s ease;
}

.lightbox-close:hover {
  background: rgba(0, 0, 0, 0.9);
}

.lightbox-image {
  width: 100%;
  height: auto;
  max-height: 400px;
  object-fit: contain;
}

.lightbox-info {
  padding: 24px;
  background: white;
}

.lightbox-info h3 {
  font-size: 20px;
  margin: 0 0 12px;
  color: var(--fg);
  font-family: var(--font-mono);
}

.lightbox-info p {
  font-size: 16px;
  color: var(--muted);
  margin: 0;
  line-height: 1.5;
}

/* Sezione roadmap/timeline rinnovata */
.project-next-steps {
  /* Rimosso max-width per allineare con la sezione CTA */
}

.roadmap-header {
  text-align: center;
  margin-bottom: 80px;
}

.roadmap-timeline {
  position: relative;
}

.timeline-item {
  display: flex;
  gap: 32px;
  margin-bottom: 40px;
  position: relative;
}

.timeline-item:last-child {
  margin-bottom: 0;
}

.timeline-marker {
  flex-shrink: 0;
  position: relative;
  z-index: 2;
}

.marker-number {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, var(--sage), var(--warm-clay));
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-weight: 600;
  font-size: 18px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.marker-line {
  position: absolute;
  top: 48px;
  left: 50%;
  transform: translateX(-50%);
  width: 2px;
  height: 72px;
  background: linear-gradient(180deg, var(--sage), var(--warm-clay));
  opacity: 0.3;
}

.timeline-content {
  flex: 1;
  background: white;
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  border: 1px solid var(--line);
  overflow: hidden;
  transition: all 0.3s ease;
}

.timeline-content:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.12);
}

.timeline-header {
  width: 100%;
  padding: 32px;
  background: none;
  border: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: left;
}

.timeline-header:hover {
  background: rgba(163, 177, 138, 0.02);
}

.timeline-title-section {
  flex: 1;
}

.timeline-title {
  font-size: 24px;
  font-family: var(--font-mono);
  font-weight: 600;
  color: var(--fg);
  margin: 0 0 8px;
  transition: color 0.3s ease;
}

.timeline-header:hover .timeline-title {
  color: var(--sage);
}

.timeline-status {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 500;
  color: var(--warm-clay);
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 4px 12px;
  background: rgba(176, 128, 54, 0.1);
  border-radius: 12px;
}

.timeline-toggle {
  color: var(--muted);
  transition: all 0.3s ease;
}

.timeline-item.is-open .timeline-toggle {
  transform: rotate(180deg);
  color: var(--sage);
}

.timeline-details {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease;
}

.timeline-item.is-open .timeline-details {
  max-height: 300px;
}

.timeline-body {
  padding: 0 32px 32px;
  border-top: 1px solid var(--line);
  margin-top: 0;
}

.timeline-body p {
  font-size: 16px;
  line-height: 1.6;
  color: var(--muted);
  margin: 24px 0;
}

.timeline-meta {
  display: flex;
  gap: 24px;
  margin-top: 20px;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 14px;
  color: var(--muted);
  font-weight: 500;
}

.meta-item svg {
  color: var(--sage);
}

/* Punti animati */
.animated-dots {
  display: flex;
  gap: 8px;
  align-items: center;
  margin-left: 4px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

.dot-1 {
  background: var(--sage);
  animation-delay: 0s;
}

.dot-2 {
  background: var(--warm-clay);
  animation-delay: 0.3s;
}

.dot-3 {
  background: var(--muted);
  animation-delay: 0.6s;
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.3;
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(1.2);
  }
}

/* Sezione prossimi sviluppi */
.project-next-steps h2 {
  font-size: 32px;
  margin: 0 0 8px;
  color: var(--fg);
  font-family: var(--font-mono);
  font-weight: 600;
  text-align: left;
  display: flex;
  align-items: center;
  gap: 16px;
}

.next-steps-intro {
  font-size: 18px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0 0 32px;
  text-align: left;
  max-width: 60ch;
}

/* Accordion Styles */
.accordion-container {
  max-width: none;
  margin: 0;
}

.accordion-item {
  border-bottom: 1px solid var(--line);
  transition: all 0.3s ease;
}

.accordion-item:last-child {
  border-bottom: none;
}

.accordion-item.is-open {
  border-bottom: none;
}

.accordion-header {
  width: 100%;
  padding: 24px 0;
  background: none;
  border: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: left;
}

.accordion-header:hover {
  padding-left: 16px;
  background: rgba(163, 177, 138, 0.02);
  border-radius: 8px;
}

.accordion-title {
  font-size: 18px;
  font-family: var(--font-mono);
  font-weight: 400;
  color: var(--fg);
  transition: color 0.3s ease;
}

.accordion-header:hover .accordion-title {
  color: var(--sage);
}

.accordion-item:nth-child(2) .accordion-header:hover .accordion-title {
  color: var(--warm-clay);
}

.accordion-item:nth-child(3) .accordion-header:hover .accordion-title {
  color: var(--muted);
}

.accordion-icon {
  font-size: 20px;
  font-family: var(--font-mono);
  color: var(--muted);
  transition: all 0.3s ease;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.accordion-header:hover .accordion-icon {
  color: var(--sage);
  transform: scale(1.1);
}

.accordion-item:nth-child(2) .accordion-header:hover .accordion-icon {
  color: var(--warm-clay);
}

.accordion-item:nth-child(3) .accordion-header:hover .accordion-icon {
  color: var(--muted);
}

.accordion-item.is-open .accordion-icon {
  transform: rotate(45deg);
  color: var(--sage);
}

.accordion-item.is-open .accordion-title {
  color: var(--sage);
}

.accordion-item:nth-child(2).is-open .accordion-icon {
  color: var(--warm-clay);
}

.accordion-item:nth-child(2).is-open .accordion-title {
  color: var(--warm-clay);
}

.accordion-item:nth-child(3).is-open .accordion-icon {
  color: var(--muted);
}

.accordion-item:nth-child(3).is-open .accordion-title {
  color: var(--muted);
}

.accordion-item:nth-child(2).is-open .accordion-icon {
  color: var(--warm-clay);
}

.accordion-item:nth-child(2).is-open .accordion-title {
  color: var(--warm-clay);
}

.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease;
}

.accordion-item.is-open .accordion-content {
  max-height: 200px;
}

.accordion-body {
  padding: 16px 0 24px 0;
  border-bottom: 4px solid var(--sage);
  margin-bottom: 16px;
}

.accordion-body p {
  font-size: 16px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
}

/* Varianti colore per diversificare */
.accordion-item:nth-child(1) .accordion-body {
  border-bottom-color: var(--sage);
}

.accordion-item:nth-child(2) .accordion-body {
  border-bottom-color: var(--warm-clay);
}

.accordion-item:nth-child(3) .accordion-body {
  border-bottom-color: var(--muted);
}

.accordion-item:nth-child(4) .accordion-body {
  border-bottom-color: var(--sage);
}

/* CTA finale */
.project-cta {
  text-align: left;
  padding: 60px 0;
}

.project-cta h2 {
  font-size: 32px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
}

.project-cta p {
  font-size: 18px;
  color: var(--muted);
  margin: 0 0 32px;
  max-width: 60ch;
}

.cta-buttons {
  display: flex;
  gap: 16px;
  justify-content: flex-start;
  flex-wrap: wrap;
}

/* Responsive */
@media (max-width: 768px) {
  .project-detail-section {
    padding: 20px 0 80px;
  }

  .project-hero {
    grid-template-columns: 1fr;
    gap: 40px;
    text-align: center;
    margin-bottom: 80px;
  }

  .project-hero-image {
    order: -1;
  }

  .hero-image {
    height: 250px;
  }

  .hero-title {
    font-size: clamp(32px, 8vw, 48px);
  }

  .project-lead {
    font-size: 18px;
    max-width: 100%;
  }

  .project-details {
    padding: 40px 24px;
  }

  .project-highlights {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .project-actions,
  .cta-buttons {
    flex-direction: column;
    align-items: center;
  }

  .project-meta-header {
    justify-content: center;
  }

  .feature-with-image {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .feature-with-image.reverse {
    direction: ltr;
  }

  .feature-with-image.vertical {
    gap: 30px;
    max-width: 100%;
  }

  .feature-with-image.vertical .screenshot-container {
    max-width: 100%;
  }

  .feature-with-image.vertical .feature-content {
    padding: 24px;
  }

  .feature-content {
    padding: 24px;
    text-align: center;
  }

  .feature-content h3 {
    font-size: 24px;
  }

  .feature-content p {
    font-size: 16px;
  }



  .features-with-images {
    gap: 40px;
  }

  .project-features {
    padding: 40px 0;
    margin: 40px 0;
  }

  .project-features .container {
    padding: 40px 24px;
    border-radius: 12px;
  }

  .screenshot-container {
    padding: 16px;
  }



  .project-next-steps {
    padding: 60px 0;
    margin: 30px 0 60px;
  }

  .project-next-steps .container {
    padding: 40px 24px;
    border-radius: 12px;
  }

  /* Accordion responsive */
  .accordion-container {
    max-width: 100%;
  }

  .accordion-header {
    padding: 20px 0;
  }

  .accordion-header:hover {
    padding-left: 12px;
  }

  .accordion-title {
    font-size: 16px;
  }

  .accordion-icon {
    font-size: 18px;
    width: 18px;
    height: 18px;
  }

  .accordion-body {
    padding-left: 16px;
    margin-left: 6px;
  }

  .accordion-body p {
    font-size: 15px;
  }

  .project-next-steps h2 {
    font-size: 28px;
    gap: 8px;
    margin: 0 0 6px;
  }

  .next-steps-intro {
    margin: 0 0 24px;
    font-size: 16px;
  }

  .dot {
    width: 6px;
    height: 6px;
  }

  .animated-dots {
    gap: 4px;
  }

  .gallery-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .gallery-image img {
    height: 200px;
  }

  .lightbox-content {
    max-width: 95vw;
    max-height: 500px;
  }

  .lightbox-image {
    max-height: 300px;
  }

  .lightbox-info {
    padding: 16px;
  }

  .project-gallery {
    padding: 60px 0;
    margin: 60px 0;
  }

  /* Storia del progetto responsive */
  .project-story {
    padding: 40px 0;
    margin: 40px 0;
  }

  .story-challenge {
    margin-bottom: 24px;
  }

  .story-challenge h2 {
    font-size: 28px;
  }

  .story-challenge p {
    font-size: 18px;
  }

  .story-highlights {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .highlight-item h2 {
    font-size: 24px;
  }

  .highlight-item p {
    font-size: 18px;
  }
}
</style>
