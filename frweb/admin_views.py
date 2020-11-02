import os
import zipfile
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .forms import UploadFileForm, BorrarName
from .models import Persona
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Reconocidos,Usuarios
import FaceRecognition.data_preprocess as entrenar
import FaceRecognition.train_main as modelo
from django.views.decorators.csrf import csrf_exempt
import shutil
#basedir="C:\\Users\\Corgito\\Desktop\\TFG-copia\\"
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@staff_member_required
def SubirZip(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # subir archivo

            Archivo = request.FILES['Archivo']
            nombre = request.POST['Nombre']
            
            # comprobar ruta
            if os.path.isdir(basedir+ '\\FaceRecognition\\train_img\\' + nombre):
                print('ruta existe')
                fs = FileSystemStorage()
                fs.save(Archivo.name, Archivo)
                # UnzipArchivo
                reg = Reconocidos(nombre=nombre)
                reg.save()
                with zipfile.ZipFile((basedir + '\\media\\' + Archivo.name), 'r') as zip_ref:
                    print('Extraer')
                    zip_ref.extractall(basedir + '\\FaceRecognition\\train_img\\' + nombre)  # modificar ruta destino
                ##Borrar ZIP
                os.remove(basedir + '\\media\\' + Archivo.name)
                context={'estado':'La persona ha sido actualizada correctamente'}
                return render(request,'respuestasadmin.html',context) 
                
            else:
                os.mkdir(basedir+ '\\FaceRecognition\\train_img\\' + nombre)
                print('ruta creada')
                fs = FileSystemStorage()
                fs.save(Archivo.name, Archivo)
                # UnzipArchivo
                reg = Reconocidos(nombre=nombre)
                reg.save()
                with zipfile.ZipFile((basedir + '\\media\\' + Archivo.name), 'r') as zip_ref:
                    print('Extraer')
                    zip_ref.extractall(basedir+ '\\FaceRecognition\\train_img\\'+ nombre)  # modificar ruta destino
                ##Borrar ZIP
                os.remove(basedir + '\\media\\' + Archivo.name)

                context={'estado':'La persona ha sido añadida correctamente'}
                return render(request,'respuestasadmin.html',context) 
    else:
        form = UploadFileForm()
    # Load documents for the list page
    documents = Persona.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form}
    return render(request, 'nuevapersona.html', context)


@staff_member_required
def Entrenamiento(request):#Verde
    try:
        print("INFO  [Realizando el modelo]")
        entrenar.DPreprocesses.preproceso(None)
        print("INFO [Entrenando el modelo]")
        modelo.Train_main.train_main(None)
        print('Entrenamiento terminado')

        print('Actualizando la base de datos')
        lista = os.listdir(basedir+ '\\FaceRecognition\\train_img')
        for nombre in lista:
            fotos = os.listdir(basedir+ '\\FaceRecognition\\train_img\\' + nombre)
            p = Usuarios(nombre=nombre, fotos=len(fotos))
            p.save()
            r=Reconocidos(nombre=nombre)
            r.save()
        listado = Usuarios.objects.all()

        context = {'registros': listado, 'resultado': 'El entrenamiento se ha relizado correctamente'}
        return render(request, 'Entrenamiento.html', context)
    except:
        context = {'registros': '' , 'resultado': 'El entrenamiento no se ha podido realizar'}
        return render(request, 'Entrenamiento.html', context)



@staff_member_required
def BorrarReconocido(request):#Verde
    registros = Reconocidos.objects.all()
    lista=''
    for registro in registros:
        lista+=registro.nombre

    if request.method=='POST':
        form=BorrarName(request.POST)
        if form.is_valid():
            #borrar
            nombre=request.POST['Nombre']
            if nombre in lista:
                try:
                    Reconocidos.objects.filter(nombre=nombre).delete()#borraregistro
                    Usuarios.objects.filter(nombre=nombre).delete()#borrar registro
                    if os.path.exists(basedir+ '\\FaceRecognition\\train_img\\' + nombre):#comprueba que existe
                        shutil.rmtree(basedir+ '\\FaceRecognition\\train_img\\' + nombre)#borra carpeta
                    if os.path.exists(basedir+ '\\FaceRecognition\\pre_img\\' + nombre):
                        shutil.rmtree(basedir+ '\\FaceRecognition\\pre_img\\' + nombre)
                    context = {'registros': registros, 'form': form}
                    return render(request, 'BorrarReconocido.html', context)
                except:
                    context = {'registros': registros, 'form': form}
                    return render(request, 'BorrarReconocido.html', context)
            else:
                context = {'registros': registros, 'form': form}
                return render(request, 'BorrarReconocido.html', context)

    else:
        form=BorrarName()

    context = {'registros': registros, 'form': form}
    return render(request, 'BorrarReconocido.html', context)


@staff_member_required
def ZonaAdmin(request):#Verde
    return render(request,'Administracion.html')

@staff_member_required
def prueba(request):
    ruta=basedir+'/FaceRecognition/train_img/01 Alfie Allen'
    listado = os.listdir(ruta)
    for foto in listado:
        print(foto)
    context={'lista':listado }
    return render(request, 'fotos.html',context)

@csrf_exempt
@staff_member_required
def mostrarfoto(request):
    registros = Reconocidos.objects.all()
    form=BorrarName()
    if request.method=='POST':
        form=BorrarName(request.POST)
        if form.is_valid():
            nombre=request.POST['Nombre']
            if os.path.exists(basedir+'/FaceRecognition/train_img/'+nombre):
                ruta=basedir+'/FaceRecognition/train_img/'+nombre
                listado = os.listdir(ruta)
                context={'lista':listado,'nombre':nombre }
            else:
                context={'lista':"",'nombre':"No se ha encontrado la persona introducida" }
            return render(request, 'fotos.html',context)
    
    context = {'registros': registros, 'form': form}
    return render(request, 'BorrarReconocido.html', context)

@csrf_exempt
@staff_member_required
def borrarfoto(request):
    if request.method=='POST':        
        foto=request.POST.urlencode().split('.x')       
        cad=request.POST.urlencode().split('&')
        nombre=cad[2].replace('+'," ").replace('=',"")
        estado='No se ha realizado el borrado'
        try:
            if os.path.exists(basedir+ '\\FaceRecognition\\train_img\\' + nombre +"\\"+ foto[0]):#comprueba que existe
                os.remove(basedir+ '\\FaceRecognition\\train_img\\' + nombre +"\\"+ foto[0])
            if os.path.exists(basedir+ '\\FaceRecognition\\pre_img\\' + nombre +"\\"+ foto[0]):
                os.remove(basedir+ '\\FaceRecognition\\pre_img\\' + nombre +"\\"+ foto[0])
            estado='El borrado se ha realizado correctamente'   
        except:
            print('error en borrado')

        context={'estado':estado}
        return render(request,'respuestasadmin.html',context)   
    else:
        return render(request, 'home.html')