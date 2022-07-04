
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from .models import Post, Comentarios
from .forms import ComentarioForm
from django.contrib.auth.decorators import login_required



def about(request):
    return render(request,'about.html')


class Home(ListView):
    model = Post  
    template_name= 'home.html'
    ordering=['-fecha']

class PostDetallado(DetailView):
    model=Post
    template_name= 'postDetallado.html'

class AgregarPost(CreateView):
    model=Post
    template_name= 'agregarPost.html'
    fields= '__all__'


class EditarPost(UpdateView):
    model=Post
    template_name= 'editarPost.html'
    fields=('titulo','subtitulo','contenido','imagen')

class EliminarPost(DeleteView):
    model=Post
    template_name='eliminarPost.html'
    success_url= reverse_lazy('home')

class ComentarioPost(CreateView):
    model=Comentarios
    form_class=ComentarioForm
    template_name='comentarios.html'
    
    def form_valid(self, form):
        form.instance.comentario_id=self.kwargs['pk']
        return super().form_valid(form)

    success_url= reverse_lazy('home')