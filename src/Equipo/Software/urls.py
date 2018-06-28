from django.conf.urls import url

from Equipo.Software.views import SoftwareView, UpdateSoftware

urlpatterns = [
    url(r'^$', SoftwareView.as_view(), name = 'SoftwareView'),
    url(r'^(?P<pk>[0-9]+)/$', UpdateSoftware.as_view(), name = 'UpdateSoftware'),
]
