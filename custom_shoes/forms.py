from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Tu reseña'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu reseña aquí...'})
        }

class ContactForm(forms.Form):
    subject = forms.CharField(label='Asunto', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 6}))
    from_email = forms.EmailField(label='Tu Correo', widget=forms.EmailInput(attrs={'class': 'form-control'}))