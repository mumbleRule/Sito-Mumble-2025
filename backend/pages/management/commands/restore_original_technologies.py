from django.core.management.base import BaseCommand
from pages.models import Project


class Command(BaseCommand):
    help = 'Ripristina le tecnologie originali dei progetti'

    def handle(self, *args, **options):
        try:
            # Tecnologie originali dal file add_projects.py
            technologies = {
                'Hotel Target': 'Django, Vue.js, PostgreSQL',
                'Vinovero': 'Django, Vue.js, PostgreSQL, Redis',
                'Pinbowl': 'Django, Vue.js, Stripe API, WebSocket',
                'IF65': 'Django, React, PostgreSQL, Docker',
                'CreJob': 'Django, Vue.js, PostgreSQL, Celery',
                'Roda': 'Django, Vue.js, PostgreSQL, API Integration'
            }
            
            updated_count = 0
            
            for title, tech in technologies.items():
                try:
                    project = Project.objects.get(title=title)
                    project.technologies = tech
                    project.save()
                    updated_count += 1
                    self.stdout.write(f'✅ Ripristinato: {title}')
                except Project.DoesNotExist:
                    self.stdout.write(f'⚠️ Progetto non trovato: {title}')
            
            self.stdout.write(
                self.style.SUCCESS(f'✅ Ripristinate {updated_count} tecnologie originali!')
            )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Errore durante il ripristino: {e}')
            )
