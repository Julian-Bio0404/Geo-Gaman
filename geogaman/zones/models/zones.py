"""Zones models."""

# Django
from django.contrib.gis.db import models

# MPTT
from mptt.models import MPTTModel, TreeForeignKey


class Zone(MPTTModel):
    """Zone model."""

    ORDERS = [
        (1, 'Country'),
        (2, 'State'),
        (3, 'City'),
        (4, 'Place'),
    ]

    name = models.CharField(max_length=100)
    codename = models.SlugField(unique=True)
    order = models.IntegerField(choices=ORDERS)
    mpoly = models.MultiPolygonField(null=True, blank=True)

    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    zones = models.ManyToManyField('self', blank=True)
    lng = models.FloatField()
    lat = models.FloatField()

    class MPTTMeta:
        """Meta options."""
        order_insertion_by = ['name']

    def get_order(self) -> str:
        """Return order name."""
        return self.ORDERS[self.order][1]

    def __str__(self) -> str:
        """Return order and name in str."""
        return f'{self.get_order()}: {self.name}'