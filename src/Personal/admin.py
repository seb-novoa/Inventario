from django.contrib import admin
#   Model
from Personal.models import Persona, Area, Puesto


class PersonaAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', )
    list_filter = ('Gestor','area', )
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'area', 'puesto', 'Gestor')

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Area)
admin.site.register(Puesto)
