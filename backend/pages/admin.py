from django.contrib import admin
from .models import Service, Project, Contact, SiteSettings


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'is_featured', 'is_active', 'completed_date']
    list_filter = ['is_featured', 'is_active', 'completed_date', 'created_at']
    search_fields = ['title', 'description', 'client', 'technologies']
    list_editable = ['is_featured', 'is_active']
    ordering = ['-completed_date', '-created_at']
    date_hierarchy = 'completed_date'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'company']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'

    def has_add_permission(self, request):
        # Non permettiamo di aggiungere contatti dall'admin
        return False


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_title', 'is_active', 'updated_at']
    fieldsets = (
        ('Informazioni generali', {
            'fields': ('site_title', 'is_active')
        }),
        ('Sezione Hero', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_description')
        }),
        ('Contatti', {
            'fields': ('contact_email', 'contact_phone')
        }),
    )

    def has_add_permission(self, request):
        # Permettiamo solo una istanza di SiteSettings
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Non permettiamo di cancellare le impostazioni
        return False
