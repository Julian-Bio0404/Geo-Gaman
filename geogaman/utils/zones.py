"""Zones utils."""

# Django
from django.contrib.gis.geos import Point
from django.db.models import Q

# Models
from geogaman.zones.models import Zone


def get_zones(latitude: str, longitude: str) -> list[Zone]:
    """Return zones from a geolocation (lat, lng)."""
    point = Point(float(latitude), float(longitude))
    zones = Zone.objects.filter(
        Q(mpoly__intersects=point) |
        Q(poly__intersects=point)).order_by('-level')
    return zones
