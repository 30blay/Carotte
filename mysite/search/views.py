from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from .models import Seller
from .utils import get_client_ip


def maxdist(request, max_dist_km='2'):
    max_dist_km = float(max_dist_km)
    product_list = Product.objects.all()
    output = ""
    closest_products_list = []
    for p in product_list:
        distance = p.seller.get_distance(45.501691, -73.629705)
        if distance < max_dist_km:
            output += ' '.join([p.type.name + " at " + p.seller.brand + ", "])
            closest_products_list.append(p)

    context = {'closest_products_list': closest_products_list}
    return render(request, 'search/maxdist.html', context)
