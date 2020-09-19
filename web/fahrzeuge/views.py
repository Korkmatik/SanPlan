from django.shortcuts import render
from django.views import View

from .models import Fahrzeug


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