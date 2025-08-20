from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('<str:sneaker_name>/', views.product_detail, name='product_detail'),
    path('agregar-al-carrito/<str:sneaker_name>/', views.agregar_al_carrito, name='agregar_al_carrito'),
]