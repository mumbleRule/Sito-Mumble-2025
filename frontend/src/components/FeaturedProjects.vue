<template>
  <section id="projects" class="projects-section">
    <div class="projects-container">
      <h2>I nostri progetti</h2>
      <p class="section-subtitle">
        Scopri alcuni dei progetti che abbiamo realizzato per i nostri clienti
      </p>

    <div v-if="loading" class="loading">
      Caricamento progetti...
    </div>

    <div v-else-if="projects.length === 0" class="no-projects">
      <div class="service">
        <h3>Progetti in sviluppo</h3>
        <p>
          Stiamo lavorando su progetti innovativi che saranno presto disponibili nel nostro portfolio.
        </p>
      </div>
    </div>

    <div v-else class="featured-projects">
      <router-link
        v-for="(project, index) in projects.slice(0, 6)"
        :key="project.id"
        :to="`/progetti/${project.id}`"
        class="project-card fade-in"
        :class="getCardVariant(index)"
      >
        <div
          class="project-card-image"
          :style="getImageStyle(project.title)"
        ></div>

        <div class="project-card-content">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
        </div>

        <div class="project-card-footer">
          <div class="project-tech" v-if="project.technologies">
            {{ project.technologies }}
          </div>
        </div>
      </router-link>
    </div>

      <div class="projects-link" v-if="projects.length > 0">
        <router-link to="/progetti" class="projects-btn">
          Esplora tutti i nostri progetti →
        </router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { apiService } from '../services/api.js'

const projects = ref([])
const loading = ref(true)

// Array di varianti colore per le card
const colorVariants = ['variant-muted', 'variant-sage', 'variant-warm-clay', 'variant-accent']

// Mapping delle immagini per progetto
const projectImages = {
  'Pinbowl': '/src/assets/images/pinbowl.jpg',
  'Hotel Target': '/src/assets/images/hoteltarget_hotel_management.jpg',
  'Vinovero': '/src/assets/images/vinovero_wine_bottles.jpg',
  'IF65': '/src/assets/images/if65_project_management.jpg',
  'CreJob': '/src/assets/images/crejob-students.jpg',
  'Roda': '/src/assets/images/roda_1.png'
}

// Funzione per ottenere la variante di colore basata sull'indice
const getCardVariant = (index) => {
  return colorVariants[index % colorVariants.length]
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

// Carica i progetti in evidenza dal backend
onMounted(async () => {
  try {
    const data = await apiService.getFeaturedProjects()
    projects.value = data
  } catch (error) {
    console.error('Error loading featured projects:', error)
  } finally {
    loading.value = false
  }
})


</script>

<style scoped>
.projects-section {
  padding: 80px 0 80px;
  width: 100%;
  background: var(--chip-bg);
  position: relative;
}

.projects-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--chip-bg);
  z-index: -1;
}

.projects-section h2 {
  font-size: 32px;
  margin-bottom: 12px;
  font-weight: 500;
  font-family: var(--font-mono);
  text-align: left;
}

.section-subtitle {
  font-size: 18px;
  color: var(--muted);
  margin-bottom: 40px;
  max-width: 60ch;
  text-align: left;
}

/* Projects Link - Stile prominente */
.projects-link {
  text-align: left;
  padding: 60px 0 0;
  margin-top: 40px;
}

.projects-btn {
  display: inline-flex;
  align-items: center;
  font-size: 18px;
  font-weight: 600;
  color: #fff;
  text-decoration: none;
  padding: 18px 36px;
  border: 1px solid var(--fg);
  border-radius: 12px;
  background: var(--fg);
  transition: all 0.3s ease;
  font-family: var(--font-mono);
  letter-spacing: 0.02em;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.projects-btn:hover {
  background: #000;
  border-color: #000;
  color: #fff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
}

.loading, .no-projects {
  text-align: center;
  padding: 60px 20px;
  color: var(--muted);
}

/* Featured Projects Card Styles - Homepage */
.featured-projects .project-card {
  background: var(--bg) !important;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
  display: flex;
  flex-direction: column;
}

.featured-projects .project-card:hover {
  text-decoration: none;
  color: inherit;
}

.featured-projects .project-card:visited {
  color: inherit;
}

.featured-projects .project-card-content {
  background: var(--bg) !important;
}

/* Limitazione testo descrizione a 4 righe */
.featured-projects .project-card-content p {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.5;
  max-height: calc(1.5em * 4); /* 4 righe */
}
</style>
