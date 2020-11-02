from django.db import models

# Create your models here.

class SubirImagen(models.Model):

    imagen = models.ImageField(upload_to='images/')


class SubirVideo(models.Model):
    Video = models.FileField(upload_to='videos/')
    class Meta:
        verbose_name='Añadir Video'


class Persona(models.Model):
    
    nonmbre=models.CharField(max_length=25)
    ArchivoZip=models.FileField(upload_to='media/')
   

    class Meta:
        verbose_name='Añadir Persona'

class Reconocidos(models.Model):
    nombre=models.CharField(max_length=50,primary_key=True)
    class Meta:
        verbose_name='Reconocido'
        verbose_name_plural='Reconocidos'

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50,primary_key=True)
    fotos=models.CharField(max_length=3)
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'



