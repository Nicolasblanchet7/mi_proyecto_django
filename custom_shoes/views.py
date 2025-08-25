from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.conf import settings
from .models import Sneaker, Carrito, ItemCarrito, Comment # Asegúrate de importar Comment
from .forms import CommentForm, ContactForm # Importa los nuevos formularios

# 1. Función para el registro de nuevos usuarios (Perfil Miembro)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    all_sneakers = Sneaker.objects.all()
    return render(request, 'custom_shoes/inicio.html', {'sneakers': all_sneakers})

# VISTA DE DETALLE DE PRODUCTO CON LÓGICA DE COMENTARIOS
def product_detail(request, pk):
    sneaker = get_object_or_404(Sneaker, pk=pk)
    comments = sneaker.comments.all().order_by('-created_at')

    comment_form = None
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.product = sneaker
                new_comment.user = request.user
                new_comment.save()
                return redirect('product_detail', pk=sneaker.pk)
        else:
            comment_form = CommentForm()

    context = {
        'sneaker': sneaker,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'custom_shoes/product_detail.html', context)

# 2. Lógica para manejar el carrito de un usuario
@login_required
def agregar_al_carrito(request, sneaker_name):
    if request.method == 'POST':
        sneaker = get_object_or_404(Sneaker, name=sneaker_name)
        color = request.POST.get('color')
        talla_str = request.POST.get('talla')

        try:
            talla = int(talla_str)
        except (ValueError, TypeError):
            return redirect('index')

        carrito, creado = Carrito.objects.get_or_create(user=request.user)

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

@login_required
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(user=request.user)
    
    items_carrito = ItemCarrito.objects.filter(carrito=carrito)
    total_carrito = sum(item.get_total() for item in items_carrito)
    
    return render(request, 'custom_shoes/carrito.html', {
        'items_carrito': items_carrito,
        'total_carrito': total_carrito
    })

# 3. Lógica para el perfil Colaborador (opcional, pero cumple el requisito)
@user_passes_test(lambda user: user.is_staff)
def dashboard_colaborador(request):
    return render(request, 'custom_shoes/dashboard_colaborador.html')

# 4. NUEVA VISTA PARA EL FORMULARIO DE CONTACTO
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            send_mail(
                subject,
                message,
                from_email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return render(request, 'custom_shoes/confirmacion_contacto.html')
    else:
        form = ContactForm()
    
    return render(request, 'custom_shoes/contact.html', {'form': form})