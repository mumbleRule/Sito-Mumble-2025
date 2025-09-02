<template>
  <div class="projects-page">
    <section class="projects-section">
      <div class="container">
        <div class="projects-hero">
          <div class="eyebrow font-mono">Portfolio</div>
          <h1>I nostri progetti</h1>
          <p class="lead">
            Scopri alcuni dei progetti che abbiamo realizzato per i nostri clienti.
            Ogni soluzione è stata progettata su misura per rispondere a esigenze specifiche.
          </p>
        </div>

        <div class="projects-content">
          <div v-if="loading" class="loading">
            Caricamento progetti...
          </div>

          <div v-else-if="projects.length === 0" class="no-projects">
            <div class="empty-state">
              <h3>Progetti in arrivo</h3>
              <p>
                Stiamo aggiornando il nostro portfolio con i progetti più recenti.
                Nel frattempo, <router-link to="/contatti">contattaci</router-link>
                per saperne di più sui nostri lavori.
              </p>
            </div>
          </div>

          <div v-else class="projects-by-category">
            <!-- Business Management -->
            <div id="business-management" class="category-section">
              <div class="category-header">
                <div class="category-tag sage">Business Management</div>
                <h2>Gestione aziendale e processi</h2>
                <p>Soluzioni per ottimizzare operazioni, gestire risorse e automatizzare processi aziendali complessi.</p>
              </div>
              <div class="projects-grid">
                <router-link
                  v-for="(project, index) in businessManagementProjects"
                  :key="project.id"
                  :to="`/progetti/${project.id}`"
                  class="project-card fade-in"
                  :style="{ animationDelay: `${index * 0.1}s` }"
                >
                  <div class="project-card-image" :style="getImageStyle(project.title)">
                    <div class="project-card-overlay">
                      <h3>{{ project.title }}</h3>
                      <p class="project-category" v-if="project.category">{{ project.category }}</p>
                    </div>
                  </div>
                  <div class="project-card-content">
                    <p class="project-description">{{ getShortDescription(project.description) }}</p>
                    <div class="project-tech" v-if="project.technologies">
                      <span v-for="tech in getTechnologies(project.technologies)" :key="tech" class="tech-tag">
                        {{ tech }}
                      </span>
                    </div>
                  </div>
                </router-link>
              </div>
            </div>

            <!-- E-commerce & Marketplace -->
            <div id="ecommerce-marketplace" class="category-section">
              <div class="category-header">
                <div class="category-tag warm-clay">E-commerce & Marketplace</div>
                <h2>Piattaforme di vendita e marketplace</h2>
                <p>Ecosistemi digitali per vendita online, marketplace e piattaforme che connettono domanda e offerta.</p>
              </div>
              <div class="projects-grid">
                <router-link
                  v-for="(project, index) in ecommerceProjects"
                  :key="project.id"
                  :to="`/progetti/${project.id}`"
                  class="project-card fade-in"
                  :style="{ animationDelay: `${index * 0.1}s` }"
                >
                  <div class="project-card-image" :style="getImageStyle(project.title)">
                    <div class="project-card-overlay">
                      <h3>{{ project.title }}</h3>
                      <p class="project-category" v-if="project.category">{{ project.category }}</p>
                    </div>
                  </div>
                  <div class="project-card-content">
                    <p class="project-description">{{ getShortDescription(project.description) }}</p>
                    <div class="project-tech" v-if="project.technologies">
                      <span v-for="tech in getTechnologies(project.technologies)" :key="tech" class="tech-tag">
                        {{ tech }}
                      </span>
                    </div>
                  </div>
                </router-link>
              </div>
            </div>

            <!-- Entertainment & Leisure -->
            <div id="entertainment-leisure" class="category-section">
              <div class="category-header">
                <div class="category-tag muted">Entertainment & Leisure</div>
                <h2>Intrattenimento e tempo libero</h2>
                <p>Applicazioni per il divertimento, gestione eventi e esperienze coinvolgenti per gli utenti.</p>
              </div>
              <div class="projects-grid">
                <router-link
                  v-for="(project, index) in entertainmentProjects"
                  :key="project.id"
                  :to="`/progetti/${project.id}`"
                  class="project-card fade-in"
                  :style="{ animationDelay: `${index * 0.1}s` }"
                >
                  <div class="project-card-image" :style="getImageStyle(project.title)">
                    <div class="project-card-overlay">
                      <h3>{{ project.title }}</h3>
                      <p class="project-category" v-if="project.category">{{ project.category }}</p>
                    </div>
                  </div>
                  <div class="project-card-content">
                    <p class="project-description">{{ getShortDescription(project.description) }}</p>
                    <div class="project-tech" v-if="project.technologies">
                      <span v-for="tech in getTechnologies(project.technologies)" :key="tech" class="tech-tag">
                        {{ tech }}
                      </span>
                    </div>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sezione Il nostro approccio -->
    <section id="metodologia" class="approach-section">
      <div class="container">
        <div class="approach-content">
          <div class="approach-header">
            <div class="eyebrow font-mono">Metodologia</div>
            <h2>Il nostro approccio</h2>
            <p class="approach-lead">
              Ogni progetto è unico, ma il nostro metodo di lavoro è sempre lo stesso:
              <strong>ascolto</strong>, <strong>progettazione</strong>, <strong>sviluppo</strong> e <strong>supporto continuo</strong>.
            </p>
          </div>

          <div class="approach-steps">
            <div class="step-item">
              <div class="step-number">01</div>
              <div class="step-content">
                <h3>Analisi e Discovery</h3>
                <p>Comprendiamo a fondo le tue esigenze, i processi aziendali e gli obiettivi da raggiungere.</p>
              </div>
            </div>

            <div class="step-item">
              <div class="step-number">02</div>
              <div class="step-content">
                <h3>Progettazione UX/UI</h3>
                <p>Creiamo wireframe e prototipi per definire l'esperienza utente e l'interfaccia ottimale.</p>
              </div>
            </div>

            <div class="step-item">
              <div class="step-number">03</div>
              <div class="step-content">
                <h3>Sviluppo Agile</h3>
                <p>Sviluppiamo con metodologie agili, mantenendo comunicazione costante e rilasci incrementali.</p>
              </div>
            </div>

            <div class="step-item">
              <div class="step-number">04</div>
              <div class="step-content">
                <h3>Test e Deploy</h3>
                <p>Testiamo accuratamente ogni funzionalità e gestiamo il deployment in produzione.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sezione Tecnologie -->
    <section id="tecnologie" class="tech-section">
      <div class="container">
        <div class="tech-content">
          <div class="tech-header">
            <div class="eyebrow font-mono">Tecnologie</div>
            <h2>Il nostro stack</h2>
            <p class="tech-lead">
              Utilizziamo tecnologie moderne e affidabili per creare soluzioni <strong>scalabili</strong>, <strong>performanti</strong> e <strong>sicure</strong>.
            </p>
          </div>

          <div class="tech-grid">
                <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="Django" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg" alt="Vue.js" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nuxtjs/nuxtjs-original.svg" alt="Nuxt.js" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" alt="Node.js" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/npm/npm-original-wordmark.svg" alt="npm" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" alt="TypeScript" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" alt="PostgreSQL" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" alt="Redis" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="Docker" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="Git" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" alt="Linux" class="tech-logo">
            </div>

            <div class="tech-logo-item">
              <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" alt="Nginx" class="tech-logo">
            </div>


          </div>
        </div>
      </div>
    </section>

    <!-- Sezione CTA finale -->
    <section class="projects-cta-section">
      <div class="container">
        <div class="projects-cta">
          <h2>Hai un progetto in mente?</h2>
          <p>
            Raccontaci la tua idea e scopriamo insieme come trasformarla in realtà.
            Ogni grande progetto inizia con una conversazione.
          </p>
          <div class="cta-buttons">
            <router-link to="/contatti" class="btn primary">
              Parliamo del tuo progetto
            </router-link>
            <router-link to="/" class="btn secondary">
              Scopri i nostri servizi
            </router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { apiService } from '../services/api.js'

