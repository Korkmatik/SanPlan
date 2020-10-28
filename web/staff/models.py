from django.db import models


class Qualification(models.Model):
    title = models.CharField(max_length=30, unique=True)
    short = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.title
