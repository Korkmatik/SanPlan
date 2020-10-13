import os

from django.db import models


def fahrzeug_images(instance, filename):
    return os.path.join('vehicle', str(instance.id), filename)


class FahrzeugTyp(models.Model):

    short = models.CharField(max_length=5)
    name = models.CharField(max_length=30)


class Fahrzeug(models.Model):
    NICHT_VERFUEGBAR = "NV"
    VERFUEGBAR = "VB"
    WERKSTATT = "WS"
    IM_DIENST = "ID"
    STATUS_CHOICES = [
        (NICHT_VERFUEGBAR, 'Nicht verfügbar'),
        (VERFUEGBAR, 'Verfügbar'),
        (WERKSTATT, 'In der Werkstatt'),
        (IM_DIENST, 'Im Dienst'),
    ]

    typ = models.ForeignKey(FahrzeugTyp, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, blank=True, null=True)
    kennzeichen = models.CharField(max_length=15)
    funkrufname = models.CharField(max_length=30)
    image = models.ImageField(upload_to=fahrzeug_images, blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=VERFUEGBAR)
    seats = models.PositiveIntegerField()

    def get_name(self):
        return self.name

    def get_kennzeichen(self):
        return self.kennzeichen

    def get_funkrufname(self):
        return self.funkrufname

    def get_typ(self):
        return self.typ

    def get_file_path(self):
        return 'fahrzeug_pics/' + str(self.filename)

    def get_status(self):
        return self.status

    def has_name(self):
        return self.name

    def is_verfuegbar(self):
        return self.status == self.VERFUEGBAR

    def __str__(self):
        return str(self.funkrufname)

