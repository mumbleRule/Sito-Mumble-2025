<template>
  <footer class="app-footer">
    <div class="footer-content">
      <div class="footer-brand">
        <img src="/Mumble_Lettering_Negativo.svg" alt="Mumble Logo" class="footer-logo" />
      </div>

      <div class="footer-info">
        <p class="footer-description">
          Software house B2B specializzata in gestionali su misura e automazione dei processi aziendali.
        </p>

        <div class="footer-contact">
          <a href="mailto:info@mumble.group" class="footer-email font-mono">
            info@mumble.group
          </a>
        </div>
      </div>

      <div class="footer-links">
        <nav class="footer-nav">
          <router-link to="/">Home</router-link>
          <router-link to="/progetti">Progetti</router-link>
          <router-link to="/contatti">Contatti</router-link>
        </nav>
      </div>
    </div>

    <div class="footer-bottom">
      <p class="footer-copyright">
        © {{ currentYear }} {{ siteTitle }}. Tutti i diritti riservati.
      </p>
    </div>
  </footer>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { apiService } from '../services/api.js'

const siteTitle = ref('Mumble')
const currentYear = computed(() => new Date().getFullYear())

// Carica le impostazioni del sito
onMounted(async () => {
  try {
    const settings = await apiService.getSiteSettings()
    siteTitle.value = settings.site_title || 'Mumble'
  } catch (error) {
    console.error('Error loading site settings:', error)
  }
})
</script>

<style scoped>
.app-footer {
  background: #000;
  color: #fff;
  margin-top: 0;
  padding: 60px 0 32px;
}

.footer-content {
  max-width: 1080px;
  margin: 0 auto;
  padding: 0 24px;
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 48px;
  align-items: start;
}

.footer-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.footer-logo {
  height: 32px;
  width: auto;
}

.footer-title {
  font-size: 18px;
  font-weight: 400;
  color: #fff;
}

.footer-info {
  max-width: 400px;
}

.footer-description {
  font-size: 15px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
  margin: 0 0 24px 0;
}

.footer-contact {
  margin-top: 16px;
}

.footer-email {
  color: #fff;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.2s ease;
}

.footer-email:hover {
  color: var(--accent);
}

.footer-links {
  display: flex;
  justify-content: flex-end;
}

.footer-nav {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-nav a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  font-size: 14px;
  font-family: var(--font-mono);
  transition: color 0.2s ease;
}

.footer-nav a:hover,
.footer-nav a.router-link-active {
  color: #fff;
}

.footer-bottom {
  max-width: 1080px;
  margin: 48px auto 0;
  padding: 24px 24px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.footer-copyright {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
  text-align: center;
  margin: 0;
}

/* Responsive */
@media (max-width: 768px) {
  .app-footer {
    margin-top: 0;
    padding: 40px 0 24px;
  }

  .footer-content {
    grid-template-columns: 1fr;
    gap: 32px;
    text-align: center;
  }

  .footer-brand {
    justify-content: center;
  }

  .footer-links {
    justify-content: center;
  }

  .footer-nav {
    flex-direction: row;
    justify-content: center;
    gap: 24px;
  }

  .footer-bottom {
    margin-top: 32px;
  }
}
</style>
