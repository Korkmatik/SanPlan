from django.db import models

from veranstaltung.models import Veranstaltung


class EVTUnit(models.Model):
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