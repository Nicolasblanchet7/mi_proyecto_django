from django.db import models

class Sneaker(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='sneakers/', blank=True)
    
    def __str__(self):
        return self.name
    
    