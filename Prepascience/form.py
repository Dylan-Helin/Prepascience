from django import forms

class loginForm(forms.Form):
    Pseudo = forms.CharField(label='Pseudo', max_length=100 )
    MDP = forms.CharField(label='MDP', max_length=100)