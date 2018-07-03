from django.conf.urls import url, include

from Equipo.Equipo.views import CreateEquipo

urlpatterns = [

    # Equipos
    url(r'^nuevo/$', CreateEquipo.as_view(), name = 'CreateEquipo'),


    url(r'^clase/', include('Equipo.Clase.urls')),
    url(r'^software/', include('Equipo.Software.urls')),
    url(r'^hardware/', include('Equipo.Hardware.urls')),
]
