from django.conf.urls import url

from Personal.views import (
    PuestoView, PuestoViewEditar,
    AreaView, AreaViewGuardar
    )
urlpatterns = [
    # Areas
    url(r'^area/$', AreaView.as_view(), name = 'AreaView'),
    url(r'^area/nueva/$', AreaViewGuardar.as_view(), name = 'AreaViewGuardar'),

    # Puestos
    url(r'^puesto/$', PuestoView.as_view(), name = 'home_persona'),
    url(r'^puesto/(?P<puesto_id>[0-9]+)/$', PuestoViewEditar.as_view(), name = 'PuestoViewEditar'),
]
