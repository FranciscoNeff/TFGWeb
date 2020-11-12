"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frweb.views import ImagenView, ImagenDisplay, Home,AnalizarVideovista,AnalizarVideoframe, Lista, IpVideoframe, IpVideovista, camframe, camvista, postjsimagen
from frweb.admin_views import SubirZip,Entrenamiento,BorrarReconocido,ZonaAdmin,borrarfoto,mostrarfoto

urlpatterns = [

    path('',Home,name='Inicio'),
    path('AnalizarImagen', ImagenView.as_view(), name='AnalizarImagen'),
    path('FaceRecognition/<int:pk>/', ImagenDisplay.as_view(), name='Imagendisplay'),
    path('Ipcam', IpVideovista ,name='IpCAM'),
    path('Ipcamframe/', IpVideoframe ,name='IpCAMframe'),
    path('camframe/',camframe, name='camframe'),
    path('WebCam', camvista),
    path('SubirVideo', AnalizarVideovista, name='AnalizarVideo'),
    path('Subirframe', AnalizarVideoframe, name='Analizarframe'),
    path('ListaUsuarios', Lista, name='Usuarios'),
    #path('prueba',prueba),
    path('resultado',postjsimagen),
    #Administración

    path('admin/', admin.site.urls),
    path('administracion',ZonaAdmin),
    path('admin/file',SubirZip,name='AddPersona'),
    path('admin/Entrenamiento', Entrenamiento, name="Entrenamiento"),
    path('admin/borrar', BorrarReconocido, name='BorrarUsuarios'),
    path('mostrar', mostrarfoto, name='Mostrarfotos'),
    path('borrar', borrarfoto, name='borrarfoto'),
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
