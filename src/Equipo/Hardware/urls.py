from django.conf.urls import url

from Equipo.Hardware.views import HardwareView, CreateHardware

urlpatterns = [
    url(r'^$', HardwareView.as_view(), name = 'HardwareView'),
    url(r'^nuevo/$', CreateHardware.as_view(), name = 'CreateHardware'),
    # url(r'^(?P<pk>[0-9]+)/$', UpdateSoftware.as_view(), name = 'UpdateSoftware'),
    # url(r'^(?P<pk>[0-9]+)/delete/$', DeleteSoftware.as_view(), name = 'DeleteSoftware'),
]
