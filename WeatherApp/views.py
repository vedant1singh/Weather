import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ba96862d748795532db1d91f4fd375ef'

    if request.method =="POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
        "city" : city.name,
        "temperature" : r["main"]['temp'],
        "description" : r['weather'][0]['description'] ,
        "icon" : r["weather"][0]['icon'],
        }
        weather_data.append(city_weather)

    context ={'weather_data' : weather_data, "form" : form}

    return render(request, "home.html", context)