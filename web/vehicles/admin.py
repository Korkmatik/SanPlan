from django.contrib import admin

from .models import Fahrzeug, VehicleType


admin.site.register(Fahrzeug)
admin.site.register(VehicleType)
