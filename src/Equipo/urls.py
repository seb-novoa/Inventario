from django.conf.urls import url, include

from Equipo.Equipo.views import CreateEquipo, DetailEquipo, addMAC, EditarMAC

urlpatterns = [

    #   Equipos
    url(r'^nuevo/$', CreateEquipo.as_view(), name = 'CreateEquipo'),
    url(r'^(?P<pk>[0-9]+)/$', DetailEquipo.as_view(), name = 'DetailEquipo'),

    #   MAC
    url(r'^(?P<pk>[0-9]+)/mac/$', addMAC.as_view(), name = 'addMAC'),
    url(r'^mac/(?P<pk>[0-9]+)/$', EditarMAC.as_view(), name = 'EditarMAC'),


    url(r'^clase/', include('Equipo.Clase.urls')),
    url(r'^software/', include('Equipo.Software.urls')),
    url(r'^hardware/', include('Equipo.Hardware.urls')),
]
