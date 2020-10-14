from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Fahrzeug
from .controllers import VehicleController, VehicleTypeController


class IndexView(View):

    def get(self, request):
        fahrzeuge = Fahrzeug.objects.all()

        return render(
            request,
            'fahrzeuge/index.html',
            context={
                'fahrzeuge': fahrzeuge,
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
            'fahrzeuge/create.html',
            context
        )