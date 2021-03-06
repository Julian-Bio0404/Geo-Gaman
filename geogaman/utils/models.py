"""GeoGaman models utils."""

# Django
from django.db import models


class BaseGeoGamanModel(models.Model):
    """
    Base GeoGaman Model.
    BaseGeoGamanModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following atribute:
        + created (DateTime): Store the datetime the object was created.
    """

    created = models.DateTimeField(
        'created at', auto_now_add=True,
        help_text='Date time on which the was created.')

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created']


class GeoGamanModel(BaseGeoGamanModel):
    """
    GeoGaman Model.
    GeoGamanModel acts as an abstract base class inherits from
    BaseGeoGamanModel. Extend your models of this class to add 
    the following field:
        + updated (DateTime): Store the datetime the object was updated.
    """

    updated = models.DateTimeField(
        'updated at', auto_now=True,
        help_text='Date time on which the was updated.')

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-updated']
