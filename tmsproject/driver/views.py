from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Driver
from .forms import DriverForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    return render(request, 'pages/inicio.html')

@login_required
def nosotros(request):
    return render(request, 'pages/nosotros.html')

@login_required
def drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/index.html',{'drivers': drivers})

def create_drivers(request):
    form = DriverForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('drivers')
    return render(request, 'drivers/create.html',{'form':form})

def edit_drivers(request, id):
    driver = Driver.objects.get(id=id)
    form = DriverForm(request.POST or None, request.FILES or None, instance=driver)
    if form.is_valid and request.POST:
        form.save()
        return redirect('drivers')
    return render(request,'drivers/edit.html',{'form':form})

def delete_drivers(request, id):
    driver = Driver.objects.get(id=id)
    driver.delete()
    return redirect('drivers')

