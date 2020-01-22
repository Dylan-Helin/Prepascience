from django.db import models
from django.db.models import TextField
from django.contrib.auth.models import User


# Create your models here.


class Personne(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    mdp = models.CharField(max_length=16)
    login = models.CharField(max_length=100)

    def __str__(self):
        return self.login


class Materiaux(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    important = TextField()
    description = TextField()
    infoGeneral = TextField()

    def __str__(self):
        return self.nom


class Admin(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    mdp = models.CharField(max_length=16)
    login = models.CharField(max_length=100)

    def __str__(self):
        return self.login


class Projet(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = TextField()
    chefProjet = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class PersonneProjet(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)


class ProjetMateriel(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    materiaux = models.ForeignKey(Materiaux, on_delete=models.CASCADE)


class Demande(models.Model):
    titre = models.CharField(max_length=100)
    contenu = TextField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.titre
