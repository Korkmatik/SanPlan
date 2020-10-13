from django.shortcuts import render
from django.views import View

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
                'fahrzeugeActive': True,
            }
        )


class CreateView(View):

    def get(self, request):
        context = {
            'vehicle_types': VehicleTypeController.get_all_vehicle_types(),
            'states': VehicleController.get_vehicle_states(),
        }

        return render(
            request,
            'fahrzeuge/create.html',
            context
        )