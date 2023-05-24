from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for info in reader:
            one_station = {'Name' : info['Name'],
                           'Street': info['Street'],
                           'District': info['District']}
            bus_stations.append(one_station)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 5)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
