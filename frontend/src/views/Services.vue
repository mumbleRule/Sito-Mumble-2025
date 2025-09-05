<template>
  <div class="services-page">
    <!-- Hero Section -->
    <section class="services-hero">
      <div class="container">
        <div class="hero-content">
          <div class="eyebrow font-mono">I nostri servizi</div>
          <h1>Risolviamo i problemi che rallentano il tuo business.</h1>
          <p class="hero-subtitle">
            Development, integrazioni, gestionali.
          </p>
        </div>
      </div>
    </section>

    <!-- Services Overview Section -->
    <section class="services-overview-section">
      <div class="container">
        <div class="overview-header">
          <h2>Tre aree dove facciamo la differenza</h2>
        </div>

        <div class="overview-grid">
          <div class="overview-card">
            <h3>Software scritto su misura per te</h3>
            <div class="overview-tag sage">Sviluppo</div>
            <p>Zero template. Ogni progetto nasce per i tuoi processi. Python, Django, Vue.js: tecnologie affidabili per software che dura nel tempo.</p>
            <div class="what-we-do">
              <h4>Cosa sviluppiamo:</h4>
              <ul class="overview-features">
                <li>Gestionali aziendali personalizzati</li>
                <li>Web app e piattaforme B2B</li>
                <li>Sistemi di prenotazione e booking</li>
                <li>App mobile integrate con backend</li>
              </ul>
            </div>
          </div>

          <div class="overview-card">
            <h3>Sistemi che collaborano</h3>
            <div class="overview-tag warm-clay">Integrazioni</div>
            <p>Facciamo parlare i tuoi software tra loro. API, webhooks, sincronizzazioni automatiche per eliminare il lavoro manuale e gli errori.</p>
            <div class="what-we-do">
              <h4>Cosa integriamo:</h4>
              <ul class="overview-features">
                <li>CRM con sistemi di email marketing</li>
                <li>E-commerce con gestione magazzino</li>
                <li>App mobile con gestionali esistenti</li>
                <li>Sistemi di prenotazione con calendari</li>
              </ul>
            </div>
          </div>

          <div class="overview-card">
            <h3>Il controllo del tuo business</h3>
            <div class="overview-tag muted">Gestionali</div>
            <p>CRM, ERP, dashboard: sistemi completi per gestire clienti, vendite e processi. Tutto centralizzato, tutto sotto controllo.</p>
            <div class="what-we-do">
              <h4>Cosa gestiamo:</h4>
              <ul class="overview-features">
                <li>Clienti e pipeline di vendita</li>
                <li>Magazzino e movimenti stock</li>
                <li>Ordini e spedizioni</li>
                <li>Analytics e reportistica</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sviluppo Section -->
    <section id="sviluppo" class="sviluppo-section">
      <div class="container">
        <div class="category-header">
          <h2>Sviluppo</h2>
          <p class="category-description">
            Sviluppiamo soluzioni software complete utilizzando tecnologie moderne e architetture scalabili.
          </p>
        </div>

        <div class="category-services">
          <div id="development" class="service-card">
            <div class="service-header">
              <h3>Development su misura</h3>
              <div class="service-tags">
                <span class="tag">Python</span>
                <span class="tag">Django</span>
                <span class="tag">Vue.js</span>
              </div>
            </div>
            <p class="service-description">
              Trasformiamo le tue idee in software potenti e su misura. Ogni riga di codice è pensata per i tuoi processi specifici, creando soluzioni che si adattano perfettamente al modo in cui lavori. Niente compromessi, niente limitazioni: solo tecnologia che amplifica le tue capacità.
            </p>
            <div class="use-cases">
              <h4>Progetti che realizziamo:</h4>
              <ul>
                <li>Sistema di prenotazioni per spa con gestione trattamenti e terapisti</li>
                <li>Gestionale vinicola con tracciabilità dalla vigna alla bottiglia</li>
                <li>Sistema per agenzie di marketing con campagne e reporting clienti</li>
              </ul>
            </div>
          </div>

          <div id="webapp-ux" class="service-card">
            <div class="service-header">
              <h3>Web App & UX/UI</h3>
              <div class="service-tags">
                <span class="tag">Design</span>
                <span class="tag">UX/UI</span>
                <span class="tag">Responsive</span>
              </div>
            </div>
            <p class="service-description">
              Creiamo esperienze digitali che conquistano al primo clic. Ogni interfaccia è studiata per essere intuitiva, bella e funzionale. I tuoi utenti non dovranno mai chiedersi "come funziona?" - tutto sarà naturale e immediato, su qualsiasi dispositivo.
            </p>
            <div class="use-cases">
              <h4>Esperienze che progettiamo:</h4>
              <ul>
                <li>App per personal trainer con piani di allenamento personalizzati</li>
                <li>Dashboard immobiliare con mappe interattive e tour virtuali</li>
                <li>App di delivery con tracking in tempo reale e chat con rider</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Integrazione Section -->
    <section id="integrazione" class="integrazione-section">
      <div class="container">
        <div class="category-header">
          <h2>Integrazione</h2>
          <p class="category-description">
            Colleghiamo e sincronizziamo i tuoi sistemi esistenti per automatizzare i processi aziendali.
          </p>
        </div>

        <div class="category-services">
          <div id="api-integration" class="service-card">
            <div class="service-header">
              <h3>Integrazioni API</h3>
              <div class="service-tags">
                <span class="tag">REST API</span>
                <span class="tag">Webhooks</span>
                <span class="tag">Sync</span>
              </div>
            </div>
            <p class="service-description">
              Facciamo dialogare i tuoi software come se fossero stati progettati insieme. Eliminiamo i lavori ripetitivi e gli errori umani creando ponti intelligenti tra le tue piattaforme. I dati fluiscono automaticamente dove servono, quando servono.
            </p>
            <div class="use-cases">
              <h4>Connessioni che realizziamo:</h4>
              <ul>
                <li>E-commerce che aggiorna automaticamente stock e spedizioni su Amazon</li>
                <li>CRM che invia SMS personalizzati quando un lead diventa cliente</li>
                <li>App mobile che carica foto direttamente nel gestionale cantieri</li>
              </ul>
            </div>
          </div>

          <div id="portali" class="service-card">
            <div class="service-header">
              <h3>Portali & Piattaforme</h3>
              <div class="service-tags">
                <span class="tag">Portali</span>
                <span class="tag">B2B</span>
                <span class="tag">Scalabilità</span>
              </div>
            </div>
            <p class="service-description">
              Costruiamo ecosistemi digitali dove clienti, fornitori e partner collaborano senza attriti. Piattaforme che diventano il cuore pulsante del tuo business, gestendo relazioni complesse con semplicità e crescendo insieme alla tua azienda.
            </p>
            <div class="use-cases">
              <h4>Ecosistemi che costruiamo:</h4>
              <ul>
                <li>Marketplace per artigiani con portfolio, preventivi e recensioni</li>
                <li>Portale distributori con listini dinamici e ordini automatici</li>
                <li>Hub logistico con tracking spedizioni e gestione resi</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Gestione Section -->
    <section id="gestione" class="gestione-section">
      <div class="container">
        <div class="category-header">
          <h2>Gestione</h2>
          <p class="category-description">
            Sistemi di gestione aziendale e business intelligence per ottimizzare i processi operativi.
          </p>
        </div>

        <div class="category-services">
          <div id="crm-erp" class="service-card">
            <div class="service-header">
              <h3>CRM e ERP</h3>
              <div class="service-tags">
                <span class="tag">CRM</span>
                <span class="tag">ERP</span>
                <span class="tag">Gestionale</span>
              </div>
            </div>
            <p class="service-description">
              Sostituiamo i tuoi fogli Excel con sistemi intelligenti che pensano al posto tuo. Ogni cliente, ogni prodotto, ogni processo viene orchestrato in perfetta armonia. Il tuo business diventa una macchina ben oliata che funziona anche mentre dormi.
            </p>
            <div class="use-cases">
              <h4>Sistemi che orchestriamo:</h4>
              <ul>
                <li>CRM per agenzie immobiliari con lead scoring e follow-up automatici</li>
                <li>Gestionale per ristoranti con menu engineering e food cost</li>
                <li>ERP per produzione con pianificazione materiali e quality control</li>
              </ul>
            </div>
          </div>

          <div id="business-intelligence" class="service-card">
            <div class="service-header">
              <h3>Business Intelligence</h3>
              <div class="service-tags">
                <span class="tag">Dashboard</span>
                <span class="tag">Analytics</span>
                <span class="tag">Reporting</span>
              </div>
            </div>
            <p class="service-description">
              Trasformiamo montagne di dati in cristalline intuizioni di business. Le tue decisioni non saranno più basate su sensazioni, ma su evidenze precise e predizioni intelligenti. Vedi il futuro del tuo business prima che accada.
            </p>
            <div class="use-cases">
              <h4>Intelligence che sviluppiamo:</h4>
              <ul>
                <li>Dashboard per catene retail con heatmap vendite e stock optimization</li>
                <li>Sistema predittivo per e-commerce con raccomandazioni personalizzate</li>
                <li>Analytics per startup con cohort analysis e churn prediction</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Come lavoriamo Section -->
    <section class="how-we-work-section">
      <div class="container">
        <div class="how-we-work-header">
          <div class="eyebrow font-mono">Approccio</div>
          <h2>Come lavoriamo</h2>
          <p class="approach-lead">
            Dal primo incontro al rilascio. Un processo collaudato per risultati concreti
          </p>
        </div>

        <div class="work-process">
          <div class="process-step fade-in">
            <div class="process-step-header">
              <div class="step-number sage">1</div>
              <h3>Ascoltiamo</h3>
            </div>
            <p>Capiamo i tuoi processi attuali e dove perdono efficienza. Ogni progetto inizia dall'analisi dei tuoi flussi di lavoro.</p>
          </div>

          <div class="process-step fade-in">
            <div class="process-step-header">
              <div class="step-number warm-clay">2</div>
              <h3>Progettiamo</h3>
            </div>
            <p>Disegniamo la soluzione più semplice che risolve il problema. Wireframe, mockup e architettura pensati per durare.</p>
          </div>

          <div class="process-step fade-in">
            <div class="process-step-header">
              <div class="step-number muted">3</div>
              <h3>Sviluppiamo</h3>
            </div>
            <p>Codice pulito, test approfonditi, rilasci graduali. Ogni funzionalità viene testata prima di arrivare in produzione.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="services-cta-section">
      <div class="container">
        <div class="services-cta">
          <h2>Hai un'idea? Realizziamola insieme.</h2>
          <p>
            Ogni progetto è unico. Raccontaci la tua sfida e ti spieghiamo come trasformarla in software che funziona.
          </p>
          <div class="cta-buttons">
            <router-link to="/contatti" class="btn primary">
              Parliamo del tuo progetto
            </router-link>
            <router-link to="/progetti" class="btn secondary">
              Vedi i nostri lavori
            </router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// Nessuna logica particolare necessaria per ora
