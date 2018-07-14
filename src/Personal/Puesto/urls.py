from django.conf.urls import url

#   Vistas en Personal/Puesto
from Personal.Puesto.views import PuestoView


urlpatterns =   [
    url(r'^$', PuestoView.as_view(), name  =   'PuestoView'),
]
