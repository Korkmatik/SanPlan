from .models import Veranstaltung


class VeranstaltungController():

    @staticmethod
    def get_veranstaltungen():
        return Veranstaltung.objects.all()

    @staticmethod
    def get_veranstaltung_by_id(id):
        return Veranstaltung.objects.get(id=id)

    @staticmethod
    def get_adresse_by_veranstaltung_id(id):
        return Veranstaltung.objects.get(id=id).get_adresse()
