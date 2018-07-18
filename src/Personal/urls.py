from django.conf.urls import url, include

#   Vistas
from Personal.Persona.views import CreatePersona, PersonaDetail, UpdatePersona, PersonaGestor, PersonaGestorDelete

urlpatterns =   [
    #   Personas
    url(r'^nuevo/$', CreatePersona.as_view(), name  =   'CreatePersona'),
    url(r'^(?P<pk>[0-9]+)/$', PersonaDetail.as_view(), name  =   'PersonaDetail'),
    url(r'^(?P<pk>[0-9]+)/editar/$', UpdatePersona.as_view(), name  =   'UpdatePersona'),
    url(r'^(?P<pk>[0-9]+)/gestor/$', PersonaGestor.as_view(), name  =   'PersonaGestor'),
    url(r'^(?P<pk>[0-9]+)/gestor/delete/$', PersonaGestorDelete.as_view(), name  =   'PersonaGestorDelete'),

    url(r'^puesto/', include('Personal.Puesto.urls')),
    url(r'^area/', include('Personal.Area.urls')),
]
