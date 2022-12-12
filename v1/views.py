from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

from v1.models import Place

# Create your views here.


def test(request):
    ref_location  = Point(76.735611,9.152967, srid=4326)
    print(ref_location)
    place_obj = Place.objects.filter(location__distance_lte=(ref_location, D(km=7)))
    for i in place_obj:
        print(i.name)
        print(i.location)
    return JsonResponse({'status': 'ok'})