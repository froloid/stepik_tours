import random

from django.shortcuts import render
from django.http import HttpResponseNotFound

from tours.data import tours, departures

# Create your views here.


def main_view(request):
    rand_list = list(tours.keys())
    random.shuffle(rand_list)
    rand_tours = {i: tours[i] for i in rand_list[:6]}
    return render(request, 'index.html', {'tours': rand_tours, 'departures': departures})


def departure_view(request, dep_id):
    dep_tours = {}
    for k, v in tours.items():
        if v['departure'] == dep_id:
            dep_tours[k] = v

    return render(request, 'departure.html',
                  {'tours': dep_tours,
                   'departures': departures,
                   'from': departures[dep_id]
                   })


def tour_view(request, tour_id):
    return render(request, 'tour.html',
                  {'tour': tours[tour_id],
                   'departures': departures,
                   'from': departures[tours[tour_id]['departure']]
                   })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что-то сломалось... Простите, извините!')


def custom_handler500(request):
    return HttpResponseNotFound('Ой, что-то сломалось... Простите, извините!')
