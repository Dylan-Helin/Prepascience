from django.http import HttpResponse
from django.shortcuts import render

from comptes.models import Personne


def homepage(request):
    personnes = Personne.objects.all()
    list=[1]*10
    return render(request,"home.html", {'personnes': personnes,'list':list})
