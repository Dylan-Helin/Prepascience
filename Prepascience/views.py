from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django import forms

from Prepascience.form import *
from comptes.models import *
from django.contrib.auth import authenticate, login, logout
from django.conf import settings



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
    l = len(mat)
    return render(request, "materiaux.html", {'mat': mat, 'l': l})


def profil(request):
    per = Personne.objects.filter(prenom__iexact='Angele').get

    return render(request, "profil.html", {'per': per})


"""class LoginView(TemplateView):

    template_name = 'login.html'

    def post (self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user =authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL )
        return render(request, self.template_name)"""


def demande(request):
    return render(request, "demande.html")


def ajout(request):
    return render(request, "ajout.html")


def logout(request):
    logout(request)


def demandead(request):
    dem = Demande.objects.all()
    l = len(dem)
    return render(request, "demandead.html", {'dem': dem, 'l': l})


class ajoutProjet(TemplateView):
    template_name = 'creerProjet.html'

    def get(self, request):
        form = Projetform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Projetform(request.POST)
        type = request.POST.get('type')
        form.fields['type'].choices = [(type, type)]
        if form.is_valid():
            projet = form.save(commit=False)
            projet.chefProjet = request.user
            projet.save()

            form = Projetform()

        return render(request, self.template_name, {'form': form})
