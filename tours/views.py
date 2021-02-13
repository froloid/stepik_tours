from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.


def main_view(request):
    return render(request, 'index.html')


def departure_view(request):
    return render(request, 'departure.html')


def tour_view(request):
    return render(request, 'tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что-то сломалось... Простите, извините!')


def custom_handler500(request):
    return HttpResponseNotFound('Ой, что-то сломалось... Простите, извините!')
