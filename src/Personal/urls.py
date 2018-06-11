from django.conf.urls import url

from Personal.views import PuestoView
urlpatterns = [
    url(r'^puesto/$', PuestoView.as_view(), name = 'home_persona')
]
