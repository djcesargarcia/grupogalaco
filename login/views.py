from django.shortcuts import render
from .models import Login

# Create your views here.

def login(request):
    return render (request, 'login/index.html', {})

def login_signin(request):
    return render(request, 'login/signin.html',{})

def login_signout(request):
    return render(request, 'login/signout.html',{})

def login_signup(request):
    return render(request, 'login/signup.html',{})