</script>

<style scoped>
/* Scroll offset per navbar fissa */
#sviluppo,
#development,
#webapp-ux,
#integrazione,
#api-integration,
#portali,
#gestione,
#crm-erp,
#business-intelligence {
  scroll-margin-top: 100px;
}

/* Hero Section */
.services-hero {
  background: var(--bg);
  padding: clamp(100px, 12vw, 140px) 0 clamp(40px, 6vw, 60px);
  width: 100%;
  position: relative;
}

.services-hero .container {
  max-width: 1400px;
  padding: 0 clamp(40px, 8vw, 120px);
}

.services-hero::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 200px;
  height: 200px;
  background: linear-gradient(135deg, var(--sage) 0%, transparent 70%);
  opacity: 0.03;
  border-radius: 50%;
  transform: translate(50%, -50%);
}

.hero-content {
  text-align: left;
  max-width: 900px;
  position: relative;
  z-index: 1;
}

.hero-content .eyebrow {
  color: var(--muted);
  font-size: 16px;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 32px;
  font-family: var(--font-mono);
}

.hero-content h1 {
  font-size: clamp(42px, 6vw, 64px);
  margin: 0 0 32px;
  font-weight: 400;
  line-height: 1.1;
  color: var(--fg);
  letter-spacing: -0.01em;
}

