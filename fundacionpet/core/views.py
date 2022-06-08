from unittest import expectedFailure
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Producto
from .forms import Contacto1Form, ProductoForm, RegistroUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from core.cart import Cart,Wishlist, Compare

# from django.views.generic import TemplateView


# Create your views here.

def base_1(request):
    productos = Producto.objects.all()
    data = {
        'productosTienda': productos,
    }
    return render(request, 'core/base_1.html',data)

def index(request):
    return render(request, 'core/index.html')

def error_404(request):
    return render(request, 'core/error_404.html')

def blog(request):
    return render(request, 'core/blog.html')

def blog_detalle(request):
    return render(request, 'core/blog_detalle.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def registro(request):
    return render(request, 'core/registro.html')

def login_register(request):
    return render(request, 'core/login_register.html')

def mi_cuenta(request):
    return render(request, 'core/mi_cuenta.html')

def mi_cuenta_CRUD(request):
    return render(request, 'core/mi_cuenta_CRUD.html')




def producto_detalle(request):
    return render(request, 'core/producto_detalle.html')

def carro(request):
    productos = Producto.objects.all()
    data = {
        'productosTienda': productos,
    }
    return render(request, 'core/carro.html',data)

def checkout(request):
    return render(request, 'core/checkout.html')

def wishlist(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 10)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'productosTienda': productos,
        'paginator': paginator
    }
    return render(request, 'core/wishlist.html',data)

def compare(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'productosTienda': productos,
        'paginator': paginator
    }
    return render(request, 'core/compare.html',data)



def tiendafor(request):
    productos = Producto.objects.all()
    #Paginacion
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 12)
        productos = paginator.page(page)
    except:
        raise Http404
    #Variable
    data = {
        'productosTienda': productos,
        #Paginacion
        'paginator': paginator
    }
    return render(request, 'core/tiendafor.html', data)


#FORMULARIOS
def contacto1(request):
    data = {
        'form': Contacto1Form()
    }
    if(request.method == "POST"):
        formulario = Contacto1Form(data=request.POST)
        if(formulario.is_valid()):
            formulario.save()
            messages.success(request, "Mensaje enviado exitosamente")

            #Para limpiar la pag. una vez enviado el mensaje
            return redirect('index')
        else:
            messages.error(request, "No se ha podido enviar su mensaje, intente nuevamente")
            data["form"] = formulario

    return render(request, 'core/contacto1.html', data)

#CRUD Productos
#LISTAR CRUD
def listar_producto(request):
    productos = Producto.objects.all()
    #Paginacion
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    #Variable
    data = {
        'productosTienda': productos,
        #Paginacion
        'paginator': paginator
    }
    return render(request, 'core/crud/listar_producto.html', data)


#AGREGAR CRUD
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if(request.method == "POST"):
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if(formulario.is_valid()):
            formulario.save() 
            messages.success(request, "Producto registrado correctamente")
            #Para limpiar la pag. una vez agregado el producto
            return redirect('/mi_cuenta_CRUD')
        else:
            messages.error(request, "No se ha podido agregar el producto, intente nuevamente")
            data["form"] = formulario
    return render(request, 'core/crud/agregar_producto.html', data)

#MODIFICAR CRUD
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form':ProductoForm(instance=producto)
    }
    if(request.method == 'POST'):
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if(formulario.is_valid()):
            formulario.save()
            messages.success(request, "Registro modificado correctamente" )
            return redirect('/listar_producto')
        else:
            messages.error(request, "El producto no se ha podido modificar" )
            data['form'] = formulario
    return render(request, 'core/crud/modificar_producto.html', data)

#ELIMINAR CRUD
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    try:
        producto.delete()
        messages.success(request, "Producto eliminado exitosamente")
    except:
        messages.error(request, "El producto no se ha podido eliminar")
    return redirect('/listar_producto')

