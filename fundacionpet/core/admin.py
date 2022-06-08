from django.contrib import admin
from .models import Marca, Producto, Contacto1

# Register your models here.

#Para modificar las COLUMNAS del ADMIN DJANGO
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "precio_oferta", "stock", "descripcion", "nuevo", "marca"]
    list_editable = ["precio", "precio_oferta", "stock"]
    #search_fields = ["marca"]
    list_filter = ["marca"]
    list_per_page = 2


admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto1)