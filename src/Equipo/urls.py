from django.conf.urls import url, include

from Equipo.Clase.views import ClaseView

urlpatterns = [
    url(r'^clase/$', ClaseView.as_view(), name = 'ClaseView')
]
