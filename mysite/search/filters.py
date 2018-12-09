from django import forms
from django.contrib.auth.models import User, Group

import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    type__name = django_filters.CharFilter(lookup_expr='icontains')
    organic = django_filters.BooleanFilter()

    class Meta:
        model = Product
        fields = ['type__name', 'organic']
