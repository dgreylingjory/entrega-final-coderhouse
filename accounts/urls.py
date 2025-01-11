from django.contrib import admin
from django.urls import path
from accounts import views

app_name = 'acc'

urlpatterns = [
    path('', views.index, name=('index'))
]
