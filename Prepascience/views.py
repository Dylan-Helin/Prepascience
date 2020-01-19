from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from comptes.models import *


def homepage(request):
    return render(request, "home.html")


def materiaux(request):
    if request.method == 'GET':
        form = request.GET['form']
        if form == 'null':
            mat = Materiaux.objects.all()
        else:
            mat = Materiaux.objects.filter(nom__icontains=form)
    else:
        mat = Materiaux.objects.all()
    l= len(mat)
    return render(request, "materiaux.html", {'mat': mat, 'l':l})


def profil(request):
    return render(request, "profil.html")


def login(request):
    return render(request, "login.html")
