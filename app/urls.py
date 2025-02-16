from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('predict/', views.predict, name='predict'),
    path('process/', views.process),
    path('about/', views.about),
    path('contact/', views.contact)
]