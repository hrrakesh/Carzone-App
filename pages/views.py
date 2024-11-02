from django.http import HttpResponse
from django.shortcuts import render
from .models import Team
from cars.models import Car, Car_at_top

def home(request):
    teams = Team.objects.all()
    featured_car = Car.objects.filter(is_featured=True).order_by('-created_at')
    car_top = Car_at_top.objects.all()

    # Fetch distinct values and order them in ascending order
    model_search = Car.objects.values_list('model', flat=True).distinct().order_by('model')
    city_search = Car.objects.values_list('city', flat=True).distinct().order_by('city')
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct().order_by('body_style')

    show_all_cars = False
    
    # Determine whether to show all cars or only non-featured ones
    if show_all_cars: 
        all_car = Car.objects.all()
    else:
        all_car = Car.objects.filter(is_featured=False)

    data = {
        'teams': teams,
        'featured_car': featured_car,
        'all_car': all_car,
        'car_top': car_top,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }

    return render(request, 'pages/home.html', data)



def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html',data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')