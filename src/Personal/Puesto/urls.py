from django.conf.urls import url

#   Vistas en Personal/Puesto
from Personal.Puesto.views import PuestoView, UpdatePuesto, DeletePuesto


urlpatterns =   [
    url(r'^$', PuestoView.as_view(), name  =   'PuestoView'),
    url(r'^(?P<pk>[0-9]+)/$', UpdatePuesto.as_view(), name  =   'UpdatePuesto'),
    url(r'^(?P<pk>[0-9]+)/delete$', DeletePuesto.as_view(), name  =   'DeletePuesto'),
]
