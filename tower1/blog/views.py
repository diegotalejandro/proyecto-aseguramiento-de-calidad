from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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
            

def home(request):
    if request.user.is_authenticated:
        return render(request, 'blog/home.html')
    return render(request, 'blog/index.html')
    