from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('predict/', views.predict, name='predict'),
    path('process', views.process)
]