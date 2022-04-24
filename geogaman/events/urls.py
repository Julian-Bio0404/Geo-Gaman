"""Events URLs"""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from geogaman.events.views import SportEventViewSet


router = DefaultRouter()
router.register(r'events', SportEventViewSet, basename='events')

urlpatterns = [path('', include(router.urls))]