.hero-subtitle {
  font-size: clamp(20px, 2.5vw, 26px);
  line-height: 1.5;
  color: var(--muted);
  margin: 0;
  font-weight: 300;
}

/* Services Overview Section */
.services-overview-section {
  background: var(--bg);
  padding: clamp(40px, 6vw, 60px) 0 clamp(80px, 10vw, 120px);
  width: 100%;
  position: relative;
}

.services-overview-section .container {
  max-width: 1400px;
  padding: 0 clamp(40px, 8vw, 120px);
}

.overview-header {
  text-align: left;
  margin-bottom: 48px;
  max-width: 800px;
}

.overview-header h2 {
  font-size: clamp(32px, 4vw, 40px);
  margin: 0;
  font-weight: 400;
  color: var(--fg);
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: clamp(24px, 4vw, 48px);
}

.overview-card {
  background: var(--chip-bg);
  border-radius: 20px;
  padding: 40px;
  text-align: left;
  transition: all 0.4s ease;
  border: 1px solid var(--line);
  position: relative;
  overflow: hidden;
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.overview-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
}

/* Animazioni progressive per le card */
.overview-card:nth-child(1) {
  animation-delay: 0.1s;
}

.overview-card:nth-child(2) {
  animation-delay: 0.3s;
}

.overview-card:nth-child(3) {
  animation-delay: 0.5s;
}



