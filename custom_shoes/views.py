from django.shortcuts import render, get_object_or_404
from .models import Sneaker

def index(request):
    all_sneakers = Sneaker.objects.all()
    return render(request, 'custom_shoes/inicio.html', {'sneakers': all_sneakers})

def product_detail(request, sneaker_name):  # <-- Asegúrate de que esta función esté aquí
    sneaker = get_object_or_404(Sneaker, name=sneaker_name)
    return render(request, 'custom_shoes/product_detail.html', {'sneaker': sneaker})
