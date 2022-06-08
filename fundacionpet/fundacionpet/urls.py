"""fundacionpet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import agregar_products, eliminar_products, restar_products, limpiar_carrito,agregar_productsCart, \
                        agregar_productsW, eliminar_productsW, restar_productsW, limpiar_carritoW,agregar_productsWMVC,\
                        agregar_productsC, eliminar_productsC, restar_productsC, limpiar_carritoC,agregar_productsCMVC


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('agregar/<int:producto_id>/', agregar_products, name="Add"),
    path('agregar2/<int:producto_id>/', agregar_productsCart, name="agregaCarro"),
    path('eliminar/<int:producto_id>/', eliminar_products, name="Del"),
    path('restar/<int:producto_id>/', restar_products, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),


    path('agregarW/<int:producto_id>/', agregar_productsW, name="agregarW"),
    path('agregarW2/<int:producto_id>/', agregar_productsWMVC, name="agregarWMVC"),
    path('eliminarW/<int:producto_id>/', eliminar_productsW, name="eliminarW"),
    path('restarW/<int:producto_id>/', restar_productsW, name="restarW"),
    path('limpiarW/', limpiar_carritoW, name="limpiarW"),


    path('agregarC/<int:producto_id>/', agregar_productsC, name="agregarC"),
    path('agregarC2/<int:producto_id>/', agregar_productsCMVC, name="agregarCMVC"),
    path('eliminarC/<int:producto_id>/', eliminar_productsC, name="eliminarC"),
    path('restarC/<int:producto_id>/', restar_productsC, name="restarC"),
    path('limpiarC/', limpiar_carritoC, name="limpiarC"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


