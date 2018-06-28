from django.conf.urls import url, include

urlpatterns = [
    url(r'^clase/', include('Equipo.Clase.urls')),
    url(r'^software/', include('Equipo.Software.urls')),
    url(r'^hardware/', include('Equipo.Hardware.urls')),
]
