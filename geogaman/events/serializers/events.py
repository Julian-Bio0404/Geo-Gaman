"""Events serializers."""

# Utilities
from datetime import date

# Django REST Framework
from rest_framework import serializers

# Models
from geogaman.events.models import SportEvent


class SportEventModelSerializer(serializers.ModelSerializer):
    """SportEvent model serializer."""

    start = serializers.DateField()
    finish = serializers.DateField()

    class Meta:
        """Meta options."""
        model = SportEvent
        fields = [
            'pk', 'title',
            'description',
            'start', 'finish',
            'geolocation', 'country',
            'state', 'city', 'place',
            'created', 'updated'
        ]

        read_only_fields = [
            'geolocation', 'country',
            'state', 'city',
            'created', 'updated'
        ]

    def validate(self, data):
        """Check that the start date is before the end date"""
        today = date.today()
        if data['start'] < today or data['finish'] < today:
            raise serializers.ValidationError(
                'The dates be must after that current date.')

        if data['start'] > data['finish']:
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
