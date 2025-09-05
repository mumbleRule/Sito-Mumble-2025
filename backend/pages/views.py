from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Service, Project, Contact, SiteSettings
from .serializers import ServiceSerializer, ProjectSerializer, ContactSerializer, SiteSettingsSerializer


class ServiceListView(generics.ListAPIView):
    """API per ottenere la lista dei servizi attivi"""
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class ProjectListView(generics.ListAPIView):
    """API per ottenere la lista dei progetti attivi"""
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer


class FeaturedProjectListView(generics.ListAPIView):
    """API per ottenere i progetti in evidenza"""
    queryset = Project.objects.filter(is_active=True, is_featured=True)
    serializer_class = ProjectSerializer


class ContactCreateView(generics.CreateAPIView):
    """API per creare una nuova richiesta di contatto"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Messaggio inviato con successo!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": "Errore nell'invio del messaggio", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def site_settings_view(request):
    """API per ottenere le impostazioni del sito"""
    try:
        settings = SiteSettings.objects.filter(is_active=True).first()
        if settings:
            serializer = SiteSettingsSerializer(settings)
            return Response(serializer.data)
        else:
            # Restituiamo valori di default se non ci sono impostazioni
            default_data = {
                "site_title": "Mumble",
                "hero_title": "Software su misura.\nZero compromessi.",
                "hero_subtitle": "Trasformiamo le tue idee in soluzioni digitali che funzionano.",
                "hero_description": "",
                "contact_email": "info@mumble.group",
                "contact_phone": ""
            }
            return Response(default_data)
    except Exception as e:
        return Response(
            {"error": "Errore nel recupero delle impostazioni"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
