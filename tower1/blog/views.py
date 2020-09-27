from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Anuncio

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

        anuncios_admin = Anuncio.objects.filter( tipo_usuario = "1" )[:20]
        anuncios_admin2 = Anuncio.objects.filter( tipo_usuario = "1" )[21:]

        return render(request,'blog/news.html',{'anuncios_admin':anuncios_admin,'anuncios_admin2':anuncios_admin2})


    return redirect('index')
