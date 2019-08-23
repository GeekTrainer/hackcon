from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.

class Register(generic.CreateView):
    model = models.Attendee
    fields = ['name', 'dietary_restriction']

class Details(generic.DetailView):
    model = models.Attendee
