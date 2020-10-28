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
        return str(self.strasse)

    def get_ort(self):
        return str(self.ort)

    def has_name(self):
        return (self.name is not None) and (self.name != "")

    def get_google_maps_link_for_strasse(self):
        return "http://maps.google.com/maps?q={}, {}".format(self.get_strasse(), self.get_ort())

    def get_google_maps_link_for_ort(self):
        return "http://maps.google.com/maps?q={}".format(self.get_ort())

    def __str__(self):
        return self.name


class Veranstaltung(models.Model):
    address = models.ForeignKey(Adresse, null=True, on_delete=models.SET_NULL)

    vonDateTime = models.DateTimeField()
    bisDateTime = models.DateTimeField()
    titel = models.CharField(max_length=80)
    ansprechPartner = models.CharField(max_length=80, null=True, blank=True)

    def get_titel(self):
        return self.titel

    def get_von_date_time(self):
        return self.vonDateTime

    def get_bis_date_time(self):
        return self.bisDateTime

    def get_date(self):
        return self.vonDateTime.strftime("%d. %b %Y")

    def get_adresse(self):
        return self.address

    def get_edit_url(self):
        return reverse('veranstaltung:detail', args=[ str(self.id), ])

    def has_ansprechpartner(self):
        return self.ansprechPartner is not None and self.ansprechPartner != ""

    def get_ansprechpartner(self):
        return self.ansprechPartner

    def __str__(self):
        return self.titel
