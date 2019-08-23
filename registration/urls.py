# Registration

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register.as_view(), name='attendee_register'),
    path('<int:pk>', views.Details.as_view(), name='attendee_details'),
]