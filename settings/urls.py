"""Geogaman URL Configuration."""

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(('geogaman.events.urls', 'events'), namespace='events')),
    path('', include(('geogaman.zones.urls', 'zones'), namespace='zones')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
