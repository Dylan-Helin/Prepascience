from django import forms

from comptes.models import *


class Projetform(forms.ModelForm):
    #Nom_du_projet_ = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Type_du_projet_ = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Description_ = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Projet
        fields = ('nom', 'type', 'description')