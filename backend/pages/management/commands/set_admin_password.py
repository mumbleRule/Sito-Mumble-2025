from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Imposta la password per l\'utente admin'

    def handle(self, *args, **options):
        try:
            admin_user = User.objects.get(username='admin')
            admin_user.set_password('mumbleadmin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('✓ Password admin impostata: mumbleadmin123'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('✗ Utente admin non trovato'))
