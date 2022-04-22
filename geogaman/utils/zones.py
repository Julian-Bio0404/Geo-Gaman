"""Zones utils."""

# Django
from django.contrib.gis.geos import Point

# Models
from geogaman.zones.models import Zone


def get_zones(latitude: str, longitude: str) -> list[Zone]:
    """Return zones from a geolocation (lat, lng)."""
    point = Point(float(longitude), float(latitude))
    zones = Zone.objects.filter(
        mpoly__intersects=point).order_by('-level')
    return zones
