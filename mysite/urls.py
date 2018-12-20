from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django_filters.views import FilterView

from djgeojson.views import GeoJSONLayerView

from .search.filters import ProductFilter
from .search.views import maxdist
from .search.models import Seller


urlpatterns = [
    url(r'^maxdist/(\d+(?:\.\d+))/$', maxdist, name='maxdist'),
    url(r'^maxdist/$', maxdist, name='maxdist'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^search/$', FilterView.as_view(filterset_class=ProductFilter, template_name='search/user_list.html'), name='search'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Seller), name='sellerData'),
]
