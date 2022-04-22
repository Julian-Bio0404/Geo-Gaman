"""Zones serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from geogaman.zones.models import Zone


class ZoneModelSerializer(serializers.ModelSerializer):
    """Zone model serializer."""

    type = serializers.CharField(source='get_order')

    class Meta:
        """Meta options."""
        model = Zone
        fields = [
            'pk', 'name',
            'codename',
            'lng', 'lat'
        ]

        read_only_fields = [
            'pk', 'name',
            'codename',
            'lng', 'lat'
        ]
