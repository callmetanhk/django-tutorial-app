
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('bestseller/', views.bestseller, name='bestseller'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('single', views.single, name='single'),
]

handler404 = 'myapp.views.custom_404'