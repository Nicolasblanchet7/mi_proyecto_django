from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'), # Nueva ruta para registro
    path('contact/', views.contact, name='contact'), # Nueva ruta para contacto
    path('product/<int:pk>/', views.product_detail, name='product_detail'), # URL ACTUALIZADA
    path('agregar-al-carrito/<str:sneaker_name>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
]