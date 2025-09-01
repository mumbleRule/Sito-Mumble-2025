from django.core.management.base import BaseCommand
from pages.models import Project


class Command(BaseCommand):
    help = 'Aggiorna le descrizioni dei progetti per avere lunghezza uniforme'

    def handle(self, *args, **options):
        try:
            # Descrizioni uniformi (circa 100-120 caratteri)
            descriptions = {
                'Hotel Target': 'Sistema CRM completo per consulenza alberghiera. Gestisce marketing, vendite e tracking clienti nel settore hospitality.',
                'Vinovero': 'Piattaforma e-commerce per vini pregiati con gestione inventario, catalogo prodotti e integrazione pagamenti.',
                'Pinbowl': 'Sistema di prenotazione per bowling center. Include booking online, gestione piste e sistema di pagamento integrato.',
                'IF65': 'Piattaforma di project management per team distribuiti con tracking attività e reportistica avanzata.',
                'CreJob': 'Portale per formazione professionale che connette studenti e aziende con gestione corsi e certificazioni.',
                'Roda': 'Sistema gestionale manifatturiero con controllo produzione, gestione ordini e integrazione ERP esistenti.'
            }
            
            updated_count = 0
            
            for title, description in descriptions.items():
                try:
                    project = Project.objects.get(title=title)
                    project.description = description
                    project.save()
                    updated_count += 1
                    self.stdout.write(f'✅ Aggiornato: {title}')
                except Project.DoesNotExist:
                    self.stdout.write(f'⚠️ Progetto non trovato: {title}')
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ Aggiornate {updated_count} descrizioni progetti!')
            )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Errore durante l\'aggiornamento: {e}')
            )