#REGISTRO USUARIO
def registro_usuario(request):
    #Para enviarlo al template
    data = {
        'form': RegistroUserCreationForm()
    }
    #Validar metodo POST
    if(request.method == 'POST'):
        formulario = RegistroUserCreationForm(data=request.POST)
        if(formulario.is_valid()):
            formulario.save()
            #Autenticar usuario
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            #Para que el usuario quede logueado
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #Redirigir al index
            return redirect('index')
        else:
            data["form"] = formulario
    return render(request, 'registration/registro_usuario.html', data)




#VIEWS PARA EL CARRO DE COMPRA
#CARRITO HTML
def carrito(request):
    productos = Producto.objects.all()
    data = {
        'productosTienda': productos,
    }
    return render(request, "carrito.html", data)

#CARRITO HTML 2 
def carro2(request):
    productos = Producto.objects.all()
    data = {
        'productosTienda': productos,
    }
    return render(request, 'core/carro2.html',data)


#AGREGAR PRODUCTO AL CARRO
def agregar_products(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.agregar(producto)
    messages.success(request, "Producto agregado al carro")
    return redirect("tiendafor")

def agregar_productsCart(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.agregar2(producto)
    return redirect("carro")

#ELIMINAR PRODUCTO AL CARRO
def eliminar_products(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.eliminar(producto)
    return redirect("carro")

#RESTAR PRODUCTO AL CARRO
def restar_products(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.restar(producto)
    return redirect("carro")

#LIMPIAR PRODUCTOS DEL CARRO
def limpiar_carrito(request):
    cart = Cart(request)
    cart.limpiar()
    return redirect("carro")






#AGREGAR PRODUCTO AL WISHLIST
def agregar_productsW(request, producto_id):
    wish = Wishlist(request)
    producto = Producto.objects.get(id=producto_id)
    wish.agregarW(producto)
    messages.success(request, "Agregado a su Lista de Deseos")
    return redirect("tiendafor")

def agregar_productsWMVC(request, producto_id):
    wish = Wishlist(request)
    producto = Producto.objects.get(id=producto_id)
    wish.agregarW2(producto)
    return redirect("wishlist")

#ELIMINAR PRODUCTO AL WISHLIST
def eliminar_productsW(request, producto_id):
    wish = Wishlist(request)
    producto = Producto.objects.get(id=producto_id)
    wish.eliminarW(producto)
    return redirect("wishlist")

#RESTAR PRODUCTO AL WISHLIST
def restar_productsW(request, producto_id):
    wish = Wishlist(request)
    producto = Producto.objects.get(id=producto_id)
    wish.restarW(producto)
    return redirect("wishlist")

#LIMPIAR PRODUCTOS DEL WISHLIST
def limpiar_carritoW(request):
    wish = Wishlist(request)
    wish.limpiarW()
    return redirect("wishlist")





#AGREGAR PRODUCTO AL COMPARE
def agregar_productsC(request, producto_id):
    compare = Compare(request)
    producto = Producto.objects.get(id=producto_id)
    compare.agregarC(producto)
    messages.success(request, "Agregado al comparador")
    return redirect("tiendafor")

def agregar_productsCMVC(request, producto_id):
    compare = Compare(request)
    producto = Producto.objects.get(id=producto_id)
    compare.agregarC2(producto)
    return redirect("compare")

#ELIMINAR PRODUCTO AL COMPARE
def eliminar_productsC(request, producto_id):
    compare = Compare(request)
    producto = Producto.objects.get(id=producto_id)
    compare.eliminarC(producto)
    return redirect("compare")

#RESTAR PRODUCTO AL COMPARE
def restar_productsC(request, producto_id):
    compare = Compare(request)
    producto = Producto.objects.get(id=producto_id)
    compare.restarC(producto)
    return redirect("compare")

#LIMPIAR PRODUCTOS DEL COMPARE
def limpiar_carritoC(request):
    compare = Compare(request)
    compare.limpiarC()
    return redirect("compare")
