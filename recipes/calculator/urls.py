from django.urls import path

from .views import index

urlpatterns = [
    path('<recipe>/', index, name='recipe'),
    # path('bus_stations/', bus_stations, name='bus_stations'),
]