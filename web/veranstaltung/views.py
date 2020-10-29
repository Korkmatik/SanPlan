from django.shortcuts import render
from django.views import View

from .controllers import VeranstaltungController


class IndexView(View):

    def get(self, request):
        return render(request,
                      'veranstaltung/index.html',
                      {
                          'veranstaltungen': VeranstaltungController.get_veranstaltungen(),
                          'home': True,
                      })


class VeranstaltungsView(View):

    def get(self, request, id):
        veranstaltung = VeranstaltungController.get_veranstaltung_by_id(id)
        return render(request,
                      'veranstaltung/detail.html',
                      {
                          'veranstaltung': veranstaltung,
                          'von': veranstaltung.get_von_date_time(),
                          'bis': veranstaltung.get_bis_date_time(),
                          'adresse': veranstaltung.get_adresse(),
                      })