from django.core.management.base import BaseCommand
from pages.models import Service, SiteSettings


class Command(BaseCommand):
    help = 'Popola il database con dati di esempio per il sito Mumble'

    def handle(self, *args, **options):
        self.stdout.write('Popolamento database in corso...')

        # Crea o aggiorna le impostazioni del sito
        site_settings, created = SiteSettings.objects.get_or_create(
            defaults={
                'site_title': 'Mumble',
                'hero_title': 'Gestionale su misura.\nProcessi più fluidi.\nCrescita misurabile.',
                'hero_subtitle': 'Creiamo gestionali B2B che liberano tempo e risorse.',
                'hero_description': 'Trasformiamo la complessità dei tuoi processi in percorsi chiari ed efficienti. Con TOC e AI, ogni ostacolo diventa l\'occasione per accelerare la crescita della tua azienda.',
                'contact_email': 'info@mumble.group',
                'contact_phone': '',
                'is_active': True
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('✓ Impostazioni sito create'))
        else:
            self.stdout.write(self.style.WARNING('→ Impostazioni sito già esistenti'))

        # Crea i servizi se non esistono
        services_data = [
            {
                'title': 'CRM e ERP',
                'description': 'Sistemi di gestione clienti e risorse aziendali su misura. Centralizza vendite, contatti, inventario e processi in un\'unica piattaforma efficiente.',
                'subtitle': 'Gestione aziendale integrata',
                'order': 1
            },
            {
                'title': 'Development',
                'description': 'Gestionali personalizzabili al 100% con codice scritto da zero. Prediligiamo <strong>Python</strong>, <strong>Django</strong>, <strong>Vue.js</strong> e <strong>PostgreSQL</strong>, ma adattiamo la tecnologia alle tue esigenze.',
                'subtitle': 'Codice su misura, risultati concreti',
                'order': 2
            },
            {
                'title': 'Portali & Piattaforme',
                'description': 'Progettiamo e sviluppiamo portali, aree riservate, aree clienti e piattaforme digitali complete.',
                'subtitle': 'Presenza digitale strutturata',
                'order': 3
            },
            {
                'title': 'Web App & UX/UI',
                'description': 'Sviluppiamo web app moderne e ottimizziamo l\'esperienza utente. Collaboriamo con designer esperti per risultati eccellenti.',
                'subtitle': 'Esperienza utente ottimizzata',
                'order': 4
            },
            {
                'title': 'Integrazioni API',
                'description': 'Integriamo il tuo gestionale esistente con nuove funzionalità. Reportistica avanzata e connessioni tra sistemi diversi.',
                'subtitle': 'Ecosistema connesso',
                'order': 5
            }
        ]

        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                title=service_data['title'],
                defaults=service_data
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Servizio creato: {service.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'→ Servizio già esistente: {service.title}'))

        self.stdout.write(self.style.SUCCESS('\n🎉 Popolamento completato con successo!'))
        self.stdout.write('\nPuoi ora:')
        self.stdout.write('1. Avviare il server Django: python manage.py runserver')
        self.stdout.write('2. Avviare il frontend Vue.js: cd frontend && npm run dev')
        self.stdout.write('3. Accedere all\'admin: http://localhost:8000/admin (admin/admin)')
