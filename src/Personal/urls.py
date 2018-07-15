from django.conf.urls import url, include

urlpatterns =   [
    url(r'^puesto/', include('Personal.Puesto.urls')),
    url(r'^area/', include('Personal.Area.urls')),
]
