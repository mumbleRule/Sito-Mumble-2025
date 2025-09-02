<template>
  <section class="hero">
    <div class="hero-container">
      <div class="eyebrow font-mono">Software house B2B</div>
      <h1 v-html="formatTitle(heroTitle)"></h1>
      <p class="lead">
        {{ heroSubtitle }}<br/>
        {{ heroDescription }}
      </p>
      <div class="cta">
        <router-link class="btn primary" to="/contatti">
          Parla con noi
        </router-link>
        <router-link class="btn secondary" to="/servizi">
          Scopri servizi
        </router-link>
        <router-link class="btn" to="/progetti">
          Vedi progetti
        </router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { apiService } from '../services/api.js'

const heroTitle = ref('Soluzioni software su misura.<br/>Processi automatizzati.<br/>Business accelerato.')
const heroSubtitle = ref('Sviluppiamo piattaforme web che semplificano il lavoro e fanno crescere le aziende.')
const heroDescription = ref('Dalla progettazione allo sviluppo, creiamo soluzioni digitali che trasformano le sfide quotidiane in opportunità di crescita per il tuo business.')

// Carica le impostazioni del sito
onMounted(async () => {
  try {
    const settings = await apiService.getSiteSettings()
    if (settings.hero_title) {
      heroTitle.value = settings.hero_title
    }
    if (settings.hero_subtitle) {
      heroSubtitle.value = settings.hero_subtitle
    }
    if (settings.hero_description) {
      heroDescription.value = settings.hero_description
    }
  } catch (error) {
    console.error('Error loading hero settings:', error)
  }
})

// Formatta il titolo convertendo \n in <br>
const formatTitle = (title) => {
  return title.replace(/\n/g, '<br/>')
}

// Funzione scrollToServices rimossa - ora "Scopri servizi" porta alla pagina dedicata
</script>

<style scoped>
/* Gli stili sono già definiti nel CSS globale */
</style>
