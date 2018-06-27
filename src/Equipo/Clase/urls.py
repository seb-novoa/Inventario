from django.conf.urls import url, include

from Equipo.Clase.views import ClaseView, UpdateClase, DeleteClase

urlpatterns = [
    url(r'^$', ClaseView.as_view(), name = 'ClaseView'),
    url(r'^(?P<pk>[0-9]+)/$', UpdateClase.as_view(), name = 'UpdateClase'),
    url(r'^(?P<pk>[0-9]+)/delete/$', DeleteClase.as_view(), name = 'DeleteClase'),

]
