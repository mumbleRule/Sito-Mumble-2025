from django.core.management.base import BaseCommand
from pages.models import SiteSettings


class Command(BaseCommand):
    help = 'Aggiorna il contenuto dell\'hero section con i nuovi testi'

    def handle(self, *args, **options):
        try:
            # Prova a ottenere le impostazioni esistenti
            settings = SiteSettings.objects.first()
            
            if settings:
                # Aggiorna i contenuti esistenti
                settings.hero_title = "Soluzioni software su misura.\nProcessi automatizzati.\nBusiness accelerato."
                settings.hero_subtitle = "Sviluppiamo piattaforme web che semplificano il lavoro e fanno crescere le aziende."
                settings.hero_description = "Dalla progettazione allo sviluppo, creiamo soluzioni digitali che trasformano le sfide quotidiane in opportunità di crescita per il tuo business."
                settings.save()
                
                self.stdout.write(
                    self.style.SUCCESS('✅ Contenuto hero aggiornato con successo!')
                )
            else:
                # Crea nuove impostazioni se non esistono
                SiteSettings.objects.create(
                    site_title="Mumble",
                    hero_title="Soluzioni software su misura.\nProcessi automatizzati.\nBusiness accelerato.",
                    hero_subtitle="Sviluppiamo piattaforme web che semplificano il lavoro e fanno crescere le aziende.",
                    hero_description="Dalla progettazione allo sviluppo, creiamo soluzioni digitali che trasformano le sfide quotidiane in opportunità di crescita per il tuo business.",
                    contact_email="info@mumble.group"
                )
                
                self.stdout.write(
                    self.style.SUCCESS('✅ Nuove impostazioni create con successo!')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Errore durante l\'aggiornamento: {e}')
            )
