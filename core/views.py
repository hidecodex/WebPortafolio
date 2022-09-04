from core.models import Componente, Producto
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages


# Paginas del menu.
def home (request):
    Productos = Producto.objects.all()
    data = {"Productos":Productos}
    return render(request, 'home.html', data)

def departamentos (request):
    componente = Componente.objects.get(Nombre='departamentos')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'departamentos.html', data)
def hoteles (request):
    componente = Componente.objects.get(Nombre='hoteles')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'hoteles.html', data)
def resorts (request):
    componente = Componente.objects.get(Nombre='resorts')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'resorts.html', data)
def villas (request):
    componente = Componente.objects.get(Nombre='villas')
    Productos = Producto.objects.filter(Componente=componente)
    data = {"Productos":Productos}
    return render(request, 'villas.html', data)
def admin (request):
    Productos = Producto.objects.all()
    data = {"Productos":Productos}
    return render(request, 'admin.html', data)

def SignIn(request):
    contexto = {}
    return render(request, 'signin.html', contexto)

def SignUp(request):
    return render(request,'registro.html')

def Registros(request):
    username = request.POST.get('usuario','')
    email = request.POST.get('correo','')
    password1 = request.POST.get('clave','')
    usuario = User.objects.create_user(username, email, password1)
    usuario.save()
    return redirect('index')


def Logeando(request):
    username = request.POST.get('usuario','')
    password = request.POST.get('clave', '')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return redirect('index')
    else:
        return redirect('SignIn')
def Deslogeo(request):
    logout(request)
    return redirect('index')

