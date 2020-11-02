# forms.py 
from django import forms 
from .models import SubirImagen
from .admin import Reconocidos
class ImagenForm(forms.ModelForm): 
  
    class Meta: 
        model = SubirImagen
        fields = ['imagen']

class UploadFileForm(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Archivo = forms.FileField()

class UploadVideoForm(forms.Form):
    Video = forms.FileField()

class BorrarName(forms.Form):
    Nombre = forms.CharField(max_length=50)

class ReconocidosForm(forms.Form):
    Nombre=forms.CharField(max_length=50)

class VideoForm(forms.Form):
    Ip=forms.CharField(max_length=100)
