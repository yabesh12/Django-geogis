from django.contrib.gis import admin

from v1.models import Place

class LocationAdmin(admin.OSMGeoAdmin):
    # default_zoom = 5
    default_zoom = 5
    default_extent = (76.735611, 9.152967, 76.735611, 9.152967)

# Register your models here.
admin.site.register(Place, LocationAdmin)