from django.shortcuts import render
from django.views import View

from .models import Vehicle
from .controllers import VehicleController, VehicleTypeController


class IndexView(View):

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


class CreateView(View):

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
