from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('workout', views.workout),
    path('about', views.about),
    path('contacts', views.contacts)
]