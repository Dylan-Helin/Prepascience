from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
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


class projets(TemplateView):

    def get(self, request):
        form = AjoutCollab()
        if request.user.is_authenticated:
            pchef = Projet.objects.filter(chefProjet__exact=request.user)
            pcollab = PersonneProjet.objects.filter(personne__exact=request.user)
            nomcollab = PersonneProjet.objects.all()
            listeMat = ProjetMateriel.objects.all()
            return render(request, "projet.html", {'pchef': pchef, 'pcollab': pcollab, 'form': form, 'nomcollab': nomcollab, 'listeMat': listeMat})
        else:
            return render(request, "projet.html")

    def post(self, request):
        form = AjoutCollab(request.POST)
        nom=request.POST.get('nom')
        id=int(request.POST.get('i'))
        if form.is_valid():
            collaborateur = User.objects.filter(username__exact=nom)
            projet = Projet.objects.filter(id__exact=id).get()
            testDejaExistant = PersonneProjet.objects.filter(personne=collaborateur.get(),projet=projet)
            if testDejaExistant:
                return redirect('/projets')
            if not collaborateur:
                return redirect('/projets')
            else:
                b=form.save(commit=False)
                b.personne = collaborateur.get()
                b.projet = projet
                b.save()
                form = AjoutCollab()
                return redirect('/projets')
