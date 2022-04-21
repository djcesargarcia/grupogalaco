from django.shortcuts import  render, redirect
from .forms import LoginForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import Login

# Create your views here.

def login(request):
    return render (request, 'login/index.html', {})

        
def logout(request):
    logout(request)
    return render(request, 'login/index.html', {})




