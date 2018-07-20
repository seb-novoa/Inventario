from django.contrib import admin
from Equipo.models import Clase, Software, Hardware, Equipo, MAC

class EquipoAdmin(admin.ModelAdmin):
    search_fields = ('serie', 'serieEnap', 'serieEntel',)
    list_display    =   ('serie','clase', 'serieEnap','serieEntel', 'estado',)
    list_filter = ('estado', 'clase',)

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Clase)
admin.site.register(Software)
admin.site.register(Hardware)
admin.site.register(MAC)