const projects = ref([])
const loading = ref(true)

// Progetti categorizzati
const businessManagementProjects = ref([])
const ecommerceProjects = ref([])
const entertainmentProjects = ref([])

// Mapping dei progetti per categoria
const projectCategories = {
  'Hotel Target': 'business',
  'IF65': 'business',
  'Roda': 'business',
  'Vinovero': 'ecommerce',
  'CreJob': 'ecommerce',
  'Pinbowl': 'entertainment'
}

// Mapping delle immagini per progetto
const projectImages = {
  'Pinbowl': '/src/assets/images/pinbowl.jpg',
  'Hotel Target': '/src/assets/images/hoteltarget_hotel_management.jpg',
  'Vinovero': '/src/assets/images/vinovero_wine_bottles.jpg',
  'IF65': '/src/assets/images/if65_project_management.jpg',
  'CreJob': '/src/assets/images/crejob-students.jpg',
  'Roda': '/src/assets/images/roda_1.png'
}

// Funzione per categorizzare i progetti
const categorizeProjects = (projectsList) => {
  businessManagementProjects.value = projectsList.filter(p => projectCategories[p.title] === 'business')
  ecommerceProjects.value = projectsList.filter(p => projectCategories[p.title] === 'ecommerce')
  entertainmentProjects.value = projectsList.filter(p => projectCategories[p.title] === 'entertainment')
}

