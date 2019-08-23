from django.db import models
from django.urls import reverse

# Create your models here.
class DietaryRestriction(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    dietary_restriction = models.ForeignKey(DietaryRestriction, on_delete=models.PROTECT)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('attendee_details', kwargs={'pk': self.pk})
