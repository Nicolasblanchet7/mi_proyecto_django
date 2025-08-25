from django.db import models
from django.contrib.auth.models import User

class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Carrito(models.Model):
    # Relación de uno a uno con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrito de {self.user.username}"

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    talla = models.IntegerField()
    cantidad = models.PositiveIntegerField(default=1)

    def get_total(self):
        return self.sneaker.price * self.cantidad

    def __str__(self):
        return f"{self.cantidad} de {self.sneaker.name}"

# Nuevo modelo para el perfil del usuario
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Nuevo modelo para los comentarios y reseñas
class Comment(models.Model):
    product = models.ForeignKey(Sneaker, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.user.username}'