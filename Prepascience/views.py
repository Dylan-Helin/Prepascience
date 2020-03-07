from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from django import forms

from Prepascience.form import *
from comptes.models import *
from django.contrib.auth import authenticate, login, logout
from django.conf import settings


def homepage(request):
    nbp = Projet.objects.all().count()
    nbm = Materiaux.objects.all().count()
    nbu = User.objects.all().count()
    return render(request, "home.html", {'nbm': nbm, 'nbp': nbp, 'nbu': nbu})


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
    per = User.objects.filter(username__iexact=request.user.username).get
    nbp = PersonneProjet.objects.filter(personne__exact=request.user).count()
    nbcp = Projet.objects.filter(chefProjet__exact=request.user).count()
    nbp = nbp + nbcp

    return render(request, "profil.html", {'per': per, 'nbp': nbp, 'nbcp': nbcp})


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


class demande(TemplateView):
    template_name = 'demande.html'

    def get(self, request):
        form = Demandeform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Demandeform(request.POST)
        if form.is_valid():
            form.save()

            form = Demandeform

        return render(request, self.template_name, {'form': form})


class ajout(TemplateView):
    template_name = 'ajout.html'

    def get(self, request):
        form = Ajoutform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = Ajoutform(request.POST)
        if form.is_valid():
            form.save()

            form = Ajoutform

        return render(request, self.template_name, {'form': form})



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


class ajoutProfil(TemplateView):
    template_name = "creation.html"

    def get(self, request):
        form = CreaProform()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreaProform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            form = CreaProform()
        return render(request, self.template_name, {'form': form})


def projets(request):
    pchef = Projet.objects.filter(chefProjet__exact=request.user)
    pcollab = PersonneProjet.objects.filter(personne__exact=request.user)
    return render(request, "projet.html", {'pchef': pchef, 'pcollab': pcollab})
