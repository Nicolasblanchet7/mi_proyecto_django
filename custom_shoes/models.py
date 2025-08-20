from django.db import models

class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class Carrito(models.Model):
    # La clave primaria ya está definida automáticamente
    def __str__(self):
        return f"Carrito {self.id}"

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