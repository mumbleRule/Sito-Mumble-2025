from django.core.management.base import BaseCommand
from pages.models import Project
from datetime import date


class Command(BaseCommand):
    help = 'Aggiunge i progetti specifici di Mumble al database'

    def handle(self, *args, **options):
        self.stdout.write('Aggiunta progetti in corso...')

        projects_data = [
            {
                'title': 'Hotel Target',
                'description': 'Piattaforma CRM intelligente che ha rivoluzionato la gestione operativa di Hotel Target. Sistema completo per lead management, automazione marketing e ottimizzazione dei processi di vendita nel settore alberghiero.',
                'client': 'Hotel Target',
                'technologies': 'Django, Vue.js, PostgreSQL',
                'is_featured': True,
                'completed_date': date(2024, 6, 15),
                'category': 'CRM'
            },
            {
                'title': 'Vinovero',
                'description': 'ERP enterprise per enoteca multi-location specializzata in vini naturali. Sistema unificato per gestione acquisti, magazzino, vendite e monitoraggio AI della vendita al bicchiere.',
                'client': 'VinoVero',
                'technologies': 'Django, Vue.js, PostgreSQL, AI/ML',
                'is_featured': True,
                'completed_date': date(2024, 4, 20),
                'category': 'ERP'
            },
            {
                'title': 'Pinbowl',
                'description': 'Gestionale modulare completo per il più grande skatepark indoor d\'Europa. Sistema integrato per gestione lezioni, clienti, marketing, fatturazione e amministrazione.',
                'client': 'Pinbowl',
                'technologies': 'Django, Vue.js, PostgreSQL, Stripe',
                'is_featured': True,
                'completed_date': date(2024, 3, 10),
                'category': 'Gestionale'
            },
            {
                'title': 'IF65',
                'description': 'Piattaforma enterprise di project management per gruppi multi-business. Sistema di coordinamento, monitoraggio e ottimizzazione delle risorse tra diverse divisioni aziendali.',
                'client': 'IF65 Group',
                'technologies': 'Django, Vue.js, PostgreSQL, Docker',
                'is_featured': True,
                'completed_date': date(2024, 2, 5),
                'category': 'Business Management'
            },
            {
                'title': 'CreJob',
                'description': 'Piattaforma digitale per esperienze formative internazionali. Sistema completo di ricerca, prenotazione e gestione soggiorni, tirocini e corsi all\'estero per studenti europei.',
                'client': 'CreJob',
                'technologies': 'Django, Vue.js, PostgreSQL, Elasticsearch',
                'is_featured': True,
                'completed_date': date(2024, 1, 15),
                'category': 'Piattaforma'
            },
            {
                'title': 'Roda',
                'description': 'Sistema backend enterprise per configuratore web di arredamento outdoor di lusso. Architettura scalabile per personalizzazione prodotti, gestione dati complessi e performance ottimali.',
                'client': 'Roda',
                'technologies': 'Django, PostgreSQL, Redis, Docker',
                'is_featured': True,
                'completed_date': date(2023, 12, 20),
                'category': 'Configuratore'
            }
        ]

        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Progetto creato: {project.title}'))
            else:
                # Aggiorna il progetto esistente
                for key, value in project_data.items():
                    setattr(project, key, value)
                project.save()
                self.stdout.write(self.style.WARNING(f'→ Progetto aggiornato: {project.title}'))

        self.stdout.write(self.style.SUCCESS('\n🎉 Progetti aggiunti con successo!'))
        self.stdout.write('I progetti sono ora visibili nella pagina /progetti e nell\'admin Django.')
