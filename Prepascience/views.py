from django.http import HttpResponse
from django.shortcuts import render

from comptes.models import *


def homepage(request):
    personnes = Personne.objects.all()
    list = [1] * 10
    return render(request, "home.html", {'personnes': personnes, 'list': list})


def materiaux(request):
    mat = Materiaux.objects.all()
    j = 0
    return render(request, "materiaux.html", {'mat': mat, 'j': j})
