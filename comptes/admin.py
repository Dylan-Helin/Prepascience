from django.contrib import admin
from .models import Personne
from .models import Projet
from .models import PersonneProjet
from .models import ProjetMateriel
from .models import Materiaux
from .models import Admin

# Register your models here.


admin.site.register(Personne)
admin.site.register(ProjetMateriel)
admin.site.register(Projet)
admin.site.register(PersonneProjet)
admin.site.register(Admin)
admin.site.register(Materiaux)