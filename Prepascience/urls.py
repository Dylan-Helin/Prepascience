from django.conf.urls import url
from . import views

"""Prepascience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Prepascience import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.homepage),
    path('materiel/', views.materiaux),
    path ('profil/', views.profil),
    path('login/',LoginView.as_view(template_name='login.html')),
    path('demande/',views.demande.as_view()),
    path('ajout/',views.ajout),
    path('demandead/',views.demandead),
    path('ajoutProjet/', views.ajoutProjet.as_view()),
    path('logout/',LogoutView.as_view(template_name='logout.html')),
    path('ajoutProfil/', views.ajoutProfil.as_view()),
]

urlpatterns+=staticfiles_urlpatterns()
