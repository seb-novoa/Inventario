from django.conf.urls import url

from PersonalEquipo.views import Asignar, Devolver, Historial, HistorialEquipo

urlpatterns =   [
    url(r'^(?P<pk>[0-9]+)/$', Asignar.as_view(), name = 'Asignar'),
    url(r'^(?P<pk>[0-9]+)/devolver/$', Devolver.as_view(), name = 'Devolver'),
    url(r'^historial/(?P<pk>[0-9]+)/$', Historial.as_view(), name = 'Historial'),
    url(r'^historial_equipo/(?P<pk>[0-9]+)/$', HistorialEquipo.as_view(), name = 'HistorialEquipo'),
]
