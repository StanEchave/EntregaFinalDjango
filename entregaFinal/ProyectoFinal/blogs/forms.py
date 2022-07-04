from .models import Comentarios
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentarios
        fields=('contenido','autor')