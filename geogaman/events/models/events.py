"""Event models."""

# Django
from django.db import models

# Utils
from geogaman.utils.models import GeoGamanModel


class SportEvent(GeoGamanModel):
    """
    Sport Event model.
    This model stores sport events.
    """

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250, blank=True)

    start = models.DateField(
        help_text='sport event start date', auto_now=False, auto_now_add=False)

    finish = models.DateField(
        help_text='sport event finish date', auto_now=False, auto_now_add=False)

    # ubication
    geolocation = models.CharField(max_length=33)
    country = models.CharField(max_length=70)
    state = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    place = models.CharField(max_length=180)

    def __str__(self):
        """Return Event title."""
        return self.title
