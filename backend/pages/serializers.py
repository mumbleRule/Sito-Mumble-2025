from rest_framework import serializers
from .models import Service, Project, Contact, SiteSettings


class ServiceSerializer(serializers.ModelSerializer):
    """Serializer per i servizi"""

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'subtitle', 'order']


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer per i progetti"""

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'client', 'technologies', 'category',
            'url', 'image', 'is_featured', 'completed_date'
        ]


class ContactSerializer(serializers.ModelSerializer):
    """Serializer per i contatti"""

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'company', 'subject', 'message']

    def create(self, validated_data):
        """Crea un nuovo contatto"""
        return Contact.objects.create(**validated_data)


class SiteSettingsSerializer(serializers.ModelSerializer):
    """Serializer per le impostazioni del sito"""

    class Meta:
        model = SiteSettings
        fields = [
            'id', 'site_title', 'hero_title', 'hero_subtitle',
            'hero_description', 'contact_email', 'contact_phone'
        ]
