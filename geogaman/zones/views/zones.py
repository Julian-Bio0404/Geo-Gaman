"""Zone views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from rest_framework.permissions import IsAuthenticated

# Models
from geogaman.zones.models import Zone

# Serializers
from geogaman.zones.serializers import ZoneModelSerializer


class ZoneViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Zone ViewSet.
    Handle retrieve and list zones
    """

    queryset = Zone.objects.all()
    serializer_class = ZoneModelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('order', 'lng', 'lat')
    filter_fields = ('order',)