// Funzione per ottenere lo stile dell'immagine
const getImageStyle = (projectTitle) => {
  const imagePath = projectImages[projectTitle]
  if (imagePath) {
    return {
      backgroundImage: `url(${imagePath})`
    }
  }
  return {}
}

// Funzione per accorciare la descrizione
const getShortDescription = (description) => {
  if (description.length > 120) {
    return description.substring(0, 120) + '...'
  }
  return description
}

// Funzione per dividere le tecnologie in array
const getTechnologies = (techString) => {
  if (!techString) return []
  return techString.split(',').map(tech => tech.trim())
}

// Carica i progetti dal backend
onMounted(async () => {
  try {
    const data = await apiService.getProjects()
    projects.value = data
    categorizeProjects(data)
  } catch (error) {
    console.error('Error loading projects:', error)
    businessManagementProjects.value = []
    ecommerceProjects.value = []
    entertainmentProjects.value = []
  } finally {
    loading.value = false
  }
})
</script>

<style scoped>
/* Scroll offset per navbar fissa */
#business-management,
#ecommerce-marketplace,
#entertainment-leisure,
#metodologia,
#tecnologie {
  scroll-margin-top: 100px;
}

.projects-page {
  min-height: 100vh;
}

.projects-section {
  background-color: var(--bg);
  padding: 80px 0 120px;
  width: 100%;
}

.projects-hero {
  text-align: left;
  margin-bottom: 80px;
  max-width: 800px;
}

