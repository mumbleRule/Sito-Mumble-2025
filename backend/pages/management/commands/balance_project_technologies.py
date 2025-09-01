from django.core.management.base import BaseCommand
from pages.models import Project


class Command(BaseCommand):
    help = 'Bilancia le tecnologie dei progetti per avere lunghezza uniforme'

    def handle(self, *args, **options):
        try:
            # Tecnologie bilanciate (circa 25-30 caratteri)
            technologies = {
                'Hotel Target': 'Django, Vue.js, PostgreSQL',  # 26 caratteri - OK
                'Vinovero': 'Django, Vue.js, Redis',           # 20 caratteri
                'Pinbowl': 'Django, Vue.js, Stripe',           # 22 caratteri  
                'IF65': 'Django, React, PostgreSQL',           # 24 caratteri
                'CreJob': 'Django, Vue.js, PostgreSQL',        # 26 caratteri
                'Roda': 'Django, Vue.js, API Integration'      # 30 caratteri
            }
            
            updated_count = 0
            
            for title, tech in technologies.items():
                try:
                    project = Project.objects.get(title=title)
                    project.technologies = tech
                    project.save()
                    updated_count += 1
                    self.stdout.write(f'✅ Bilanciato: {title} ({len(tech)} caratteri)')
                except Project.DoesNotExist:
                    self.stdout.write(f'⚠️ Progetto non trovato: {title}')
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ Bilanciate {updated_count} tecnologie progetti!')
            )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Errore durante il bilanciamento: {e}')
            )
