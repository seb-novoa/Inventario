from django.conf.urls import url

from Equipo.Hardware.views import HardwareView, CreateHardware, UpdateHardware, DeleteHardware

urlpatterns = [
    url(r'^$', HardwareView.as_view(), name = 'HardwareView'),
    url(r'^nuevo/$', CreateHardware.as_view(), name = 'CreateHardware'),
    url(r'^(?P<pk>[0-9]+)/$', UpdateHardware.as_view(), name = 'UpdateHardware'),
    url(r'^(?P<pk>[0-9]+)/delete/$', DeleteHardware.as_view(), name = 'DeleteHardware'),
]
