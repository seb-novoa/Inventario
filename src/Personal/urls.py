from django.conf.urls import url, include

urlpatterns =   [
    url(r'^puesto/', include('Personal.Puesto.urls')),
]
