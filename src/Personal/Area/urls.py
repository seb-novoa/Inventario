from django.conf.urls import url

#   Vistas
from Personal.Area.views import AreaView, CreateArea, UpdateArea, DeleteArea

urlpatterns =   [
    url(r'^$', AreaView.as_view(), name =   'AreaView'), #   Listado de las areas
    url(r'^nueva/$', CreateArea.as_view(), name =   'CreateArea'), #   Vista para agregar un area
    url(r'^(?P<pk>[0-9]+)/$', UpdateArea.as_view(), name =   'UpdateArea'), #   Vista para editar un area
    url(r'^(?P<pk>[0-9]+)/delete/$', DeleteArea.as_view(), name =   'DeleteArea'), #   Eliminar un area
]
