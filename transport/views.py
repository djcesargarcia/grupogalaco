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
    return render(request, 'drivers/create.html')

def edit(request):
    return render(request, 'drivers/edit.html')

def form(request):
    return render(request, 'drivers/form.html')

#Path for Home.

def home(request):
    return render(request, 'home/index.html')

#Path for Routes.

def routes(request):
    return render(request, 'routes/index.html')

def create(request):
    return render(request, 'routes/create.html')

def edit(request):
    return render(request, 'routes/edit.html')

def form(request):
    return render(request, 'routes/form.html')

#Path for Customers.

def customers(request):
    return render(request, 'customers/index.html')

def create(request):
    return render(request, 'customers/create.html')

def edit(request):
    return render(request, 'customers/edit.html')

def form(request):
    return render(request, 'customers/form.html')

#Path for Users.

def users(request):
    return render(request, 'users/index.html')

def create(request):
    return render(request, 'users/create.html')

def edit(request):
    return render(request, 'users/edit.html')

def form(request):
    return render(request, 'users/form.html')

#Path for Warehouses.

def warehouses(request):
    return render(request, 'warehouses/index.html')


