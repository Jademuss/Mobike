from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.inicio, name='inicio'),
    #path('inicio/cli_lista/', views.cli_lista, name='cli_lista'),
    #path('inicio/cli_lista/<int:pk>/', views.regis_view, name='regis_view'),
    #path('inicio/regis/', views.regis, name= 'regis),
    #path('inicio/<int:pk>/edit/', views.regis_edit , name ='regis_edit'),
]
