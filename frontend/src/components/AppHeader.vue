<template>
  <header class="navbar" :class="{ 'navbar-scrolled': isScrolled }">
    <div class="navbar-container">
      <router-link class="navbar-brand" to="/">
        <img src="/Mumble_Lettering_Positivo.svg?v=2" alt="Mumble Logo" class="navbar-logo" />
      </router-link>

      <!-- Desktop Navigation -->
      <nav class="navbar-nav desktop-nav" @mouseleave="scheduleMegamenuClose">
        <div class="nav-item" @mouseenter="showMegamenu('servizi')">
          <router-link to="/servizi" class="nav-link">Servizi</router-link>
        </div>

        <div class="nav-item" @mouseenter="showMegamenu('progetti')">
          <router-link to="/progetti" class="nav-link">Progetti</router-link>
        </div>

        <div class="nav-item" @mouseenter="showMegamenu('contatti')">
          <router-link to="/contatti" class="nav-link">Contattaci</router-link>
        </div>

        <!-- Megamenu Container Unico -->
        <div class="megamenu-container"
             :class="{ 'active': !!activeMegamenu }"
             @mouseenter="cancelMegamenuClose"
             @mouseleave="scheduleMegamenuClose">

          <!-- Megamenu Servizi -->
          <div v-show="activeMegamenu === 'servizi'" class="megamenu servizi-megamenu">
            <div class="megamenu-content">
              <div class="megamenu-section">
                <div class="section-tag sage">Sviluppo</div>
                <ul>
                  <li><a href="/servizi#sviluppo" @click="hideMegamenu">Development</a></li>
                  <li><a href="/servizi#sviluppo" @click="hideMegamenu">Web App & UX/UI</a></li>
                </ul>
              </div>
              <div class="megamenu-section">
                <div class="section-tag warm-clay">Integrazione</div>
                <ul>
                  <li><a href="/servizi#integrazione" @click="hideMegamenu">Integrazioni API</a></li>
                  <li><a href="/servizi#integrazione" @click="hideMegamenu">Portali & Piattaforme</a></li>
                </ul>
              </div>
              <div class="megamenu-section">
                <div class="section-tag muted">Gestione</div>
                <ul>
                  <li><a href="/servizi#gestione" @click="hideMegamenu">CRM e ERP</a></li>
                  <li><a href="/servizi#gestione" @click="hideMegamenu">Business Intelligence</a></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Megamenu Progetti -->
          <div v-show="activeMegamenu === 'progetti'" class="megamenu progetti-megamenu">
            <div class="megamenu-content">
              <div class="megamenu-section">
                <div class="section-tag sage">Progetti</div>
                <ul>
                  <li><a href="/progetti#business-management" @click="hideMegamenu">Business Management</a></li>
                  <li><a href="/progetti#ecommerce-marketplace" @click="hideMegamenu">E-commerce & Marketplace</a></li>
                  <li><a href="/progetti#entertainment-leisure" @click="hideMegamenu">Entertainment & Leisure</a></li>
                </ul>
              </div>
              <div class="megamenu-section">
                <div class="section-tag warm-clay">Metodologia</div>
                <ul>
                  <li><a href="/progetti#metodologia" @click="hideMegamenu">Il nostro processo</a></li>
                </ul>
              </div>
              <div class="megamenu-section">
                <div class="section-tag muted">Tecnologie</div>
                <ul>
                  <li><a href="/progetti#tecnologie" @click="hideMegamenu">Stack tecnologico</a></li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Megamenu Contatti -->
          <div v-show="activeMegamenu === 'contatti'" class="megamenu contatti-megamenu">
            <div class="megamenu-content">
              <div class="megamenu-section">
                <div class="section-tag sage">Parliamo del tuo progetto</div>
                <p>Raccontaci la tua idea e troviamo insieme la soluzione migliore.</p>
                <a href="/contatti" class="megamenu-cta" @click="hideMegamenu">Inizia ora →</a>
              </div>
              <div class="megamenu-section">
                <div class="section-tag warm-clay">Contatti Diretti</div>
                <ul>
                  <li><a href="mailto:info@mumble.group" class="email-link" @click="hideMegamenu">info@mumble.group</a></li>
                </ul>
                <div class="section-tag muted" style="margin-top: 24px;">Seguici</div>
                <ul>
                  <li><a href="#" target="_blank" @click="hideMegamenu">LinkedIn</a></li>
                  <li><a href="#" target="_blank" @click="hideMegamenu">GitHub</a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </nav>

      <!-- Mobile Menu Button -->
      <button
        class="mobile-menu-btn"
        @click="toggleMobileMenu"
        :class="{ 'active': isMobileMenuOpen }"
        aria-label="Toggle menu"
      >
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
        <span class="hamburger-line"></span>
      </button>
    </div>

    <!-- Mobile Navigation -->
    <nav class="mobile-nav" :class="{ 'active': isMobileMenuOpen }">
      <router-link to="/servizi" class="mobile-nav-link" @click="closeMobileMenu">Servizi</router-link>
      <router-link to="/progetti" class="mobile-nav-link" @click="closeMobileMenu">Progetti</router-link>
      <router-link to="/contatti" class="mobile-nav-link" @click="closeMobileMenu">Contattaci</router-link>
    </nav>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { apiService } from '../services/api.js'

