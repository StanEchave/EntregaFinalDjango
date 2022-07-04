from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    titulo=models.CharField(max_length=255)
    subtitulo=models.CharField(max_length=255)
    contenido=models.TextField()
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="postImg",null=True,blank=True)
    fecha=models.DateField(auto_now_add=True)

    def __str__(self): 
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('postDetallado',args=(str(self.id)) )

class Comentarios(models.Model):
    comentario=models.ForeignKey(Post, related_name="comentario" ,on_delete=models.CASCADE)
    contenido=models.TextField()
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    fechaPublicado=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return  '%s - %s' % (self.comentario.titulo,self.autor)
    
    def get_absolute_url(self):
        return reverse('postDetallado',args=(str(self.id)) )
   