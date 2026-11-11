from django.contrib import admin
from .models import Carrera, Profesor, Materia, Aula

# No era necesario pero quise implementarlo
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Aula)