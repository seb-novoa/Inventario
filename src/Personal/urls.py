from django.conf.urls import url

from Personal.views import (
    PuestoView, PuestoViewEditar,
    AreaView, AreaViewGuardar, AreaViewEditar,
    PersonaViewGuardar, PersonaViewGestor, PersonaViewEditar,
    PersonaViewEditarGuardar, PersonaViewEditarDelete,
    )
urlpatterns = [
    # Personal
    url(r'^nueva/$', PersonaViewGuardar.as_view(), name = 'PersonaViewGuardar'),
    url(r'^gestor/(?P<persona_id>[0-9]+)/$', PersonaViewGestor.as_view(), name = 'PersonaViewGestor'),
    url(r'^editar/$', PersonaViewEditar.as_view(), name = 'PersonaViewEditar'),
    url(r'^editar/(?P<pk>[0-9]+)/$', PersonaViewEditarGuardar.as_view(), name = 'PersonaViewEditarGuardar'),
    url(r'^editar/(?P<pk>[0-9]+)/delete/$', PersonaViewEditarDelete.as_view(), name = 'PersonaViewEditarDelete'),
    # Areas
    url(r'^area/$', AreaView.as_view(), name = 'AreaView'),
    url(r'^area/nueva/$', AreaViewGuardar.as_view(), name = 'AreaViewGuardar'),
    url(r'^area/(?P<area_id>[0-9]+)/$', AreaViewEditar.as_view(), name = 'AreaViewEditar'),
    # Puestos
    url(r'^puesto/$', PuestoView.as_view(), name = 'home_persona'),
    url(r'^puesto/(?P<puesto_id>[0-9]+)/$', PuestoViewEditar.as_view(), name = 'PuestoViewEditar'),
]
