from django import forms
from django.contrib.auth.models import User, Group

import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    type__name = django_filters.CharFilter(lookup_expr='icontains')
    seller__brand = django_filters.CharFilter(lookup_expr='icontains')
    #year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    #groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ['type__name', 'seller__brand']
