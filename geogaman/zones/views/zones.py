"""Zone views."""

# Django REST Framework
from rest_framework import mixins,  status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from rest_framework.permissions import AllowAny

# Models
from geogaman.zones.models import Zone

# Serializers
from geogaman.zones.serializers import (ZoneModelSerializer,
                                        SearchZoneEventsSerializer)


class ZoneViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    Zone ViewSet.
    Handle retrieve and list zones
    """

    queryset = Zone.objects.all()
    serializer_class = ZoneModelSerializer
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('order', 'lng', 'lat')
    filter_fields = ('order',)

    @action(detail=False, methods=['post'])
    def events(self, request):
        """Get events ids of a zone."""
        serializer = SearchZoneEventsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        zone = serializer.validated_data
        data = {'events_ids': zone.events_ids}
        return Response(data, status=status.HTTP_200_OK)