.overview-tag {
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 24px;
  display: inline-block;
  color: white;
  position: relative;
  animation: tagPulse 2s infinite;
}

.overview-tag.sage {
  background: var(--sage);
  animation-delay: 0s;
}

.overview-tag.warm-clay {
  background: var(--warm-clay);
  animation-delay: 0.3s;
}

.overview-tag.muted {
  background: var(--muted);
  animation-delay: 0.6s;
}

.overview-card h3 {
  font-size: 32px;
  margin: 0 0 28px;
  font-weight: 500;
  color: var(--fg);
  line-height: 1.2;
}

.overview-card p {
  font-size: 17px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0 0 32px;
}

.overview-features {
  list-style: none;
  padding: 0;
  margin: 0;
}

.overview-features li {
  font-size: 14px;
  color: var(--fg);
  margin-bottom: 8px;
  padding-left: 16px;
  position: relative;
}

.overview-features li::before {
  content: '→';
  position: absolute;
  left: 0;
  color: var(--sage);
  font-weight: 600;
}

/* Colori specifici per le frecce delle diverse card */
.overview-card:has(.overview-tag.warm-clay) .overview-features li::before {
  color: var(--warm-clay);
}

.overview-card:has(.overview-tag.muted) .overview-features li::before {
  color: var(--muted);
}

.what-we-do {
  margin-top: 24px;
}

.what-we-do h4 {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 600;
  color: var(--fg);
  margin: 0 0 16px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Sottotitolo senza animazione - appare subito */

/* Animazione wordAppear rimossa */

/* Service Sections with Alternating Backgrounds */
.sviluppo-section {
  background: var(--chip-bg);
  padding: 80px 0;
  width: 100%;
}

.integrazione-section {
  background: var(--bg);
  padding: 80px 0;
  width: 100%;
}

.gestione-section {
  background: var(--chip-bg);
  padding: 80px 0;
  width: 100%;
}

/* Card backgrounds per sezione */
.integrazione-section .service-card {
  background: var(--chip-bg);
}

.category-header {
  margin-bottom: 40px;
}

.category-header h2 {
  font-family: var(--font-mono);
  font-size: 28px;
  font-weight: 600;
  color: var(--fg);
  margin: 0 0 16px;
}

.category-description {
  font-size: 18px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
  max-width: 60ch;
}

.category-services {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.service-card {
  background: var(--bg);
  border-radius: 12px;
  padding: 28px;
  border: 1px solid var(--line);
  transition: all 0.3s ease;
}

.service-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
}

.service-header {
  margin-bottom: 16px;
}

.service-header h3 {
  font-family: var(--font-mono);
  font-size: 18px;
  font-weight: 600;
  color: var(--fg);
  margin: 0 0 10px;
}

.service-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  background: none;
}

.service-stack {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 8px;
}

