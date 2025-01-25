from django.contrib import admin
from django.urls import path
from fuel import views
from fuel.views import *

app_name = 'fuel'

urlpatterns = [
    path('', views.index, name='index'),

    path('vales/', ValeListView.as_view(), name='vale_list'),
    path('vales/create/', ValeCreateView.as_view(), name='crear_vale'),	
    path('vales/<int:pk>/update', ValeUpdateView.as_view(), name='vale_update'),
    path('vales/<int:pk>/detail', ValeDetailView.as_view(), name='vale_detail'),
    path('vales/<int:pk>/delete', ValeDeleteView.as_view(), name='vale_delete'),

    ##path('modelo/', ModeloHelicopteroListView.as_view(), name='modelo_list'),
    path('modelo/create/', ModeloHelicopteroCreateView.as_view(), name='modelo_create'),
    path('modelo/<int:pk>/update/', ModeloHelicopteroUpdateView.as_view(), name='modelo_update'),
    path('modelo/<int:pk>/detail/', ModeloHelicopteroDetailView.as_view(), name='modelo_detail'),
    path('modelo/<int:pk>/delete/', ModeloHelicopteroDeleteView.as_view(), name='modelo_delete'),
    
    ##path('aeronave/', AeronaveListView.as_view(), name='aeronave_list'),
    path('aeronave/create/', AeronaveCreateView.as_view(), name='aeronave_create'),
    path('aeronave/<int:pk>/update/', AeronaveUpdateView.as_view(), name='aeronave_update'),
    path('aeronave/<int:pk>/detail/', AeronaveDetailView.as_view(), name='aeronave_detail'),
    path('aeronave/<int:pk>/delete/', AeronaveDeleteView.as_view(), name='aeronave_delete'),
    
    ##path('camion/', CamionListView.as_view(), name='camion_list'),
    path('camion/create/', CamionCreateView.as_view(), name='camion_create'),
    path('camion/<int:pk>/update/', CamionUpdateView.as_view(), name='camion_update'),
    path('camion/<int:pk>/detail/', CamionDetailView.as_view(), name='camion_detail'),
    path('camion/<int:pk>/delete/', CamionDeleteView.as_view(), name='camion_delete'),
]