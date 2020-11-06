import os

from django.db import models
from django.urls import reverse


def vehicle_images(instance, filename):
    return os.path.join('vehicle', str(instance.id), filename)


class VehicleType(models.Model):

    short = models.CharField(max_length=5)
    name = models.CharField(max_length=30)

    def get_short(self):
        return self.short

    def get_name(self):
        return self.name


class Vehicle(models.Model):
    NOT_AVAILABLE = "NV"
    AVAILABLE = "VB"
    WORKSHOP = "WS"
    IN_SERVICE = "ID"
    STATUS_CHOICES = [
        (NOT_AVAILABLE, 'Nicht verfügbar'),
        (AVAILABLE, 'Verfügbar'),
        (WORKSHOP, 'In der Werkstatt'),
        (IN_SERVICE, 'Im Dienst'),
    ]

    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, blank=True, null=True)
    license_plate = models.CharField(max_length=15)
    radio_call_name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to=vehicle_images, blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=AVAILABLE)
    seats = models.PositiveIntegerField()

    def get_name(self):
        return self.name

    def get_license_plate(self):
        return self.license_plate

    def get_radio_call_name(self):
        return self.radio_call_name

    def get_type(self):
        return self.type

    def get_image_path(self):
        return self.image.image_url.url

    def get_status(self):
        return self.status

    def get_seats(self):
        return self.seats

    def has_name(self):
        return (self.name is not None) and (self.name != "")

    def has_radio_call_name(self):
        return (self.radio_call_name is not None) and (self.radio_call_name != "")

    def is_available(self):
        return self.status == self.AVAILABLE

    def get_update_url(self):
        return reverse('vehicles:update', args=(self.id,))

    def __str__(self):
        return str(self.license_plate)
