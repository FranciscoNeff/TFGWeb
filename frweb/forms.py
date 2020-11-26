# forms.py 
from django import forms 
from .models import SubirImagen
from .admin import Reconocidos
""" 
    En este módulo se encuentran todos los formularios necesarios para la interacción con el usuario.
"""
class ImagenForm(forms.ModelForm): 
    """
    Formulario de petición de imágenes.

    :Método clase: **ImagenForm** (forms.ModelForm).
    :Formulario: ImagenForm.

        :campo imagen: Archivo de imagen a analizar.

    :Modelo: :mod:`models.SubirImagen`.
    """ 
    class Meta: 
        model = SubirImagen
        fields = ['imagen']

class UploadFileForm(forms.Form):
    """
    Formulario de petición para añadir nuevas personas.

    :Método clase: **UploadFileForm** (forms.Form).

    :Formulario: UploadFileForm.
    
        :campo Nombre: Nombre de la nueva persona.
        :campo Archivo: Archivo con los datos de la persona en formato ".zip".

    :Modelo: :mod:`models.Persona`.
    """ 
    Nombre = forms.CharField(max_length=50)
    Archivo = forms.FileField()

class UploadVideoForm(forms.Form):
    """
    Formulario de petición para añadir nuevas personas.

    :Método clase: **UploadVideoForm** (forms.Form).

    :Formulario: UploadVideoForm.

        :campo Video: Archivo de video a analizar.

    :Modelo: :mod:`models.SubirVideo`.
    """ 
    Video = forms.FileField()

class BorrarName(forms.Form):
    """
    Formulario de petición para borrar una persona.

    :Método clase: **BorrarName** (forms.Form).

    :Formulario: BorrarName.

        :campo Nombre: Campo de texto para introducir el valor.

    :Modelo: :mod:`models.Usuarios`.
    """ 
    Nombre = forms.CharField(max_length=50)

class ReconocidosForm(forms.Form):
    """
    Formulario de petición para añadir nuevas personas.

    :Método clase: **ReconocidosForm** (forms.Form).

    :Formulario: ReconocidosForm.

        :campo Nombre: Campo de texto para introducir el valor.

    :Modelo: :mod:`models.Reconocidos`.
    """ 
    Nombre=forms.CharField(max_length=50)

class VideoForm(forms.Form):
    """
    Formulario de petición para conseguir la dirección Ip de la cámara y otros campos de texto.

    :Método clase: **VideoForm** (forms.Form).

    :Formulario: UploadVideoForm.

        :campo Ip: Campo de texto para introducir el valor.

    :Modelo: :mod:`models.Reconocidos`.
    """ 
    Ip=forms.CharField(max_length=100)