const router = useRouter()
const siteTitle = ref('Mumble')

// Navbar state
const isScrolled = ref(false)
const isMobileMenuOpen = ref(false)
const activeMegamenu = ref(null)

// Scroll detection for sticky navbar
const handleScroll = () => {
  isScrolled.value = window.scrollY > 20
}

// Mobile menu functions
const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
}

// Megamenu functions with timers to prevent flickering
let openTimer = null
let closeTimer = null

const showMegamenu = (menu) => {
  // Cancella qualsiasi timer di chiusura in corso
  if (closeTimer) {
    clearTimeout(closeTimer)
    closeTimer = null
  }

  // Cancella qualsiasi timer di apertura precedente
  if (openTimer) {
    clearTimeout(openTimer)
    openTimer = null
  }

  // Apri con un piccolo delay per evitare aperture accidentali
  openTimer = setTimeout(() => {
    activeMegamenu.value = menu
    openTimer = null
  }, 100)
}

const hideMegamenu = () => {
  // Cancella qualsiasi timer in corso
  if (openTimer) {
    clearTimeout(openTimer)
    openTimer = null
  }
  if (closeTimer) {
    clearTimeout(closeTimer)
    closeTimer = null
  }

  activeMegamenu.value = null
}

const scheduleMegamenuClose = () => {
  // Cancella qualsiasi timer di apertura in corso
  if (openTimer) {
    clearTimeout(openTimer)
    openTimer = null
  }

  // Programma la chiusura con delay per permettere il movimento del mouse
  closeTimer = setTimeout(() => {
    activeMegamenu.value = null
    closeTimer = null
  }, 250)
}

const cancelMegamenuClose = () => {
  // Cancella il timer di chiusura se il mouse rientra nell'area
  if (closeTimer) {
    clearTimeout(closeTimer)
    closeTimer = null
  }
}

// Carica le impostazioni del sito
onMounted(async () => {
  try {
    const settings = await apiService.getSiteSettings()
    siteTitle.value = settings.site_title || 'Mumble'
  } catch (error) {
    console.error('Error loading site settings:', error)
  }

  // Add scroll listener
  window.addEventListener('scroll', handleScroll)
  handleScroll() // Check initial scroll position
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* Modern Sticky Navbar */
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(235, 235, 225, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid transparent;
  transition: all 0.3s ease;
}

.navbar-scrolled {
  background: rgba(235, 235, 225, 0.98);
  border-bottom-color: rgba(0, 0, 0, 0.05);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 80px;
}

/* Brand/Logo */
.navbar-brand {
  display: flex;
  align-items: center;
  text-decoration: none;
  transition: transform 0.3s ease;
}

.navbar-brand:hover {
  transform: scale(1.05);
}

.navbar-logo {
  height: 32px;
  width: auto;
}

/* Desktop Navigation */
.desktop-nav {
  display: flex;
  align-items: center;
  gap: 40px;
}

.nav-item {
  position: relative;
}



.nav-link {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 500;
  color: var(--fg);
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  position: relative;
  padding: 8px 0;
  transition: all 0.3s ease;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--muted);
  transition: width 0.3s ease;
}

.nav-link:hover::after,
.nav-link.router-link-active::after {
  width: 100%;
}

.nav-link:hover {
  color: var(--muted);
}

.nav-link.router-link-active {
  color: var(--muted);
}

/* Megamenu Container Unico */
.megamenu-container {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: all 0.3s ease;
  z-index: 1000;
  margin-top: 8px;
  pointer-events: none;
}

/* Hover bridge per evitare gap tra nav e megamenu */
.megamenu-container::before {
  content: '';
  position: absolute;
  top: -12px;
  left: 0;
  right: 0;
  height: 12px;
  background: transparent;
}

.megamenu-container.active {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
  pointer-events: auto;
}

/* Megamenu Styles */
.megamenu {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  width: 450px;
  max-width: calc(100vw - 40px);
  margin: 0 auto;
}

/* Megamenu per schermi grandi */
@media (min-width: 1400px) {
  .megamenu {
    width: 480px;
  }

  .megamenu-content {
    gap: clamp(18px, 3vw, 24px);
    padding: clamp(20px, 4vw, 28px);
  }

  .megamenu-section a {
    font-size: 15px;
  }
}

/* Layout specifico per megamenu Contattaci */
.contatti-megamenu .megamenu-content {
  grid-template-columns: 1fr 1fr !important;
  gap: 24px !important;
  min-height: 140px;
}

/* Prima sezione del megamenu contattaci - più spazio */
.contatti-megamenu .megamenu-section:first-child {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding-right: 8px;
}

.contatti-megamenu .megamenu-section:first-child p {
  margin: 6px 0 14px !important;
  line-height: 1.4 !important;
  font-size: 13px !important;
}

/* Seconda sezione del megamenu contattaci - allineamento */
.contatti-megamenu .megamenu-section:last-child {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding-left: 8px;
}

/* Spacing uniforme per le liste nel megamenu contattaci */
.contatti-megamenu .megamenu-section ul {
  margin-bottom: 16px;
}

.contatti-megamenu .megamenu-section li {
  margin-bottom: 10px;
}



.megamenu-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: clamp(12px, 2vw, 20px);
  padding: clamp(16px, 3vw, 24px);
}



