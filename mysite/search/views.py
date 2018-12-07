from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from .models import Seller
from .utils import get_client_ip


def index(request):
    product_list = Product.objects.all()
    output = ""
    for p in product_list:
        distance = p.seller.get_distance(45.501691, -73.629705)
        if distance < 2:
            output += ' '.join([p.type.name + " at " + p.seller.brand + ", "])

    return HttpResponse(output)
