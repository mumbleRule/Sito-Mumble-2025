<template>
  <footer class="mega-footer">
    <!-- Main Footer Content -->
    <div class="footer-main">
      <div class="footer-container">
        <!-- Brand Section -->
        <div class="footer-brand-section">
          <div class="footer-brand">
            <img src="/Mumble_Lettering_Negativo.svg" alt="Mumble Logo" class="footer-logo" />
          </div>
          <p class="footer-tagline">
            Ascoltiamo. Progettiamo. Realizziamo.
          </p>
          <p class="footer-description">
            Software house B2B specializzata in gestionali su misura e automazione dei processi aziendali.
            Trasformiamo le tue idee in soluzioni digitali efficaci.
          </p>
          <div class="footer-contact-info">
            <a href="mailto:info@mumble.group" class="contact-item">
              <span class="contact-icon">✉</span>
              <span class="contact-text">info@mumble.group</span>
            </a>
            <a href="tel:+39123456789" class="contact-item">
              <span class="contact-icon">📞</span>
              <span class="contact-text">+39 123 456 789</span>
            </a>
          </div>
        </div>

        <!-- Services Section -->
        <div class="footer-section">
          <h4 class="footer-section-title">Servizi</h4>
          <div class="footer-subsection">
            <h5>Sviluppo</h5>
            <ul class="footer-links">
              <li><a href="/servizi#development">Development</a></li>
              <li><a href="/servizi#webapp-ux">Web App & UX/UI</a></li>
            </ul>
          </div>
          <div class="footer-subsection">
            <h5>Integrazione</h5>
            <ul class="footer-links">
              <li><a href="/servizi#api-integration">Integrazioni API</a></li>
              <li><a href="/servizi#portali">Portali & Piattaforme</a></li>
            </ul>
          </div>
          <div class="footer-subsection">
            <h5>Gestione</h5>
            <ul class="footer-links">
              <li><a href="/servizi#crm-erp">CRM e ERP</a></li>
              <li><a href="/servizi#business-intelligence">Business Intelligence</a></li>
            </ul>
          </div>
        </div>

        <!-- Projects Section -->
        <div class="footer-section">
          <h4 class="footer-section-title">Progetti</h4>
          <ul class="footer-links">
            <li><a href="/progetti/hoteltarget">HotelTarget</a></li>
            <li><a href="/progetti/vinovero">Vinovero</a></li>
            <li><a href="/progetti/pinbowl">Pinbowl</a></li>
            <li><a href="/progetti/if65">IF65</a></li>
            <li><a href="/progetti/crejob">CreJob</a></li>
            <li><a href="/progetti/roda">Roda</a></li>
          </ul>
          <div class="footer-cta">
            <router-link to="/progetti" class="footer-cta-link">
              Vedi tutti i progetti →
            </router-link>
          </div>
        </div>

        <!-- Company Section -->
        <div class="footer-section">
          <h4 class="footer-section-title">Azienda</h4>
          <ul class="footer-links">
            <li><a href="/chi-siamo">Chi siamo</a></li>
            <li><a href="/processo">Il nostro processo</a></li>
            <li><a href="/tecnologie">Tecnologie</a></li>
            <li><a href="/contatti">Contatti</a></li>
          </ul>

          <div class="footer-subsection">
            <h5>Seguici</h5>
            <div class="social-links">
              <a href="#" class="social-link" aria-label="LinkedIn">
                <span class="social-icon">💼</span>
              </a>
              <a href="#" class="social-link" aria-label="GitHub">
                <span class="social-icon">🔗</span>
              </a>
              <a href="#" class="social-link" aria-label="Email">
                <span class="social-icon">✉️</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Newsletter Section -->
    <div class="footer-newsletter">
      <div class="footer-container">
        <div class="newsletter-content">
          <div class="newsletter-text">
            <h4>Rimani aggiornato</h4>
            <p>Ricevi insights su tecnologia e digitalizzazione aziendale</p>
          </div>
          <div class="newsletter-form">
            <input
              type="email"
              placeholder="La tua email"
              class="newsletter-input"
              v-model="newsletterEmail"
            />
            <button class="newsletter-btn" @click="subscribeNewsletter">
              Iscriviti
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Bottom -->
    <div class="footer-bottom">
      <div class="footer-container">
        <div class="footer-bottom-content">
          <div class="footer-legal">
            <p class="footer-copyright">
              © {{ currentYear }} {{ siteTitle }}. Tutti i diritti riservati.
            </p>
            <div class="footer-legal-links">
              <a href="/privacy">Privacy Policy</a>
              <a href="/cookie">Cookie Policy</a>
              <a href="/termini">Termini di Servizio</a>
            </div>
          </div>
          <div class="footer-made-by">
            <p class="made-with">
              Fatto con <span class="heart">❤️</span> da Mumble
            </p>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { apiService } from '../services/api.js'

const siteTitle = ref('Mumble')
const currentYear = computed(() => new Date().getFullYear())
const newsletterEmail = ref('')

