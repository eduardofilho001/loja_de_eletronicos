from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    
#....................... CONTA ......................
    path('login/', views.login, name="login"),
    path('cadastro/', views.cadastro, name="cadastro"),
#....................................................

#.................... NAVBAR LINKS ..................
    path('lojas', views.lojas, name="lojas"),
    path('computadores', views.computadores, name="computadores"),
    path('tablets', views.tablets, name="tablets"),
    path('drones_camera', views.drones_camera, name="drones_camera"),
    path('audio', views.audio, name="audio"),
    path('mobile', views.mobile, name="mobile"),
    path('tv_home_theater', views.tv_home_theater, name="tv_home_theater"),
    path('tec_vestivel', views.tec_vestivel, name="tec_vestivel"),
    path('promocoes', views.promocoes, name="promocoes"),
#......................................................

#.................... PRODUTOS ......................
    path('prod_details', views.prod_details, name="prod_details"),
#....................................................
]    