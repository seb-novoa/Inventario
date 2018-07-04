from django.conf.urls import url

from PersonalEquipo.views import Asignar

urlpatterns =   [
    url(r'^(?P<pk>[0-9]+)/$', Asignar.as_view(), name = 'Asignar'),
]
