
from django.contrib import admin
from django.urls import path
from home import views as home
from . import views
urlpatterns = [
    path('', views.index, name='home')
]