// Newsletter subscription
const subscribeNewsletter = async () => {
  if (!newsletterEmail.value) {
    alert('Inserisci una email valida')
    return
  }

  try {
    // Qui potresti integrare con un servizio di newsletter
    console.log('Newsletter subscription:', newsletterEmail.value)
    alert('Grazie per la tua iscrizione!')
    newsletterEmail.value = ''
  } catch (error) {
    console.error('Newsletter subscription error:', error)
    alert('Errore durante l\'iscrizione. Riprova più tardi.')
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
})
</script>

<style scoped>
/* Mega Footer */
.mega-footer {
  background: #000;
  color: #fff;
  margin-top: 0;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

/* Main Footer Content */
.footer-main {
  padding: 80px 0 60px;
}

.footer-main .footer-container {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 60px;
  align-items: start;
}

/* Brand Section */
.footer-brand-section {
  max-width: 400px;
}

.footer-brand {
  margin-bottom: 20px;
}

.footer-logo {
  height: 40px;
  width: auto;
}

.footer-tagline {
  font-family: var(--font-mono);
  font-size: 16px;
  font-weight: 600;
  color: #fff;
  margin: 0 0 16px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.footer-description {
  font-size: 16px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
  margin: 0 0 32px;
}

.footer-contact-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 12px;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s ease;
}

.contact-item:hover {
  color: #fff;
}

.contact-icon {
  font-size: 16px;
  width: 20px;
  text-align: center;
}

/* Footer Sections */
.footer-section {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.footer-section-title {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  margin: 0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.footer-subsection {
  margin-bottom: 20px;
}

.footer-subsection h5 {
  font-size: 13px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.8);
  margin: 0 0 8px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s ease;
  line-height: 1.4;
}

.footer-links a:hover {
  color: #fff;
}

.footer-cta {
  margin-top: 16px;
}

.footer-cta-link {
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 600;
  color: #fff;
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 8px 16px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 6px;
  transition: all 0.3s ease;
  display: inline-block;
}

.footer-cta-link:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateX(4px);
}

/* Social Links */
.social-links {
  display: flex;
  gap: 12px;
  margin-top: 8px;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  text-decoration: none;
  transition: all 0.3s ease;
}

.social-link:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}

.social-icon {
  font-size: 16px;
}

/* Newsletter Section */
.footer-newsletter {
  background: rgba(255, 255, 255, 0.05);
  padding: 40px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.newsletter-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: center;
}

.newsletter-text h4 {
  font-family: var(--font-mono);
  font-size: 18px;
  font-weight: 600;
  color: #fff;
  margin: 0 0 8px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.newsletter-text p {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.7);
  margin: 0;
  line-height: 1.5;
}

.newsletter-form {
  display: flex;
  gap: 12px;
}

.newsletter-input {
  flex: 1;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  color: #fff;
  font-size: 14px;
  transition: all 0.3s ease;
}

.newsletter-input::placeholder {
  color: rgba(255, 255, 255, 0.5);
}

.newsletter-input:focus {
  outline: none;
  border-color: rgba(255, 255, 255, 0.4);
  background: rgba(255, 255, 255, 0.15);
}

.newsletter-btn {
  padding: 12px 24px;
  background: #fff;
  color: #000;
  border: none;
  border-radius: 8px;
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.newsletter-btn:hover {
  background: rgba(255, 255, 255, 0.9);
  transform: translateY(-1px);
}

/* Footer Bottom */
.footer-bottom {
  padding: 32px 0;
}

.footer-bottom-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
}

.footer-legal {
  display: flex;
  align-items: center;
  gap: 32px;
}

.footer-copyright {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
  margin: 0;
}

.footer-legal-links {
  display: flex;
  gap: 24px;
}

.footer-legal-links a {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-legal-links a:hover {
  color: rgba(255, 255, 255, 0.8);
}

.footer-made-by {
  text-align: right;
}

.made-with {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
  margin: 0;
}

.heart {
  color: #ff6b6b;
  animation: heartbeat 2s ease-in-out infinite;
}

@keyframes heartbeat {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}

/* Responsive Design */
@media (max-width: 1024px) {
  .footer-main .footer-container {
    grid-template-columns: 1fr 1fr;
    gap: 40px;
  }

  .footer-brand-section {
    grid-column: 1 / -1;
    max-width: none;
    margin-bottom: 20px;
  }
}

@media (max-width: 768px) {
  .footer-main {
    padding: 60px 0 40px;
  }

  .footer-main .footer-container {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .newsletter-content {
    grid-template-columns: 1fr;
    gap: 24px;
    text-align: center;
  }

  .newsletter-form {
    flex-direction: column;
  }

  .footer-bottom-content {
    flex-direction: column;
    text-align: center;
    gap: 16px;
  }

  .footer-legal {
    flex-direction: column;
    gap: 16px;
  }

  .footer-legal-links {
    justify-content: center;
  }

  .footer-made-by {
    text-align: center;
  }
}

@media (max-width: 480px) {
  .footer-container {
    padding: 0 16px;
  }

  .footer-main {
    padding: 40px 0 32px;
  }

  .footer-newsletter {
    padding: 32px 0;
  }

  .footer-bottom {
    padding: 24px 0;
  }

  .footer-legal-links {
    flex-direction: column;
    gap: 8px;
  }
}
</style>
