from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from frweb.forms import ImagenForm,VideoForm,UploadVideoForm
from django.http import HttpResponse
from django.views.generic import DetailView
from frweb.models import SubirImagen
import FaceRecognition.identify_face_image as ifm
from django.core.files.storage import FileSystemStorage
from .models import SubirVideo, Usuarios
import base64
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt

from django.http import StreamingHttpResponse
from FaceRecognition.identity_face_videoweb import identify_face_video as ifv
from FaceRecognition.identity_face_webcam import identify_face_webcam as ifw

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def Home(request):#Verde
    return render(request, 'home.html')


class ImagenView(TemplateView):#VERDE pero no es mio

    form = ImagenForm
    template_name = 'imagenview.html'
    def post(self, request, *args, **kwargs):

        form = ImagenForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            ruta=basedir+"/"+obj.imagen.url
            valor=ifm.identify_face_image.resultado(None, ruta)#devuelva ruta de la nueva foto
            return HttpResponseRedirect(reverse_lazy('Imagendisplay', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     
    
    def get(self, request, *args, **kwargs):
        #Cada vez que hacemos una petición al servidor borramos las fotos en su interior.
        ruta=(basedir+"/media/images")
        fotos = os.listdir(ruta)
        for foto in fotos:
            os.remove(basedir+"/media/images/"+foto)
        return self.post(request, *args, **kwargs)

class ImagenDisplay(DetailView):
    
    model = SubirImagen
    template_name = 'imagendisplay.html'
    context_object_name = 'img'

def AnalizarVideovista(request):
    return render(request, 'AnalizarVideoVista.html')

@xframe_options_sameorigin
@csrf_exempt
def AnalizarVideoframe(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            Archivo = request.FILES['Video']
            fs = FileSystemStorage(basedir+"/media/videos")
            fs.save(Archivo.name, Archivo)
            rArchivo= basedir+"/media/videos"+'/'+Archivo.name
            frame = (ifv.resultado(None, rArchivo))
            return StreamingHttpResponse(frame, content_type='multipart/x-mixed-replace; boundary=frame')
    else:
        form = UploadVideoForm()      
        try:
            archivos = os.listdir(basedir+"/media/videos")
            for archivo in archivos:
                os.remove(basedir+"/media/videos/"+ archivo)
        except:
            print('no se ha podido borrar')
    msg='Introduzca el video a analizar'
    context = {'msg':msg, 'form': form}
    return render(request, 'AnalizarVideoframe.html', context)


def Lista(request):#verde
    registros=Usuarios.objects.all()
    context={'registros':registros}
    return render(request,'ListaReconocidos.html',context)

@xframe_options_sameorigin
def IpVideovista(request):
    return render(request,'AnalizarVideoIPvista.html')

@xframe_options_sameorigin
@csrf_exempt
def IpVideoframe(request):
    form = VideoForm()
    msg='Introduzca dirección Ip de su camara IP'
    if request.method == 'POST':
        dirIP=request.POST['Ip']
        frame = (ifv.resultado(None, dirIP))
        return StreamingHttpResponse(frame, content_type='multipart/x-mixed-replace; boundary=frame')
    else:
        context={'msg':msg,'form':form}
        return render(request,'AnalizarVideoframe.html',context)


def camvista(request):
    return render(request, 'webcamjs.html')

@csrf_exempt
def postjsimagen(request):
    if request.method == 'POST':
        base=request.POST['img']
        token=request.POST['token']
        im = Image.open(BytesIO(base64.b64decode(base)))
        ruta=basedir+'/media/images/'+token+'.png'
        im.save(ruta, 'PNG')
        valor=ifm.identify_face_image.resultado(None, ruta)#devuelva ruta de la nueva foto
        return HttpResponse('media/images/'+token+'.png')
        
    else:
        return HttpResponse('empty')


