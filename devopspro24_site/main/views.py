from django.shortcuts import render
from .models import Teammates
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def workout(request):
    teammates = Teammates.objects.all()
    return render(request, 'main/workout.html', {'Members': teammates })

def about(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def photos(request):
    return render(request, 'main/photos.html')

