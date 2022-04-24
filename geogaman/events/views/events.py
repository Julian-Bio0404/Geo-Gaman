"""Sport Event views."""

# Django REST Framework
from rest_framework import viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from rest_framework.permissions import AllowAny

# Models
from geogaman.events.models import SportEvent

# Serializers
from geogaman.events.serializers import SportEventModelSerializer


class SportEventViewSet(viewsets.ModelViewSet):
    """
    Sport Event Viewset.
    Handle create, retrieve, list, update and destroy
    a sport event.
    """

    queryset = SportEvent.objects.all()
    serializer_class = SportEventModelSerializer
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('country', 'state', 'city')
    ordering_fields = ('start',)
    ordering = ('start',)
    filter_fields = ('country', 'state', 'city')
