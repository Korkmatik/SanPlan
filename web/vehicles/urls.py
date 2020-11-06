from django.urls import path

from . import views

app_name = 'vehicles'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create', views.CreateView.as_view(), name='create'),
    path('vehicle_type/create', views.CreateVehicleTypeView.as_view(), name='create_vehicle_type')
]
