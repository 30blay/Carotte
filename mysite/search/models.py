from __future__ import unicode_literals
from geopy.geocoders import Nominatim
from geopy import distance
from djgeojson.fields import PointField


from django.db import models


class Specie(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    brand = models.CharField(max_length=30)
    address = models.CharField(max_length=200, null=True)
    geom = PointField(null=True)

    class Meta:
        unique_together = (("brand", "geom"),)

    def __str__(self):
        return self.brand

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.address:
            self.geocode()
        super(Seller, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def geocode(self):
        geolocator = Nominatim()
        location = geolocator.geocode(self.address)
        self.geom = {'type': 'Point', 'coordinates': [location.latitude, location.longitude]}

    def get_distance(self, latitude, longitude):
        return distance.distance(self.geom['coordinates'], (latitude, longitude)).km


class Product(models.Model):
    type = models.ForeignKey(Specie, on_delete=models.CASCADE, null=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=False)
    organic = models.BooleanField(default=False)
    numSold = models.IntegerField(default=0)

    def __str__(self):
        return self.type.name + " at " + self.seller.brand

    class Meta:
        # unique constraint : only one potato at a certain seller
        unique_together = (("type", "seller"),)

