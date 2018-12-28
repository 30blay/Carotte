from django.shortcuts import render
from django.http import HttpResponse
import json
from django.utils.html import escapejs
from django.utils.html import mark_safe

from .models import Product
from .filters import ProductFilter


def maxdist(request, max_dist_km='2'):
    max_dist_km = float(max_dist_km)
    products = Product.objects.all()

    pfilter = ProductFilter(request.GET, queryset=products)

    map_products = [{'loc': [float(product.seller.geom['coordinates'][0]), float(product.seller.geom['coordinates'][1])],
                     'name': product.type.name,
                     'seller': product.seller.brand,
                     } for product in pfilter.qs]

    output = ""
    closest_products_list = []
    for p in products:
        distance = p.seller.get_distance(45.501691, -73.629705)
        if distance < max_dist_km:
            output += ' '.join([p.type.name + " at " + p.seller.brand + ", "])
            closest_products_list.append(p)

    context = {'closest_products_list': closest_products_list,
               'filter': pfilter,
               'map_products': mark_safe(escapejs(json.dumps(map_products))),
               }
    return render(request, 'search/maxdist.html', context)
