from django.urls import path
from . views import RegistroUsuario,EditarUsuario,CambioContraseña


urlpatterns = [
   path('registro/', RegistroUsuario.as_view(), name="registro"),
   path('editarUsuario/', EditarUsuario.as_view(), name="editarUsuario"),
   path('password/', CambioContraseña.as_view(template_name='registration/cambiarContraseña.html')),
]
