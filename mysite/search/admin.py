from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Product, Seller, Specie

admin.site.register(Product)
admin.site.register(Specie)


@admin.register(Seller)
class HeroAdmin(admin.ModelAdmin):
    readonly_fields = ["geom"]
