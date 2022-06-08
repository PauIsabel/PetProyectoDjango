# from django.conf.urls import url
# from django.conf import settings
# from django.views.static import serve
from django.urls import path
from .views import index,blog_detalle,blog,carro,checkout,compare,error_404,\
                    galeria,login_register,nosotros,producto_detalle,registro,\
                    wishlist,tiendafor,contacto1,listar_producto,agregar_producto,\
                    modificar_producto,eliminar_producto,registro_usuario,mi_cuenta,\
                    mi_cuenta_CRUD

urlpatterns = [
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
    path('', index, name="index"),
    path('blog_detalle/', blog_detalle, name="blog_detalle"),
    path('blog/', blog, name="blog"),
    path('carro/', carro, name="carro"),
    path('checkout/', checkout, name="checkout"),
    path('compare/', compare, name="compare"),
    path('error_404/', error_404, name="error_404"),
    path('galeria/', galeria, name="galeria"),
    path('login_register/', login_register, name="login_register"),
    path('nosotros/', nosotros, name="nosotros"),
    path('producto_detalle/', producto_detalle, name="producto_detalle"),
    path('registro/', registro, name="registro"),
    path('wishlist/', wishlist, name="wishlist"),

    path('tiendafor/', tiendafor, name="tiendafor"),
    path('contacto1/', contacto1, name="contacto1"),
    path('listar_producto/', listar_producto, name="listar_producto"),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro_usuario/', registro_usuario, name="registro_usuario"),
    path('mi_cuenta/', mi_cuenta, name="mi_cuenta"),
    path('mi_cuenta_CRUD/', mi_cuenta_CRUD, name="mi_cuenta_CRUD"),

]