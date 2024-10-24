import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(BUS_STATION_CSV, mode ='r', encoding="UTF-8") as file:
        csvFile = csv.DictReader(file)
        #bus_stations = []
        bus_stations = [line for line in csvFile]
        #for lines in csvFile:
        #    bus_stations.append(lines)
    #print(bus_stations)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 25)

    page = paginator.get_page(page_number)
    context = {
         'bus_stations': page.object_list,
         'page': page
    }

    return render(request, 'stations/index.html', context)
