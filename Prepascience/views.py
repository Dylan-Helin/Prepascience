from django.http import HttpResponse
from django.shortcuts import render

from comptes.models import *


def homepage(request):
    return render(request, "home.html")


def materiaux(request):
    mat = Materiaux.objects.all()
    return render(request, "materiaux.html", {'mat': mat})


def profil(request):
    return render(request, "profil.html")

def login(request):
    return render(request, "login.html")