from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Attendee)
admin.site.register(models.DietaryRestriction)
