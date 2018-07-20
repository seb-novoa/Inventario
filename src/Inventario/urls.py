from django.conf.urls import url, include
from django.contrib import admin

from Equipo.Equipo.views import BuscarEquipo

urlpatterns = [
    url(r'^$', BuscarEquipo.as_view(), name = 'BuscarEquipo'),
    url(r'^admin/', admin.site.urls),
    url(r'^persona/', include('Personal.urls')),
    url(r'^equipo/', include('Equipo.urls')),
    url(r'^asignar/', include('PersonalEquipo.urls')),
]
