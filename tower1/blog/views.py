from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Anuncio
from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_authenticated and request.user.is_staff == 1:
        return render(request, 'blog/home.html')
    if request.user.is_authenticated:
        return render(request, 'blog/home.html')
    
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                #login manual
                do_login(request,user)
                #y se va a la portada
                if request.user.is_authenticated and request.user.is_staff == 1:
                    return redirect('home')
                return redirect('home')
    return render(request, 'blog/index.html', {'form':form})


def logout(request):
    #finaliza la sesion
    do_logout(request)
    #manda a la portada
    return redirect('/')

def home(request):
    if request.user.is_authenticated:
        
        #anuncios_admin = Anuncio.objects.all()[:3]
        anuncios_admin = Anuncio.objects.filter( tipo_usuario = "1" )[:3]
        anuncios_usuarios = Anuncio.objects.filter( tipo_usuario = "0" )[:3]

        
        return render(request, 'blog/home.html',{'anuncios_admin' : anuncios_admin, 'anuncios_usuarios' : anuncios_usuarios})
    return redirect('index')


def news(request):
    if request.user.is_authenticated:

        anuncios_admin = Anuncio.objects.filter( tipo_usuario = "1" )[:10]
        anuncios_admin2 = Anuncio.objects.filter( tipo_usuario = "1" )[11:]

        return render(request,'blog/news.html',{'anuncios_admin':anuncios_admin,'anuncios_admin2':anuncios_admin2})


    return redirect('index')

def news2(request):
    if request.user.is_authenticated :
        
        anuncios_usuarios = Anuncio.objects.filter( tipo_usuario = "0" )[:10]
        anuncios_usuarios2 = Anuncio.objects.filter( tipo_usuario = "0" )[11:]
    
        return render( request, 'blog/news2.html', {'anuncios_usuarios':anuncios_usuarios, 'anuncios_usuarios2':anuncios_usuarios2})
    
    return redirect('index')

def anuncio(request):
    ############ANUNCIO DE LA ADMINISTRACION###################3
    if request.user.is_authenticated and request.user.is_staff == 1:
        if request.POST:
            anuncio = Anuncio()

            anuncio.autor = request.user.username
            anuncio.titulo = request.POST.get('titulo')
            anuncio.contenido = request.POST.get('mensaje')
            anuncio.categoria = "null"
            anuncio.tipo_usuario = 1

            priori = request.POST.get('Prioridad')
            if priori == "Alta":
                anuncio.prioridad = 3
            if priori == "Media":
                anuncio.prioridad = 2
            if priori == "Baja":
                anuncio.prioridad = 1                


            try:
                anuncio.save()
                mensaje = "Enviado"
                messages.success(request, mensaje)
                return redirect('home')
            except:
                mensaje = "Error"
                messages.error(request, mensaje)

        return render(request,'blog/anuncio.html')

    #########ANUNCIO DE LA COMUNIDAD############################3
    if request.user.is_authenticated and request.user.is_staff == 0:
            anuncio = Anuncio()

            anuncio.autor = request.user.username
            anuncio.titulo = request.POST.get('titulo')
            anuncio.contenido = request.POST.get('mensaje')
            anuncio.categoria = request.POST.get('categoria')
            anuncio.tipo_usuario = 0
            anuncio.prioridad = 0
              


            try:
                anuncio.save()
                mensaje = "Enviado"
                messages.success(request, mensaje)
                return redirect('home')
            except:
                mensaje = "Error"
                messages.error(request, mensaje)
            
            return render(request,'blog/anuncio2.html')

    return redirect('index')


