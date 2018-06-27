from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^persona/', include('Personal.urls')),
    url(r'^equipo/', include('Equipo.urls')),
]
