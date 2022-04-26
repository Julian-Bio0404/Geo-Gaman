"""Users commands."""

# Utilities
import pandas as pd

# Django
from django.core.management.base import BaseCommand

# Models
from geogaman.zones.models import Zone


class Command(BaseCommand):
    """Zone command."""

    help = 'Upload zones csv to database'

    def handle(self, *args, **options):
        data = pd.DataFrame(
            pd.read_csv('./datasource/countries.csv'),
            columns=[
                'WKT', 'ISO3', 'NAME', 'LON', 'LAT'
            ]
        )

        for zone in data.itertuples():
            # mpoly = 146, poly = 100
            try:
                Zone.objects.create(
                    name=zone.NAME,
                    codename=zone.ISO3,
                    order=1,
                    poly=zone.WKT,
                    lng=zone.LON,
                    lat=zone.LAT
                )
            except TypeError:
                Zone.objects.create(
                    name=zone.NAME,
                    codename=zone.ISO3,
                    order=1,
                    mpoly=zone.WKT,
                    lng=zone.LON,
                    lat=zone.LAT
                )

        self.stdout.write(
            self.style.SUCCESS('Zones created successfully.'))
