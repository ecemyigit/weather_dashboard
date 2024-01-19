# weather_app/urls.py

from django.urls import path
from .views import weather, index, forecast, logout_view
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('weather/', weather, name='weather'),
    path('forecast/', forecast, name='forecast'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/', views.remove_favorite, name='remove_favorite'),

]
