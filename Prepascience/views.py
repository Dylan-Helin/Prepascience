from django.http import HttpResponse
from django.shortcuts import render

from comptes.models import *


def homepage(request):
    return render(request, "home.html")


def materiaux(request):
    mat = Materiaux.objects.all()
    return render(request, "materiaux.html", {'mat': mat})


def profil(request):
    per = Personne.objects.filter(prenom__iexact='Angele').get

    return render(request, "profil.html", {'per': per})

def login(request):
    return render(request, "login.html")

def demande(request):
    return render(request, "demande.html")

def ajout(request):
    return render(request, "ajout.html")