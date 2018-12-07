from django.test import TestCase

from .models import *


class locationTestCase(TestCase):
    def test_zero_distance_calc(self):
        nearbySeller = Seller(brand="Maxi", address="3400 Linton, Cote des neiges")
        nearbySeller.save()
        dist = nearbySeller.distance_to(45.501678, -73.629755)
        self.assertAlmostEqual(dist, 0, places=1)

    def test_far_distance_calc(self):
        nearbySeller = Seller(brand="Maxi", address="3400 Linton, Cote des neiges")
        nearbySeller.save()
        dist = nearbySeller.distance_to(45.514168, -73.618198)
        self.assertAlmostEqual(dist, 1.632, places=2)
