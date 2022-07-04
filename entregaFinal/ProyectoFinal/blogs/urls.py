from django.urls import path
from . views import Home,PostDetallado,AgregarPost,EditarPost,EliminarPost,ComentarioPost
from . import views


urlpatterns = [

path('', Home.as_view() , name="home"),
path("about/", views.about, name="about"),
path('post/<int:pk>',PostDetallado.as_view(), name="postDetallado"),
path('agregarPost/', AgregarPost.as_view(),name="agregarPost"),
path('post/editarPost/<int:pk>', EditarPost.as_view(),name="editarPost"),
path('post/<int:pk>/eliminar',EliminarPost.as_view(),name="eliminarPost"),
path('post/<int:pk>/comentarios', ComentarioPost.as_view() , name="comentarios"),

]
