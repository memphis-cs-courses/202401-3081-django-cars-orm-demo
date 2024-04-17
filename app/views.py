from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Car


# Create your views here.
def cars_list(request):
    cars = Car.objects.all()
    return render(request, "cars/index.html", {"cars": cars})


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, "cars/show.html", {"car": car})
