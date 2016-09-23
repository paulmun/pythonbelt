from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="poke_index"),
    url(r'^(?P<pokedID>[0-9]+$)', views.poke, name="poke_poke")
]