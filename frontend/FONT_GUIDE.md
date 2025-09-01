# 🎨 Guida Font - Mumble.group

## Font utilizzati

### 1. **FK Grotesk** (Font principale)
- **Uso**: Tutto il testo generale, titoli, paragrafi, navigazione
- **Carattere**: Amichevole, moderno, leggibile
- **Pesi**: 300 (light), 400 (regular), 500 (medium), 600 (semibold)

### 2. **IBM Plex Mono** (Font tecnico)
- **Uso**: Elementi tecnici, codice, acronimi, tecnologie
- **Carattere**: Professionale, tecnico, preciso
- **Pesi**: 300 (light), 400 (regular), 500 (medium), 600 (semibold)

## Quando usare IBM Plex Mono

### ✅ Elementi tecnici:
- **Titoli sezioni e card**: Tutti i titoli h2, h3
- **Bottoni CTA**: Tutti i bottoni e link
- **Eyebrow labels**: "Software house B2B", "Portfolio", etc.
- **Acronimi nel testo**: `TOC`, `AI`, `API`, `REST`, `JSON`
- **Tecnologie**: `Django`, `Vue.js`, `Python`, `JavaScript`
- **Codice e comandi**: `npm install`, `git clone`
- **URL e endpoint**: `/api/services/`, `https://mumble.group`

### ✅ Classi CSS disponibili:
```css
.font-mono          /* Applica IBM Plex Mono */
.tech-label         /* Label tecnico con stile */
.api-endpoint       /* Stile per endpoint API */
.code               /* Stile per codice inline */
```

### ✅ Esempi di utilizzo:

**HTML:**
```html
<span class="font-mono">API</span>
<div class="tech-label">TOC = Theory of Constraints</div>
<code>npm run dev</code>
```

**Vue.js:**
```vue
<h3>Strategie <span class="font-mono">TOC</span> & <span class="font-mono">AI</span></h3>
<p>Tecnologie: <span class="font-mono">{{ project.technologies }}</span></p>
```

## Quando usare FK Grotesk

### ✅ Tutto il resto:
- Titoli e sottotitoli
- Paragrafi e descrizioni
- Navigazione
- Bottoni e call-to-action
- Form e input
- Messaggi utente

## Variabili CSS

```css
:root {
  --font-main: 'FK Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  --font-mono: 'IBM Plex Mono', 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
}
```

## Fallback

Entrambi i font hanno fallback appropriati:
- **FK Grotesk** → System fonts (Apple, Windows, Linux)
- **IBM Plex Mono** → Monospace fonts di sistema

## Caricamento

I font vengono caricati da:
- **FK Grotesk**: Fontshare (gratuito)
- **IBM Plex Mono**: Google Fonts (gratuito)

Entrambi sono ottimizzati per il web con `display=swap` per evitare FOIT (Flash of Invisible Text).

## Esempi nel sito

### Homepage:
- **Eyebrow**: `font-mono` → "Software house B2B"
- **Titolo**: `font-main` → "Gestionale su misura..."
- **Servizi**: Mix di entrambi per evidenziare parti tecniche

### Progetti:
- **Tecnologie**: `font-mono` → "Django, Vue.js, PostgreSQL"
- **Descrizione**: `font-main` → Testo normale

### Contatti:
- **Form**: `font-main` → Tutto il form
- **Email**: `font-mono` → "info@mumble.group"
