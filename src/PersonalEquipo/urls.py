from django.conf.urls import url

from PersonalEquipo.views import Asignar, Devolver

urlpatterns =   [
    url(r'^(?P<pk>[0-9]+)/$', Asignar.as_view(), name = 'Asignar'),
    url(r'^(?P<pk>[0-9]+)/devolver/$', Devolver.as_view(), name = 'Devolver'),
]
