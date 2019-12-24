from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('product/', views.products, name='products'),
    path('customer/<str:pk>/', views.customers, name='customers'),
    #path('order/create/<str:pk>/', views.createOrder, name='createOrder'),
    path('update/order/<str:pk>/', views.UpdateForm, name='UpdateForm'),
path('delete/order/<str:pk>/', views.deleteForm, name='deleteForm'),
]
