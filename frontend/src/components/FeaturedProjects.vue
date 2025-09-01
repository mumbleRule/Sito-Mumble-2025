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
      <div
        v-for="(project, index) in projects.slice(0, 6)"
        :key="project.id"
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
      </div>
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

/* Projects Link - Stile intermedio */
.projects-link {
  text-align: left;
  padding: 40px 0 0;
  margin-top: 32px;
}

.projects-btn {
  display: inline-flex;
  align-items: center;
  font-size: 16px;
  font-weight: 500;
  color: var(--fg);
  text-decoration: none;
  padding: 12px 24px;
  border: 2px solid var(--line);
  border-radius: 8px;
  background: transparent;
  transition: all 0.3s ease;
}

.projects-btn:hover {
  border-color: var(--sage);
  background: var(--sage);
  color: white;
  transform: translateY(-1px);
}

.loading, .no-projects {
  text-align: center;
  padding: 60px 20px;
  color: var(--muted);
}

/* Featured Projects Card Styles - Homepage */
.featured-projects .project-card {
  background: var(--bg) !important;
}

.featured-projects .project-card-content {
  background: var(--bg) !important;
}
</style>
