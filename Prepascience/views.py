from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from comptes.models import *
from django.contrib.auth import authenticate, login, logout

def homepage(request):
    return render(request, "home.html")


def materiaux(request):
    if request.method == 'GET':
        form = request.GET['form']
        if form == '':
            mat = Materiaux.objects.all()
        else:
            mat = Materiaux.objects.filter(nom__icontains=form)
    else:
        mat = Materiaux.objects.all()
    l= len(mat)
    return render(request, "materiaux.html", {'mat': mat, 'l':l})

def profil(request):
    per = Personne.objects.filter(prenom__iexact='Angele').get

    return render(request, "profil.html", {'per': per})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is None:
        login(request, user)
    else:
        return render(request, "login.html")

def demande(request):
    return render(request, "demande.html")

def ajout(request):
    return render(request, "ajout.html")

def logout(request):
    logout(request)