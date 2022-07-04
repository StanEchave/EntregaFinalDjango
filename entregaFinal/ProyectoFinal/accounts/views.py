
from django.shortcuts import render
from django.views import generic 
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistroForm,PerfilForm


class RegistroUsuario(generic.CreateView):
    form_class=RegistroForm
    template_name='registration/registro.html'
    success_url= reverse_lazy('login')



class EditarUsuario(generic.UpdateView):
    form_class=PerfilForm
    template_name='registration/editarPerfil.html'
    success_url= reverse_lazy('home')

    def get_object(self):
        return self.request.user


class CambioContraseña(PasswordChangeView):
    form_class= PasswordChangeForm
    success_url= reverse_lazy('editarUsuario')