.stack-label {
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 500;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.stack-tech {
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 500;
  color: var(--fg);
}

.stack-separator {
  color: var(--muted);
  font-weight: 400;
}

.tag {
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 500;
  padding: 6px 12px;
  border-radius: 6px;
  animation: tagPulse 2s infinite;
}

/* Colori specifici per ogni tag */
.tag:nth-child(1) {
  background: var(--sage);
  color: white;
  animation-delay: 0s;
}

.tag:nth-child(2) {
  background: var(--warm-clay);
  color: white;
  animation-delay: 0.3s;
}

.tag:nth-child(3) {
  background: var(--muted);
  color: white;
  animation-delay: 0.6s;
}

/* Rimuovi effetti hover sui tag - sovrascrive regole della homepage */
.service-card:hover .service-tags {
  background: none !important;
}

.service-card:hover .service-tags .tag {
  background: inherit !important;
}

.service-card:hover .tag:nth-child(1) {
  background: var(--sage) !important;
  color: white !important;
}

.service-card:hover .tag:nth-child(2) {
  background: var(--warm-clay) !important;
  color: white !important;
}

.service-card:hover .tag:nth-child(3) {
  background: var(--muted) !important;
  color: white !important;
}

@keyframes tagPulse {
  0%, 100% {
    opacity: 0.7;
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(1.05);
  }
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

.fade-in {
  opacity: 0;
  animation: fadeIn 0.6s ease forwards;
}

.service-description {
  font-size: 16px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0 0 20px;
}

/* Use Cases */
.use-cases {
  margin-top: 20px;
}

.use-cases h4 {
  font-family: var(--font-mono);
  font-size: 14px;
  font-weight: 600;
  color: var(--fg);
  margin: 0 0 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.use-cases ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.use-cases li {
  font-size: 14px;
  color: var(--muted);
  padding: 6px 0;
  position: relative;
  padding-left: 16px;
  line-height: 1.4;
}

.use-cases li::before {
  content: '→';
  color: var(--sage);
  font-weight: bold;
  position: absolute;
  left: 0;
  top: 6px;
}

/* Come lavoriamo Section */
.how-we-work-section {
  background: var(--bg);
  padding: 80px 0;
  width: 100%;
}

.how-we-work-section .container {
  max-width: 1400px;
  padding: 0 clamp(40px, 8vw, 120px);
}

.how-we-work-header {
  text-align: left;
  margin-bottom: 60px;
}

.how-we-work-header .eyebrow {
  color: var(--muted);
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.how-we-work-header h2 {
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

.work-process {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: clamp(24px, 4vw, 32px);
}

.process-step {
  background: var(--chip-bg);
  border-radius: 20px;
  padding: 40px;
  text-align: left;
  border: 1px solid var(--line);
  transition: all 0.4s ease;
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.process-step:nth-child(1) {
  animation-delay: 0.1s;
}

.process-step:nth-child(2) {
  animation-delay: 0.3s;
}

.process-step:nth-child(3) {
  animation-delay: 0.5s;
}

.process-step:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
}

.process-step-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.step-number {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-size: 20px;
  font-weight: 600;
  flex-shrink: 0;
  animation: tagPulse 2s infinite;
}

.step-number.sage {
  background: var(--sage);
}

.step-number.warm-clay {
  background: var(--warm-clay);
}

.step-number.muted {
  background: var(--muted);
}

/* Delay specifici per ogni step number */
.process-step:nth-child(1) .step-number {
  animation-delay: 0.2s;
}

.process-step:nth-child(2) .step-number {
  animation-delay: 0.5s;
}

.process-step:nth-child(3) .step-number {
  animation-delay: 0.8s;
}

.process-step h3 {
  font-size: 20px;
  font-weight: 600;
  color: var(--fg);
  margin: 0;
  font-family: var(--font-mono);
}

.process-step p {
  font-size: 16px;
  line-height: 1.6;
  color: var(--muted);
  margin: 0;
}

/* CTA Section */
.services-cta-section {
  background: transparent;
  padding: 20px 0 80px;
}

.services-cta {
  text-align: left;
  max-width: 600px;
  background: transparent;
  padding: 0;
}

.services-cta h2 {
  font-size: clamp(32px, 4vw, 40px);
  margin: 0 0 24px;
  color: var(--fg);
  font-weight: 400;
  line-height: 1.2;
}

.services-cta p {
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
  .services-hero {
    padding: clamp(80px, 10vw, 100px) 0 clamp(60px, 8vw, 80px);
  }

  .services-hero::before {
    width: 150px;
    height: 150px;
  }

  .hero-content .eyebrow {
    font-size: 14px;
    margin-bottom: 24px;
  }

  .hero-content h1 {
    font-size: clamp(32px, 8vw, 42px);
  }

  .hero-subtitle {
    font-size: clamp(18px, 4vw, 22px);
  }

  .services-hero .container,
  .services-overview-section .container,
  .how-we-work-section .container {
    padding: 0 clamp(24px, 6vw, 40px);
  }

  .services-overview-section {
    padding: clamp(32px, 6vw, 40px) 0 clamp(60px, 8vw, 80px);
  }

  .overview-header {
    margin-bottom: 40px;
  }

  .overview-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .overview-card {
    padding: 32px;
  }

  .overview-card h3 {
    font-size: 24px;
  }

  .overview-card p {
    font-size: 16px;
  }
  
  .services-overview-section {
    padding: 0 0 40px;
  }

  .sviluppo-section,
  .integrazione-section,
  .gestione-section {
    padding: 60px 0;
  }

  .overview-grid {
    grid-template-columns: 1fr;
    gap: 32px;
  }

  .overview-card {
    padding: 24px;
  }

  .category-services {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .service-card {
    padding: 20px;
  }
  
  .how-we-work-section {
    padding: 60px 0;
  }

  .how-we-work-header {
    margin-bottom: 40px;
  }

  .work-process {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .process-step {
    padding: 32px;
  }

  .process-step-header {
    gap: 12px;
    margin-bottom: 16px;
  }

  .step-number {
    width: 40px;
    height: 40px;
    font-size: 18px;
  }

  .process-step h3 {
    font-size: 18px;
  }

  .process-step p {
    font-size: 15px;
  }

  .services-cta-section {
    padding: 60px 0;
  }

  .cta-buttons {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
