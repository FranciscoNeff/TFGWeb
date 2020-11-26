"""
ejemplo de configuración de URL

En `urlpatterns` esta la lista de rutas URLs para vistas. Para mas información por favor revise: https://docs.djangoproject.com/en/3.0/topics/http/urls/
Cada una de estas rutas hace referencia a un servicio. Para mas información revise el manual de usuario. 

"""
from django.contrib import admin
from django.urls import path
from frweb.views import ImagenView, ImagenDisplay, Home,AnalizarVideovista,AnalizarVideoframe, Lista, IpVideoframe, IpVideovista, camvista, postjsimagen
from frweb.admin_views import SubirZip,Entrenamiento,BorrarReconocido,ZonaAdmin,borrarfoto,mostrarfotoborrado, mostrarfoto

urlpatterns = [

    path('',Home,name='Inicio'),

    path('AnalizarImagen', ImagenView.as_view(), name='AnalizarImagen'),
    path('FaceRecognition/<int:pk>/', ImagenDisplay.as_view(), name='Imagendisplay'),

    path('Ipcam', IpVideovista ,name='IpCAM'),
    path('Ipcamframe/', IpVideoframe ,name='IpCAMframe'),

    path('WebCam', camvista, name='WebCam'),
    path('resultado',postjsimagen),

    path('SubirVideo', AnalizarVideovista, name='AnalizarVideo'),
    path('Subirframe', AnalizarVideoframe, name='Analizarframe'),
    
    path('ListaUsuarios', Lista, name='Usuarios'),
    
    #Administración

    path('administracion',ZonaAdmin),

    path('admin/file',SubirZip,name='AddPersona'),

    path('admin/Entrenamiento', Entrenamiento, name="Entrenamiento"),

    path('admin/borrar', BorrarReconocido, name='BorrarUsuarios'),

    path('borrarfotos', mostrarfotoborrado, name='MostrarfotosBorrado'),
    path('borrar', borrarfoto, name='borrarfoto'),
    
    path('verfotos', mostrarfoto, name='Mostrarfotos'),

    #Admin de Django
    path('admin/', admin.site.urls),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
