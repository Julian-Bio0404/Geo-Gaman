"""Zones URLs"""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from geogaman.zones.views import ZoneViewSet


router = DefaultRouter()
router.register(r'zones', ZoneViewSet, basename='zones')

urlpatterns = [path('', include(router.urls))]
