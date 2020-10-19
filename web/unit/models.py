from django.db import models

from veranstaltung.models import Veranstaltung


class EVTUnit(models.Model):
    event = models.ForeignKey(Veranstaltung, on_delete=models.CASCADE)

    unit_leader = models.CharField(max_length=80)
    unit_second = models.CharField(max_length=80)
    trainee = models.CharField(max_length=80, blank=True, null=True)

    location = models.CharField(max_length=200)

    additional_information = models.CharField(max_length=300, blank=True, default="")

    def get_leader(self):
        return self.unit_leader

    def get_second(self):
        return self.unit_second

    def get_trainee(self):
        return self.trainee

    def get_location(self):
        return self.location

    def get_additional_information(self):
        return self.additional_information

    def has_trainee(self):
        return self.trainee is not None

    def __str__(self):
        to_str = f"{self.unit_leader} {self.unit_second}"
        if self.has_trainee():
            to_str += f" {self.trainee}"
        return to_str
