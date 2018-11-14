from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cliente/<int:ID_CLIENTE>/', views.getCliente, name='getCliente'),
    #path('inicio/regis/', views.regis, name= 'regis),
    #path('inicio/cli_lista/', views.cli_lista, name='cli_lista'),
    #path('inicio/cli_lista/<int:pk>/', views.regis_view, name='regis_view'),
    #path('inicio/<int:pk>/edit/', views.regis_edit , name ='regis_edit'),
]
