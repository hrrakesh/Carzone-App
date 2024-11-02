from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Car
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def cars(request):
    cars = Car.objects.filter(for_rented=True)

    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    # Fetch distinct values and order them in ascending order
    model_search = Car.objects.values_list('model', flat=True).distinct().order_by('model')
    city_search = Car.objects.values_list('city', flat=True).distinct().order_by('city')
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct().order_by('body_style')

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)



def car_details(request,id):


    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }

    return render(request,'cars/car-details.html', data)

@login_required(login_url='login')  # Redirects to login page if user is not authenticated
def search(request):
    car_search_need_to_be_display_in_the_page = False
    cars = Car.objects.all()

    # Apply filters if they exist in request.GET
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(car_title__icontains=keyword)

            
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if min_price and max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    # Set up pagination after filtering
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    # Prepare unique and ordered data for dropdowns
    model_search = Car.objects.values_list('model', flat=True).distinct().order_by('model')
    city_search = Car.objects.values_list('city', flat=True).distinct().order_by('city')
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct().order_by('body_style')
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct().order_by('transmission')

    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
        'cars_search_want': car_search_need_to_be_display_in_the_page
    }

    return render(request, 'cars/search.html', data)
