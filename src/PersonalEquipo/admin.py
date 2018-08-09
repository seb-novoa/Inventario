from django.contrib import admin

#   Modelos
from PersonalEquipo.models import PersonalEquipo, PersonalEquipoHistoria

class PersonaAdmin(admin.ModelAdmin):
    list_filter = ('persona__area', 'equipo__clase',)

admin.site.register(PersonalEquipo, PersonaAdmin)
# admin.site.register(PersonalEquipoHistoria)
