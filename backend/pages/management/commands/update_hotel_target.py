from django.core.management.base import BaseCommand
from pages.models import Project


class Command(BaseCommand):
    help = 'Aggiorna le tecnologie del progetto Hotel Target rimuovendo Email Marketing API'

    def handle(self, *args, **options):
        try:
            # Trova il progetto Hotel Target
            hotel_target = Project.objects.filter(title='Hotel Target').first()
            
            if hotel_target:
                # Aggiorna le tecnologie rimuovendo "Email Marketing API"
                hotel_target.technologies = 'Django, Vue.js, PostgreSQL'
                hotel_target.save()
                
                self.stdout.write(
                    self.style.SUCCESS('✅ Progetto Hotel Target aggiornato con successo!')
                )
                self.stdout.write(
                    f'Nuove tecnologie: {hotel_target.technologies}'
                )
            else:
                self.stdout.write(
                    self.style.WARNING('⚠️ Progetto Hotel Target non trovato nel database')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Errore durante l\'aggiornamento: {e}')
            )
