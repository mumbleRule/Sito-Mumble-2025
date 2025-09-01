<template>
  <header>
    <div class="header-container">
      <router-link class="brand" to="/">
        <img src="/Mumble_Lettering_Positivo.svg?v=2" alt="Mumble Logo" class="logo" />
      </router-link>
      <nav>
        <router-link to="/" @click="scrollToServices">Servizi</router-link>
        <router-link to="/progetti">Progetti</router-link>
        <router-link to="/contatti">Contattaci</router-link>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { apiService } from '../services/api.js'

const router = useRouter()
const siteTitle = ref('Mumble')

// Carica le impostazioni del sito
onMounted(async () => {
  try {
    const settings = await apiService.getSiteSettings()
    siteTitle.value = settings.site_title || 'Mumble'
  } catch (error) {
    console.error('Error loading site settings:', error)
  }
})

// Funzione per andare alla homepage e scrollare ai servizi
const scrollToServices = () => {
  if (router.currentRoute.value.path === '/') {
    // Se siamo già nella homepage, scrolla ai servizi
    setTimeout(() => {
      const element = document.getElementById('services')
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
      }
    }, 100)
  }
  // Se non siamo nella homepage, il router-link ci porterà lì
}
</script>

<style scoped>
/* Gli stili sono già definiti nel CSS globale */
</style>
