from django.contrib import admin

from .models import Fahrzeug, FahrzeugTyp


admin.site.register(Fahrzeug)
admin.site.register(FahrzeugTyp)
