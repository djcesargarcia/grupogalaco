from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Login
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def login(request):
    print("Your account has been created.")
    return render (request, 'login/index.html', {})

def log_in(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('login/log_in')
            return HttpResponse('<h1>You are logged in</h1>')
        return render(request, "login/log_in.html", {'form': form})
    return render(request, "login/log_in.html", {'form': form})
    
    
def log_out(request):
    return render(request, 'login/log_out.html',{})

def sign_up(request):
    form = LoginForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your account has been created.')
        return redirect('log_in')
    return render(request, 'login/sign_up.html',{'form':form})

def log_error(request):
    return render(request, 'login/log_error.html',{})




    