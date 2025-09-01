from django.core.management.base import BaseCommand
from pages.models import Project


class Command(BaseCommand):
    help = 'Bilancia le descrizioni dei progetti per avere lunghezza uniforme'

    def handle(self, *args, **options):
        try:
            # Descrizioni bilanciate (circa 80-90 caratteri per uniformità)
            descriptions = {
                'Hotel Target': 'CRM personalizzato per consulenza alberghiera con gestione clienti e marketing.',
                'Vinovero': 'Gestionale ERP per enoteche con vendita al bicchiere e gestione inventario.',
                'Pinbowl': 'Software di gestione completo per skatepark con prenotazioni ed eventi.',
                'IF65': 'Piattaforma di project management per progetti IT con tracking e reporting.',
                'CreJob': 'Portale per soggiorni e tirocini all\'estero con matching automatico.',
                'Roda': 'Sistema gestionale manifatturiero con controllo produzione e ordini.'
            }
            
            updated_count = 0
            
            for title, description in descriptions.items():
                try:
                    project = Project.objects.get(title=title)
                    project.description = description
                    project.save()
                    updated_count += 1
                    self.stdout.write(f'✅ Bilanciato: {title} ({len(description)} caratteri)')
                except Project.DoesNotExist:
                    self.stdout.write(f'⚠️ Progetto non trovato: {title}')
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ Bilanciate {updated_count} descrizioni progetti!')
            )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Errore durante il bilanciamento: {e}')
            )