/* Section Tags */
.section-tag {
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

.section-tag.sage {
  background: var(--sage);
}

.section-tag.warm-clay {
  background: var(--warm-clay);
}

.section-tag.muted {
  background: var(--muted);
}

.megamenu-section ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.megamenu-section li {
  margin-bottom: 8px;
}

.megamenu-section a {
  color: var(--muted);
  text-decoration: none;
  font-size: 14px;
  line-height: 1.5;
  transition: color 0.3s ease;
  display: block;
  padding: 4px 0;
}

.megamenu-section a:hover {
  color: var(--fg);
}

/* Email link specifico con hover warm clay */
.megamenu-section .email-link {
  color: var(--fg);
  font-weight: 600;
}

.megamenu-section .email-link:hover {
  color: var(--warm-clay);
}

.megamenu-section p {
  color: var(--muted);
  font-size: 14px;
  line-height: 1.5;
  margin: 0 0 16px;
}



.megamenu-cta {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 5px !important;
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  color: var(--fg) !important;
  text-decoration: none !important;
  text-transform: uppercase !important;
  letter-spacing: 0.3px !important;
  padding: 8px 14px !important;
  background: var(--chip-bg) !important;
  border-radius: 6px !important;
  transition: all 0.3s ease !important;
  white-space: nowrap !important;
  text-align: center !important;
  margin-top: 4px !important;
  width: fit-content !important;
}

.megamenu-cta:hover {
  background: var(--muted);
  color: white;
  transform: translateX(4px);
}

/* Mobile Menu Button */
.mobile-menu-btn {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  z-index: 1001;
}

.hamburger-line {
  width: 24px;
  height: 2px;
  background: var(--fg);
  margin: 3px 0;
  transition: all 0.3s ease;
  transform-origin: center;
}

.mobile-menu-btn.active .hamburger-line:nth-child(1) {
  transform: rotate(45deg) translate(6px, 6px);
}

.mobile-menu-btn.active .hamburger-line:nth-child(2) {
  opacity: 0;
}

.mobile-menu-btn.active .hamburger-line:nth-child(3) {
  transform: rotate(-45deg) translate(6px, -6px);
}

/* Mobile Navigation */
.mobile-nav {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: var(--bg);
  border-bottom: 1px solid var(--line);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  transform: translateY(-100%);
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
}

.mobile-nav.active {
  transform: translateY(0);
  opacity: 1;
  visibility: visible;
}

.mobile-nav-link {
  display: block;
  font-family: var(--font-mono);
  font-size: 16px;
  font-weight: 500;
  color: var(--fg);
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 20px 24px;
  border-bottom: 1px solid var(--line);
  transition: all 0.3s ease;
}

.mobile-nav-link:hover,
.mobile-nav-link.router-link-active {
  background: var(--chip-bg);
  color: var(--muted);
}

.mobile-nav-link:last-child {
  border-bottom: none;
}



/* Media query per tablet - megamenu responsive */
@media (max-width: 1024px) and (min-width: 769px) {
  .megamenu {
    width: clamp(350px, 45vw, 450px);
  }

  .megamenu-content {
    gap: clamp(10px, 2vw, 18px);
    padding: clamp(14px, 3vw, 20px);
  }

  .megamenu-section a {
    font-size: 13px;
  }

  /* Megamenu contattaci responsive tablet */
  .contatti-megamenu .megamenu-content {
    min-height: 120px;
  }

  .contatti-megamenu .megamenu-section:first-child p {
    font-size: 12px !important;
    margin: 4px 0 12px !important;
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar-container {
    padding: 0 20px;
    height: 70px;
  }

  .navbar-logo {
    height: 28px;
  }

  .desktop-nav {
    display: none;
  }

  .mobile-menu-btn {
    display: flex;
  }

  .mobile-nav {
    display: block;
  }

  .megamenu-container {
    display: none;
  }
}

@media (max-width: 480px) {
  .navbar-container {
    padding: 0 16px;
    height: 65px;
  }

  .navbar-logo {
    height: 24px;
  }
}
</style>
