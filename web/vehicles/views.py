from django.shortcuts import render
from django.views import View
from django.http import Http404
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


class UpdateView(LoginRequiredMixin, View):

    def get(self, request, id):
        if not request.user.is_superuser:
            raise Http404()

        vehicle = VehicleController.get_vehicle_by_id_or_404(id)

        return render(
            request,
            'vehicles/update.html',
            {
                'vehicle': vehicle,
                'vehicle_types': VehicleTypeController.get_all_vehicle_types(),
                'states': VehicleController.get_vehicle_states(),
            }
        )

    def post(self, request, id):
        pass


class CreateVehicleTypeView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'vehicle_type/create.html')
