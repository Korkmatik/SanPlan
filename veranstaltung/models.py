from django.conf import settings
from django.db import models
from django.urls import reverse


class Adresse(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    strasse = models.CharField(max_length=50)
    strassenNummer = models.CharField(max_length=20)
    plz = models.CharField(max_length=20)
    ort = models.CharField(max_length=50)

    def get_name(self):
        return self.name

    def get_strasse(self):
        return str(self.strasse) + " " + str(self.strassenNummer)

    def get_ort(self):
        return str(self.plz) + " " + str(self.ort)

    def has_name(self):
        return (self.name != None) and (self.name != "")

    def get_google_maps_link_for_strasse(self):
        return "http://maps.google.com/maps?q={}, {}".format(self.get_strasse(), self.get_ort())

    def get_google_maps_link_for_ort(self):
        return "http://maps.google.com/maps?q={}".format(self.get_ort())

    def __str__(self):
        return self.name


class Veranstaltung(models.Model):
    adresse = models.ForeignKey(Adresse, null=True, on_delete=models.SET_NULL)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    vonDateTime = models.DateTimeField()
    bisDateTime = models.DateTimeField()
    titel = models.CharField(max_length=80)
    ansprechPartner = models.CharField(max_length=80, null=True, blank=True)

    def get_von_deutsch(self):
        return self.__to_german(self.vonDateTime.strftime("%a, %d. %b %Y %H:%M"))

    def get_bis_deutsch(self):
        return self.__to_german(self.bisDateTime.strftime("%a, %d. %b %Y %H:%M"))

    def __to_german(self, string):
        return string\
            .replace("Tue", "Dienstag")\
            .replace("Wed", "Mittwoch")\
            .replace("Thu", "Donnerstag")\
            .replace("Sep", "September")

    def get_titel(self):
        return self.titel

    def get_von_date_time(self):
        return self.vonDateTime

    def get_bis_date_time(self):
        return self.bisDateTime

    def get_date(self):
        return self.__to_german(self.vonDateTime.strftime("%d. %b %Y"))

    def get_adresse(self):
        return self.adresse

    def get_absolute_url(self):
        return reverse('veranstaltung:detail', args=[str(self.id)])

    def hat_einheiten(self):
        return (self.get_anzahl_evts() > 0)

    def has_ansprechpartner(self):
        return self.ansprechPartner != None and self.ansprechPartner != ""

    def get_evts(self):
        return EVTEinheit.objects.filter(veranstaltung_id=self.id)

    def get_anzahl_evts(self):
        return self.get_evts().count()

    def get_ansprechpartner(self):
        return self.ansprechPartner

    def __str__(self):
        return self.titel

    
class Qualifikation(models.Model):
    titel = models.CharField(max_length=20)
    kuerzel = models.CharField(max_length=10)

    def __str__(self):
        return self.titel


class EVTEinheit(models.Model):
    veranstaltung = models.ForeignKey(Veranstaltung, on_delete=models.CASCADE)

    truppFuehrer = models.CharField(max_length=80)
    personal = models.CharField(max_length=80)
    praktikant = models.CharField(max_length=80, blank=True, null=True)

    standort = models.CharField(max_length=200)

    zusatzinformation = models.CharField(max_length=300, blank=True, default="")

    def get_trupp_fuhrer(self):
        return self.truppFuehrer

    def get_personal(self):
        return self.personal

    def get_praktikant(self):
        return self.praktikant

    def get_standort(self):
        return self.standort

    def get_zusatzinformation(self):
        return self.zusatzinformation

    def has_zusatzinformation(self):
        return self.zusatzinformation != ""

    def has_praktikant(self):
        return self.praktikant != None

    def __str__(self):
        return self.truppFuehrer

