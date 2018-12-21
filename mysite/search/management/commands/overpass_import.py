import overpy
from django.core.management.base import BaseCommand
from mysite.search.models import Seller


class Command(BaseCommand):
    def handle(self, *args, **options):
        boundingBox = '(45.22364447346731,-74.20440673828125,45.80678584211672,-73.1744384765625)'
        api = overpy.Overpass()
        result = api.query("""node["shop"="supermarket"]""" + boundingBox + """;out body;""")

        for shop in result.get_nodes():
            if 'name' not in shop.tags:
                continue
            name = shop.tags['name']
            latitude = shop.lat
            longitude = shop.lon
            seller = Seller(brand=name, geom={'type': 'Point', 'coordinates': [latitude, longitude]})
            seller.save()
