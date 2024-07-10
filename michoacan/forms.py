from django import forms
from .models import CrearEvento

class CrearEventoForm(forms.ModelForm):
    class Meta:
        model = CrearEvento
        fields = ['nombre','fecha','hora','lugar','tipo','descripcion']