.projects-hero .eyebrow {
  color: var(--muted);
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.projects-hero h1 {
  font-size: clamp(40px, 5vw, 56px);
  margin: 0 0 24px;
  font-weight: 400;
  line-height: 1.1;
  color: var(--fg);
}

.projects-hero .lead {
  font-size: 20px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
}

.projects-content {
  margin-top: 60px;
}

.loading, .no-projects {
  text-align: center;
  padding: 80px 20px;
  color: var(--muted);
}

.empty-state h3 {
  font-size: 24px;
  margin-bottom: 16px;
  color: var(--fg);
}

/* Projects by Category */
.projects-by-category {
  display: flex;
  flex-direction: column;
  gap: 80px;
  padding-bottom: 80px;
}

.category-section {
  display: flex;
  flex-direction: column;
  gap: 40px;
}

.category-header {
  text-align: left;
  max-width: 800px;
}

.category-tag {
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 600;
  padding: 6px 12px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 16px;
  display: inline-block;
  color: white;
}

.category-tag.sage {
  background: var(--sage);
}

.category-tag.warm-clay {
  background: var(--warm-clay);
}

.category-tag.muted {
  background: var(--muted);
}

.category-header h2 {
  font-size: clamp(28px, 4vw, 36px);
  margin: 0 0 16px;
  font-weight: 400;
  color: var(--fg);
}

.category-header p {
  font-size: 18px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 32px;
  margin-top: 40px;
}

.projects-page .projects-grid .project-card {
  background: var(--chip-bg) !important;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  transition: all 0.3s ease;
  opacity: 0;
  transform: translateX(-20px);
  animation: slideInLeft 0.6s ease forwards;
  height: auto;
  text-decoration: none;
  color: inherit;
  display: block;
  cursor: pointer;
}



.projects-page .projects-grid .project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.project-card-image {
  height: 200px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
  display: flex;
  align-items: flex-end;
  padding: 24px;
}

.project-card-overlay {
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 24px;
}

.project-card-overlay h3 {
  color: white;
  font-size: 24px;
  font-weight: 500;
  margin: 0 0 8px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.project-category {
  color: rgba(255, 255, 255, 0.9);
  font-size: 14px;
  font-weight: 500;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.projects-page .projects-grid .project-card-content {
  padding: 24px;
  background: var(--chip-bg) !important;
}

.projects-page .projects-grid .project-description {
  font-size: 16px;
  line-height: 1.5;
  color: var(--muted);
  margin: 0 0 20px;
}



.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 20px;
}

.tech-tag {
  background: var(--line);
  color: var(--muted);
  padding: 4px 12px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 500;
  font-family: var(--font-mono);
}

.project-link {
  margin-top: auto;
}

/* Varianti colore per le card */
.variant-muted .project-card-image {
  background-color: var(--line);
}

.variant-sage .project-card-image {
  background-color: var(--sage);
}

.variant-warm-clay .project-card-image {
  background-color: var(--warm-clay);
}

.variant-accent .project-card-image {
  background-color: var(--muted);
}

/* Animazioni */
@keyframes slideInLeft {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Sezione Il nostro approccio */
.approach-section {
  background: var(--chip-bg);
  padding: 40px 0 80px;
}

.approach-content {
  /* Rimosso max-width per allineare con la CTA finale */
}

.approach-header {
  text-align: left;
  margin-bottom: 60px;
  max-width: 600px;
}

.approach-header .eyebrow {
  color: var(--muted);
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.approach-header h2 {
  font-size: 32px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
}

.approach-lead {
  font-size: 18px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
}

.approach-lead strong {
  color: var(--warm-clay);
  font-weight: 600;
}

.approach-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
}

.step-item {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}

.step-number {
  flex-shrink: 0;
  width: 48px;
  height: 48px;
  background: var(--warm-clay);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-weight: 600;
  font-size: 16px;
}

.step-content h3 {
  font-size: 18px;
  margin: 0 0 12px;
  color: var(--fg);
  font-family: var(--font-mono);
  font-weight: 500;
}

.step-content p {
  font-size: 16px;
  line-height: 1.5;
  color: var(--muted);
  margin: 0;
}

/* Sezione Tecnologie */
.tech-section {
  background: var(--bg);
  padding: 80px 0;
}

.tech-content {
  max-width: 1200px;
  margin: 0 auto;
}

.tech-header {
  text-align: left;
  margin-bottom: 60px;
  max-width: 600px;
}

.tech-header .eyebrow {
  color: var(--muted);
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.tech-header h2 {
  font-size: 32px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
}

.tech-lead {
  font-size: 18px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
}

.tech-lead strong {
  color: var(--fg);
  font-weight: 700;
}

.tech-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 16px;
  max-width: 900px;
}

.tech-logo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.tech-logo-item:hover {
  transform: scale(1.1);
}

.tech-logo {
  width: 56px;
  height: 56px;
  transition: all 0.3s ease;
  filter: grayscale(0.3);
}

.tech-logo-item:hover .tech-logo {
  filter: grayscale(0);
}

/* Tech name rimosso - solo loghi */

/* Griglia tecnologie - nessuna animazione */

/* Sezione CTA finale */
.projects-cta-section {
  background: var(--bg);
  padding: 80px 0;
}

.projects-cta {
  text-align: left;
  max-width: 600px;
}

.projects-cta h2 {
  font-size: 32px;
  margin: 0 0 16px;
  color: var(--fg);
  font-family: var(--font-mono);
}

.projects-cta p {
  font-size: 18px;
  color: var(--muted);
  margin: 0 0 32px;
  line-height: 1.6;
}

.cta-buttons {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

/* Responsive */
@media (max-width: 768px) {
  .projects-section {
    padding: 60px 0 80px;
  }

  .projects-hero {
    margin-bottom: 60px;
  }

  .projects-hero h1 {
    font-size: clamp(32px, 8vw, 40px);
  }

  .projects-hero .lead {
    font-size: 18px;
  }

  .projects-by-category {
    gap: 60px;
    padding-bottom: 60px;
  }

  .category-section {
    gap: 32px;
  }

  .category-header h2 {
    font-size: 28px;
  }

  .category-header p {
    font-size: 16px;
  }

  .projects-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .project-card-image {
    height: 160px;
    padding: 20px;
  }

  .project-card-overlay {
    padding: 20px;
  }

  .project-card-overlay h3 {
    font-size: 20px;
  }

  .project-card-content {
    padding: 20px;
  }

  /* Sezioni aggiuntive responsive */
  .approach-section {
    padding: 30px 0 60px;
  }

  .tech-section,
  .projects-cta-section {
    padding: 60px 0;
  }

  .approach-header {
    margin-bottom: 40px;
  }

  .approach-steps {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .step-item {
    gap: 16px;
  }

  .step-number {
    width: 40px;
    height: 40px;
    font-size: 14px;
  }

  .step-content h3 {
    font-size: 16px;
  }

  .step-content p {
    font-size: 15px;
  }

  .cta-buttons {
    flex-direction: column;
    align-items: flex-start;
  }

  /* Tech section responsive */
  .tech-header {
    margin-bottom: 40px;
  }

  .tech-grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
  }

  .tech-logo-item {
    padding: 8px;
  }

  .tech-logo {
    width: 48px;
    height: 48px;
  }
}

@media (max-width: 480px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }

  .project-card {
    margin: 0 -20px;
    border-radius: 0;
  }
}
</style>
