from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.

#Path App.

def index(request):
    return render(request,'transport/index.html')

#Path Drivers.

def drivers(request):
    return render(request, 'drivers/index.html')

def create(request):
    return render(request,'drivers/crear.html')

def edit(request):
    return render(request, 'drivers/editar')

#Path for Home.

def home(request):
    return render(request, 'home/index.html')

#Path for Routes.

def routes(request):
    return render(request, 'routes/index.html')

#Path for Customers.

def customers(request):
    return render(request, 'customers/index.html')

#Path for Users.




