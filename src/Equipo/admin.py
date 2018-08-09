from django.contrib import admin
from Equipo.models import Clase, Software, Hardware, Equipo, MAC

class EquipoAdmin(admin.ModelAdmin):
    search_fields = ('serie', 'serieEnap', 'serieProveedor',)
    list_display    =   ('serie','clase', 'serieEnap','serieProveedor', 'estado',)
    list_filter = ('estado', 'clase',)

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Clase)
admin.site.register(Software)
admin.site.register(Hardware)
admin.site.register(MAC)
