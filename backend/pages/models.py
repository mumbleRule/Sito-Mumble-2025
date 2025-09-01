from django.db import models


class Service(models.Model):
    """Modello per i servizi offerti da Mumble"""
    title = models.CharField(max_length=200, verbose_name="Titolo")
    description = models.TextField(verbose_name="Descrizione")
    subtitle = models.CharField(max_length=200, blank=True, verbose_name="Sottotitolo")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordine")
    is_active = models.BooleanField(default=True, verbose_name="Attivo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Servizio"
        verbose_name_plural = "Servizi"

    def __str__(self):
        return self.title


class Project(models.Model):
    """Modello per i progetti realizzati"""
    title = models.CharField(max_length=200, verbose_name="Titolo")
    description = models.TextField(verbose_name="Descrizione")
    client = models.CharField(max_length=200, blank=True, verbose_name="Cliente")
    technologies = models.CharField(max_length=500, blank=True, verbose_name="Tecnologie")
    category = models.CharField(max_length=100, blank=True, verbose_name="Categoria")
    url = models.URLField(blank=True, verbose_name="URL")
    image = models.ImageField(upload_to='projects/', blank=True, verbose_name="Immagine")
    is_featured = models.BooleanField(default=False, verbose_name="In evidenza")
    is_active = models.BooleanField(default=True, verbose_name="Attivo")
    completed_date = models.DateField(blank=True, null=True, verbose_name="Data completamento")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-completed_date', '-created_at']
        verbose_name = "Progetto"
        verbose_name_plural = "Progetti"

    def __str__(self):
        return self.title


class Contact(models.Model):
    """Modello per le richieste di contatto"""
    name = models.CharField(max_length=200, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    company = models.CharField(max_length=200, blank=True, verbose_name="Azienda")
    subject = models.CharField(max_length=300, verbose_name="Oggetto")
    message = models.TextField(verbose_name="Messaggio")
    is_read = models.BooleanField(default=False, verbose_name="Letto")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contatto"
        verbose_name_plural = "Contatti"

    def __str__(self):
        return f"{self.name} - {self.subject}"


class SiteSettings(models.Model):
    """Modello per le impostazioni del sito"""
    site_title = models.CharField(max_length=200, default="Mumble", verbose_name="Titolo sito")
    hero_title = models.CharField(max_length=500, default="Soluzioni software su misura.\nProcessi automatizzati.\nBusiness accelerato.", verbose_name="Titolo hero")
    hero_subtitle = models.TextField(default="Sviluppiamo piattaforme web che semplificano il lavoro e fanno crescere le aziende.", verbose_name="Sottotitolo hero")
    hero_description = models.TextField(default="Dalla progettazione allo sviluppo, creiamo soluzioni digitali che trasformano le sfide quotidiane in opportunità di crescita per il tuo business.", verbose_name="Descrizione hero")
    contact_email = models.EmailField(default="info@mumble.group", verbose_name="Email contatto")
    contact_phone = models.CharField(max_length=50, blank=True, verbose_name="Telefono")
    is_active = models.BooleanField(default=True, verbose_name="Attivo")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Impostazioni sito"
        verbose_name_plural = "Impostazioni sito"

    def __str__(self):
        return self.site_title

    def save(self, *args, **kwargs):
        # Assicuriamoci che ci sia solo un'istanza di SiteSettings
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError('Può esistere solo un\'istanza di SiteSettings')
        return super().save(*args, **kwargs)
