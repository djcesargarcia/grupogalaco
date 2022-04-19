from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Login
from .forms import LoginForm
from django.contrib import messages

# Create your views here.

# Create your views here.

def login(request):
    print("Your account has been created.")
    return render (request, 'login/index.html', {})

def log_in(request):
    return render(request, 'login/log_in.html',{})

def log_out(request):
    return render(request, 'login/log_out.html',{})

def sign_up(request):
    form = LoginForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your account has been created.')
        return redirect('log_in')
    return render(request, 'login/sign_up.html',{'form':form})

