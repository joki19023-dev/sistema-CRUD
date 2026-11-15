from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'estado', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la publicación'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Escribe el contenido aquí...'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del autor'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
