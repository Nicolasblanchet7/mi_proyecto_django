from django.forms import ModelForm
from .models import Sneaker
from .models import Comment
from django import forms

class SneakerForm(ModelForm):
    class Meta:
        model = Sneaker
        fields = ['name', 'brand', 'description', 'price', 'image']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Tu reseña:',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }
        
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label="Asunto:")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje:")
    from_email = forms.EmailField(label="Tu Correo:")