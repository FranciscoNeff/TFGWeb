from django.db import models

# Create your models here.
""" 
    En este módulo se encuentran todos los modelos necesarios para la interacción con el usuario.
"""

class SubirImagen(models.Model):
    """
    Modelo para generar el campo de petición de imagenes.

    :Método clase: **SubirImagen** (models.Model).
    :Modelo: SubirImagen.

        :campo imagen: Archivo de imagen a analizar.

    :Modelo: :mod:`models.SubirImagen`.
    """ 
    imagen = models.ImageField(upload_to='images/')


class SubirVideo(models.Model):
    """
    Modelo para generar el campo de petición de video.

    :Método clase: **SubirVideo** (models.Model).
    :Modelo: SubirVideo.

        :campo Video: Archivo de video a analizar.

    :Modelo: :mod:`models.SubirVideo`.
    """ 
    Video = models.FileField(upload_to='videos/')
    class Meta:
        verbose_name='Añadir Video'


class Persona(models.Model):
    """
    Modelo para generar el envio de añadir nuevas personas.

    :Método clase: **Persona** (models.Model).
    :Modelo: Persona.

        :campo nombre: Nombre de la persona a añadir.
        :campo ArchivoZip: Archivo '.zip' con los datos de la persona.

    :Modelo: :mod:`models.Persona`.
    """ 
    nombre=models.CharField(max_length=25)
    ArchivoZip=models.FileField(upload_to='media/')  
    class Meta:
        verbose_name='Añadir Persona'

class Usuarios(models.Model):
    """
    Modelo para generar la base de datos usuarios.

    :Método clase: **Usuarios** (models.Model).
    :Modelo: Usuarios.

        :campo nombre: Nombre de la persona usuario a añadir.

    :Modelo: :mod:`models.Usuarios`.
    """ 
    nombre=models.CharField(max_length=50,primary_key=True)
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'

class Reconocidos(models.Model):
    """
    Modelo para generar la base de datos Reconocidos.

    :Método clase: **Reconocidos** (models.Model).
    :Modelo: Reconocidos.

        :campo nombre: Nombre de la persona usuario a añadir.
        :campo fotos: Número de fotos utilizadas para el entrenamiento.

    :Modelo: :mod:`models.Reconocidos`.
    """ 
    nombre=models.CharField(max_length=50,primary_key=True)
    fotos=models.CharField(max_length=3)
    class Meta:
        verbose_name='Reconocido'
        verbose_name_plural='Reconocidos'



