# weather_app/views.py

import requests
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import Favorite
import os


def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def get_weather_data(city):
    api_key = os.getenv('API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.RequestException as e:
        return {'error': str(e)}

def weather(request):
    city = request.GET.get('city', 'London')  # Default to London
    data = get_weather_data(city)
    return JsonResponse(data)

def get_forecast_data(city):
    api_key = os.getenv('API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def forecast(request):
    city = request.GET.get('city', 'London')
    data = get_forecast_data(city)
    return JsonResponse(data)

def add_favorite(request):
    user = request.user
    if user.is_authenticated and request.method == "POST":
        city = request.POST.get('city')
        Favorite.objects.create(user=user, city=city)
        return JsonResponse({'status': 'success', 'city': city})
    return JsonResponse({'status': 'error', 'message': 'User not authenticated or incorrect request method'})

def remove_favorite(request):
    user = request.user
    if user.is_authenticated and request.method == "POST":
        city = request.POST.get('city')
        Favorite.objects.filter(user=user, city=city).delete()
        return JsonResponse({'status': 'success', 'city': city})
    return JsonResponse({'status': 'error', 'message': 'User not authenticated or incorrect request method'})
def index(request):
    return render(request, 'index.html')