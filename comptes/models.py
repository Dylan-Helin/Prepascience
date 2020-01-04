from django.db import models

# Create your models here.

class Personne(models.Model):
    prenom=models.CharField(max_length=100)
    nom=models.CharField(max_length=100)
    mdp=models.CharField(max_length=16)
    login=models.CharField(max_length=100)

    def __str__(self):
        return self.prenom