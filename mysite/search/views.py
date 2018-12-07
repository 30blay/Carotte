from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from .models import Seller
from .utils import get_client_ip


def maxdist(request, max_dist_km='1'):
    max_dist_km = float(max_dist_km)
    product_list = Product.objects.all()
    output = ""
    for p in product_list:
        distance = p.seller.get_distance(45.501691, -73.629705)
        if distance < max_dist_km:
            output += ' '.join([p.type.name + " at " + p.seller.brand + ", "])

    return HttpResponse(output)
