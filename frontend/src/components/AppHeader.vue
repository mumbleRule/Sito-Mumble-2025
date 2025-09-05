<template>
  <header class="navbar" :class="{ 'navbar-scrolled': isScrolled }">
    <div class="navbar-container">
      <router-link class="navbar-brand" to="/">
        <img src="/Mumble_Lettering_Positivo.svg?v=2" alt="Mumble Logo" class="navbar-logo" />
      </router-link>

      <!-- Desktop Navigation -->
      <nav class="navbar-nav desktop-nav">
        <div class="nav-item" @mouseenter="showMegamenu('servizi')" @mouseleave="hideMegamenu">
          <router-link to="/servizi" class="nav-link">Servizi</router-link>
          <div class="megamenu" :class="{ 'active': activeMegamenu === 'servizi' }">
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
        </div>

        <div class="nav-item" @mouseenter="showMegamenu('progetti')" @mouseleave="hideMegamenu">
          <router-link to="/progetti" class="nav-link">Progetti</router-link>
          <div class="megamenu" :class="{ 'active': activeMegamenu === 'progetti' }">
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
        </div>

        <div class="nav-item" @mouseenter="showMegamenu('contatti')" @mouseleave="hideMegamenu">
          <router-link to="/contatti" class="nav-link">Contattaci</router-link>
          <div class="megamenu" :class="{ 'active': activeMegamenu === 'contatti' }">
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

// Megamenu functions
const showMegamenu = (menu) => {
  activeMegamenu.value = menu
}

const hideMegamenu = () => {
  activeMegamenu.value = null
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

/* Megamenu Styles */
.megamenu {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  opacity: 0;
  visibility: hidden;
  transform: translateX(-50%) translateY(-10px);
  transition: all 0.3s ease;
  z-index: 1000;
  width: clamp(400px, 50vw, 600px);
  max-width: calc(100vw - 40px);
  margin-top: 8px;
}

.megamenu.active {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}

/* Controllo per evitare che esca dai bordi */
.nav-item:last-child .megamenu {
  left: auto;
  right: 0;
  transform: translateX(0) translateY(-10px);
}

.nav-item:last-child .megamenu.active {
  transform: translateX(0) translateY(0);
}

.megamenu-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: clamp(16px, 3vw, 32px);
  padding: clamp(20px, 4vw, 32px);
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
  padding: 7px 12px !important;
  background: var(--chip-bg) !important;
  border-radius: 5px !important;
  transition: all 0.3s ease !important;
  white-space: nowrap !important;
  text-align: center !important;
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

  .megamenu {
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
