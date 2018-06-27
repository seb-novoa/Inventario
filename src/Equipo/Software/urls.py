from django.conf.urls import url

from Equipo.Software.views import SoftwareView

urlpatterns = [
    url(r'^$', SoftwareView.as_view(), name = 'SoftwareView'),
]
