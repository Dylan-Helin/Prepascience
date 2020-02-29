from django import forms

from comptes.models import *


class Projetform(forms.ModelForm):
    nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    b = Materiaux.objects.values_list('type', flat=True).distinct()
    c = [(id, id) for id in b]
    type = forms.ChoiceField(choices=c, widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Projet
        fields = ('nom', 'type', 'description')


class CreaProform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'password')

class Demandeform(forms.ModelForm):
    titre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contenu = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Demande
        fields = ('titre', 'contenu')