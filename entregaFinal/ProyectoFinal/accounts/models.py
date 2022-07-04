from distutils.command.upload import upload
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Perfil(models.Model):
    usuario=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    link=models.CharField(max_length=255,null=True)
    imagen=models.ImageField(upload_to="avatares",null=True,blank=True)

    def __str__(self): 
        return str(self.usuario)



