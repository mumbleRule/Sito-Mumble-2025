from django.core.management.base import BaseCommand
from pages.models import Project


class Command(BaseCommand):
    help = 'Ripristina le descrizioni originali dei progetti'

    def handle(self, *args, **options):
        try:
            # Descrizioni originali ripristinate
            descriptions = {
                'Hotel Target': 'CRM personalizzato per consulenza alberghiera. Gestione clienti, attività marketing e sales, email marketing automatizzato e tracking completo per strutture ricettive.',
                'Vinovero': 'Gestionale ERP completo per la catena di enoteche con vendita al bicchiere. Sistema integrato per gestione inventario, vendite e analytics.',
                'Pinbowl': 'Software di gestione completo per il più grande skatepark indoor d\'Europa. Gestione prenotazioni, eventi e membership.',
                'IF65': 'Piattaforma avanzata di project management per progetti IT complessi. Sistema di tracking, reporting e collaborazione in tempo reale.',
                'CreJob': 'Piattaforma digitale per soggiorni e tirocini all\'estero per studenti. Matching automatico e gestione completa del processo.',
                'Roda': 'Sistema gestionale per azienda manifatturiera con controllo produzione, gestione ordini, inventario e integrazione con sistemi ERP esistenti.'
            }
            
            updated_count = 0
            
            for title, description in descriptions.items():
                try:
                    project = Project.objects.get(title=title)
                    project.description = description
                    project.save()
                    updated_count += 1
                    self.stdout.write(f'✅ Ripristinato: {title}')
                except Project.DoesNotExist:
                    self.stdout.write(f'⚠️ Progetto non trovato: {title}')
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ Ripristinate {updated_count} descrizioni originali!')
            )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Errore durante il ripristino: {e}')
            )
