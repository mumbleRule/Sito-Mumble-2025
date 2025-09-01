from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('api/services/', views.ServiceListView.as_view(), name='service-list'),
    path('api/projects/', views.ProjectListView.as_view(), name='project-list'),
    path('api/projects/featured/', views.FeaturedProjectListView.as_view(), name='featured-projects'),
    path('api/contact/', views.ContactCreateView.as_view(), name='contact-create'),
    path('api/settings/', views.site_settings_view, name='site-settings'),
]
