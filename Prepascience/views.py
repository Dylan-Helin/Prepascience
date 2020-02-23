from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django import forms

from Prepascience.form import HomeForm
from comptes.models import *
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .form import loginForm


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

def get_Login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = loginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = loginForm()

    return render(request, 'login.html', {'form': form})

def login(request):
    return render(request, "login.html")



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
        form = HomeForm
        return render(request, self.template_name, {'form': form})
