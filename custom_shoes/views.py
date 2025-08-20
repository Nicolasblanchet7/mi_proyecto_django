from django.shortcuts import render, get_object_or_404, redirect
from .models import Sneaker, Carrito, ItemCarrito # <-- Asegúrate de que los modelos estén aquí

def index(request):
    all_sneakers = Sneaker.objects.all()
    return render(request, 'custom_shoes/inicio.html', {'sneakers': all_sneakers})

def product_detail(request, sneaker_name):
    sneaker = get_object_or_404(Sneaker, name=sneaker_name)
    return render(request, 'custom_shoes/product_detail.html', {'sneaker': sneaker})

def agregar_al_carrito(request, sneaker_name):
    if request.method == 'POST':
        sneaker = get_object_or_404(Sneaker, name=sneaker_name)
        color = request.POST.get('color')
        talla_str = request.POST.get('talla')

        try:
            talla = int(talla_str)
        except (ValueError, TypeError):
            return redirect('index')
        
        # Obtiene o crea un carrito (solución temporal para pruebas)
        carrito, creado = Carrito.objects.get_or_create(id=1)

        # Agrega o actualiza el ítem en el carrito
        item_carrito, creado = ItemCarrito.objects.get_or_create(
            carrito=carrito,
            sneaker=sneaker,
            color=color,
            talla=talla
        )
        
        if not creado:
            item_carrito.cantidad += 1
            item_carrito.save()
        
        mensaje = f"{sneaker_name} ha sido agregado a tu carrito."
        return render(request, 'custom_shoes/confirmacion.html', {'mensaje': mensaje})
    
    return redirect('index')

def ver_carrito(request):
    # Obtiene el carrito (temporalmente el de id=1)
    carrito, creado = Carrito.objects.get_or_create(id=1)
    
    # Obtiene todos los ítems de ese carrito
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    
    return render(request, 'custom_shoes/carrito.html', {'items_carrito': items_carrito})