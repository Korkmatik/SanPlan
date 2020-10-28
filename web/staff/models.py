from django.db import models


class Qualification(models.Model):
    title = models.CharField(max_length=20)
    short = models.CharField(max_length=10)

    def __str__(self):
        return self.titel
