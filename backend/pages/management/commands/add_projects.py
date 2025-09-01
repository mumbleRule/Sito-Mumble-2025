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
                'description': 'Gestionale ERP completo per la catena di enoteche con vendita al bicchiere. Sistema integrato per gestione inventario, vendite e analytics.',
                'client': 'Vinovero Enoteche',
                'technologies': 'Django, Vue.js, PostgreSQL, Redis',
                'is_featured': True,
                'completed_date': date(2024, 4, 20),
                'category': 'ERP'
            },
            {
                'title': 'Pinbowl',
                'description': 'Software di gestione completo per il più grande skatepark indoor d\'Europa. Gestione prenotazioni, eventi e membership.',
                'client': 'Pinbowl Skatepark',
                'technologies': 'Django, Vue.js, Stripe API, WebSocket',
                'is_featured': True,
                'completed_date': date(2024, 3, 10),
                'category': 'Gestionale'
            },
            {
                'title': 'IF65',
                'description': 'Piattaforma avanzata di project management per progetti IT complessi. Sistema di tracking, reporting e collaborazione in tempo reale.',
                'client': 'IF65 Consulting',
                'technologies': 'Django, React, PostgreSQL, Docker',
                'is_featured': True,
                'completed_date': date(2024, 2, 5),
                'category': 'Project Management'
            },
            {
                'title': 'CreJob',
                'description': 'Piattaforma digitale per soggiorni e tirocini all\'estero per studenti. Matching automatico e gestione completa del processo.',
                'client': 'CreJob Platform',
                'technologies': 'Django, Vue.js, Elasticsearch, AWS',
                'is_featured': True,
                'completed_date': date(2024, 1, 15),
                'category': 'Piattaforma'
            },
            {
                'title': 'Roda',
                'description': 'Configuratore web interattivo per arredamento outdoor personalizzato. Visualizzazione 3D e preventivi automatici.',
                'client': 'Roda Furniture',
                'technologies': 'Three.js, Django, Vue.js, WebGL',
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
