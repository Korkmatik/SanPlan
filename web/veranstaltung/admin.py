from django.contrib import admin

from . import models


admin.site.register(models.Veranstaltung)
admin.site.register(models.Adresse)
admin.site.register(models.Qualifikation)

