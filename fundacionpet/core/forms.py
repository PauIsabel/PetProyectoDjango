from dataclasses import fields
from pickle import TRUE
from pyexpat import model
from tabnanny import verbose
from django import forms
from .models import Contacto1, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Formulario Contacto1
class Contacto1Form(forms.ModelForm):
    #Validando los campos
    nombre = forms.CharField(min_length=3, max_length=50)

    class Meta:
        model = Contacto1
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

#Formulario para agregar producto
class ProductoForm(forms.ModelForm):

    #Validando los campos
    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1000, max_value=1200000)
    precio_oferta = forms.IntegerField(min_value=0, max_value=1500000)
    stock = forms.IntegerField(min_value=1, max_value=300)
    nuevo = forms.BooleanField(required=False)

    class Meta:
        model = Producto
        fields = '__all__'
    
        #Para las fechas de agregar producto
        # widgets = {
        #     "fecha_fabricacion": forms.SelectDateWidget()
        # }

#Formulario Registro Usuario -> Para validar sus campos
class RegistroUserCreationForm(UserCreationForm):

    #Validando los campos
    first_name = forms.CharField(min_length=3, max_length=50,label="Nombre") 
    last_name = forms.CharField(min_length=3, max_length=50,label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
