# Mumble.group - Sito Web

Sito web per Mumble, software house B2B specializzata in gestionali su misura, strategie TOC e AI.

## Architettura

- **Backend**: Django + Django REST Framework
- **Frontend**: Vue.js 3 + Vite
- **Database**: SQLite (sviluppo)
- **Stile**: Design ispirato ad Anthropic

## Struttura del Progetto

```
anthromumble/
├── config/                 # Configurazione Django
├── pages/                  # App Django principale
│   ├── models.py          # Modelli (Service, Project, Contact, SiteSettings)
│   ├── views.py           # API Views
│   ├── serializers.py     # Serializzatori DRF
│   ├── admin.py           # Configurazione admin
│   └── management/        # Comandi personalizzati
├── frontend/              # App Vue.js
│   ├── src/
│   │   ├── components/    # Componenti Vue
│   │   ├── services/      # Servizi API
│   │   └── assets/        # CSS e risorse
│   └── package.json
├── manage.py
└── README.md
```

## Setup e Installazione

### 1. Backend Django

```bash
# Attiva l'ambiente virtuale
source .venv/bin/activate

# Installa dipendenze (già fatto)
pip install django djangorestframework django-cors-headers pillow

# Applica migrazioni (già fatto)
python manage.py migrate

# Popola database con dati di esempio (già fatto)
python manage.py populate_data

# Avvia server Django
python manage.py runserver
```

### 2. Frontend Vue.js

```bash
# Vai nella cartella frontend
cd frontend

# Installa dipendenze Node.js
npm install

# Avvia server di sviluppo
npm run dev
```

## API Endpoints

- `GET /api/settings/` - Impostazioni del sito
- `GET /api/services/` - Lista servizi
- `GET /api/projects/` - Lista progetti
- `GET /api/projects/featured/` - Progetti in evidenza
- `POST /api/contact/` - Invio form contatto

## Accesso Admin

- URL: http://localhost:8000/admin
- Username: admin
- Password: (da impostare con `python manage.py changepassword admin`)

## Funzionalità Implementate

### Backend
- ✅ Modelli per servizi, progetti, contatti e impostazioni
- ✅ API REST complete
- ✅ Admin interface configurata
- ✅ CORS configurato per Vue.js
- ✅ Gestione media files

### Frontend
- ✅ Design Anthropic-style responsive
- ✅ Componenti Vue modulari
- ✅ Integrazione API con axios
- ✅ Form di contatto funzionante
- ✅ Navigazione smooth scroll
- ✅ Gestione stati di caricamento ed errori

## Prossimi Passi

1. **Installare Node.js** se non presente
2. **Testare il frontend** con `npm run dev`
3. **Personalizzare contenuti** tramite admin Django
4. **Aggiungere progetti** nella sezione progetti
5. **Configurare deployment** per produzione

## Sviluppo

### Aggiungere nuovi servizi
1. Vai su http://localhost:8000/admin
2. Sezione "Servizi" → "Aggiungi servizio"
3. Il frontend si aggiornerà automaticamente

### Modificare contenuti hero
1. Admin → "Impostazioni sito"
2. Modifica titoli e descrizioni
3. Salva e ricarica il frontend

### Aggiungere progetti
1. Admin → "Progetti" → "Aggiungi progetto"
2. Carica immagini se necessario
3. Marca come "In evidenza" per homepage

## Note Tecniche

- Il frontend comunica con Django su porta 8000
- CORS configurato per sviluppo locale
- CSS variables per facile personalizzazione temi
- Componenti Vue reattivi e modulari
- Form validation lato client e server
