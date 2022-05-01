"""Zones serializers."""

# Django
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers

# Models
from geogaman.zones.models import Zone

# Utils
from geogaman.utils.zones import get_zones 


class ZoneModelSerializer(serializers.ModelSerializer):
    """Zone model serializer."""

    type = serializers.CharField(source='get_order')

    class Meta:
        """Meta options."""
        model = Zone
        fields = [
            'pk', 'name', 'codename',
            'type', 'lat','lng'
        ]


class SearchZoneEventsSerializer(serializers.Serializer):
    """Util to search events ids by zone."""

    regex = RegexValidator(
        regex=r'^\-?\d{0,3}.?\d{1,9}',
        message='Geolocation format is invalid.')

    lat = serializers.CharField(validators=[regex])
    lng = serializers.CharField(validators=[regex])

    def validate(self, data):
        """Check zones."""
        zones = get_zones(data['lat'], data['lng'])
        if not zones:
            raise serializers.ValidationError('No zones found.')
        return zones
