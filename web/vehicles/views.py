from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Vehicle
from .controllers import VehicleController, VehicleTypeController


class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        vehicles = Vehicle.objects.all()

        return render(
            request,
            'vehicles/index.html',
            context={
                'vehicles': vehicles,
                'vehicleActive': True,
            }
        )


class CreateView(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'vehicle_types': VehicleTypeController.get_all_vehicle_types(),
            'states': VehicleController.get_vehicle_states(),
            'vehicleActive': True,
        }

        return render(
            request,
            'vehicles/create.html',
            context
        )


class CreateVehicleTypeView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'vehicle_type/create.html')
