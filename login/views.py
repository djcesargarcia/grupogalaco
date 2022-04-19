from django.shortcuts import  render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Login



# Create your views here.

def login(request):
    print("Your account has been created.")
    return render (request, 'login/index.html', {})

def log_in(request):
    username = request.methodPOST
    password = request.POST.get['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect("inicio")
    else:
        messages.error("Your credentials are not valid.")
        return redirect(request, 'login/log_error.html',{})
        

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




