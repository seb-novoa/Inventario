from django.conf.urls import url

from Personal.views import PuestoView, PuestoViewEditar
urlpatterns = [
    url(r'^puesto/$', PuestoView.as_view(), name = 'home_persona'),
    url(r'^puesto/(?P<puesto_id>[0-9]+)/$', PuestoViewEditar.as_view(), name = 'PuestoViewEditar'),
]
