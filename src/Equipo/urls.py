from django.conf.urls import url, include

from Equipo.Equipo.views import CreateEquipo, DetailEquipo, addMAC, EditarMAC, EquipoHardware, EquipoSoftware, DeleteMAC, UpdateEquipo, BuscarEquipo

urlpatterns = [

    #   Equipos
    url(r'^$', BuscarEquipo.as_view(), name = 'BuscarEquipo'),
    url(r'^nuevo/$', CreateEquipo.as_view(), name = 'CreateEquipo'),
    url(r'^(?P<pk>[0-9]+)/$', DetailEquipo.as_view(), name = 'DetailEquipo'),
    url(r'^(?P<pk>[0-9]+)/editar/$', UpdateEquipo.as_view(), name = 'UpdateEquipo'),
    url(r'^(?P<pk>[0-9]+)/hardware/$', EquipoHardware.as_view(), name = 'EquipoHardware'),
    url(r'^(?P<pk>[0-9]+)/software/$', EquipoSoftware.as_view(), name = 'EquipoSoftware'),

    #   MAC
    url(r'^(?P<pk>[0-9]+)/mac/$', addMAC.as_view(), name = 'addMAC'),
    url(r'^mac/(?P<pk>[0-9]+)/$', EditarMAC.as_view(), name = 'EditarMAC'),
    url(r'^mac/(?P<pk>[0-9]+)/delete/$', DeleteMAC.as_view(), name = 'DeleteMAC'),


    url(r'^clase/', include('Equipo.Clase.urls')),
    url(r'^software/', include('Equipo.Software.urls')),
    url(r'^hardware/', include('Equipo.Hardware.urls')),
]
