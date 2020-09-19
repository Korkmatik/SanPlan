from django.db import models

def fahrzeug_images(instance, filename):
    return 'fahrzeuge/static/fahrzeug_pics/{}'.format(filename)


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

    name = models.CharField(max_length=30, null=True)
    kennzeichen = models.CharField(max_length=15)
    funkrufname = models.CharField(max_length=30)
    typ = models.CharField(max_length=10)
    filename = models.CharField(max_length=30, blank=True, default="")
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=VERFUEGBAR)

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
