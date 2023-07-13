from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.

admin.site.register(Disciplina)
admin.site.register(Entrenador)
admin.site.register(Atleta)
admin.site.register(Competencia)