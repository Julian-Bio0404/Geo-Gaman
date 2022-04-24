"""Events serializers."""

# Utilities
from datetime import date

# Django REST Framework
from rest_framework import serializers

# Models
from geogaman.events.models import SportEvent

# Serializers
from geogaman.zones.serializers import ZoneModelSerializer

# Utils
from geogaman.utils.zones import get_zones


class SportEventModelSerializer(serializers.ModelSerializer):
    """SportEvent model serializer."""

    start = serializers.DateField()
    finish = serializers.DateField()
    zone = ZoneModelSerializer(read_only=True)

    class Meta:
        """Meta options."""
        model = SportEvent
        fields = [
            'pk', 'title',
            'description',
            'start', 'finish',
            'zone', 'geolocation',
            'country', 'state',
            'city', 'place',
            'created', 'updated'
        ]

    def validate(self, data):
        """Check that the start date is before the end date"""
        start = data.get('start', None)
        finish = data.get('finish', None)
        today = date.today()

        if start and (start < today) or (finish < today):
                raise serializers.ValidationError(
                    'The dates be must after that current date.')
        if finish and (start > finish):
                raise serializers.ValidationError(
                    'The start date be must before that finish date.')
        return data

    def update(self, instance, data):
        """Update Sport Event and verify the news dates."""
        start = data.get('start', None)
        finish = data.get('finish', None)

        if start and (start > instance.finish and not finish):
            raise serializers.ValidationError(
                'The start date be must after that finish date.')

        if finish and (finish < instance.start and not start):
            raise serializers.ValidationError(
                'The finish date be must after that start date.')

        if start and finish and (start > finish):
            raise serializers.ValidationError(
                'The start date be must before that finish date.')
        return super().update(instance, data)
    
    def create(self, data):
        """Create an event and get zone from provided lat, lng."""
        geolocation = str(data['geolocation']).split()
        zone = get_zones(geolocation[0], geolocation[1])
        data['zone'] = zone[0]
        return super().create(data)
