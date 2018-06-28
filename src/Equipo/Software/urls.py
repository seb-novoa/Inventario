from django.conf.urls import url

from Equipo.Software.views import SoftwareView, UpdateSoftware, DeleteSoftware

urlpatterns = [
    url(r'^$', SoftwareView.as_view(), name = 'SoftwareView'),
    url(r'^(?P<pk>[0-9]+)/$', UpdateSoftware.as_view(), name = 'UpdateSoftware'),
    url(r'^(?P<pk>[0-9]+)/delete/$', DeleteSoftware.as_view(), name = 'DeleteSoftware'),
]
