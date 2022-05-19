from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from numpy import VisibleDeprecationWarning
from .models import Driver
from .forms import DriverForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
# Create your views here.

@login_required
def inicio(request):
    return render(request, 'pages/inicio.html')

@login_required
def nosotros(request):
    return render(request, 'pages/nosotros.html')

@login_required
def drivers(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        drivers = Driver.objects.filter(name__icontains=qtext)
    else: 
        drivers = Driver.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(drivers, 5)
        try:
            drivers = paginator.page(page)
        except EmptyPage:
            drivers = paginator.page(paginator.num_pages)
    return render(request, 'drivers/index.html', {'drivers':drivers})

@login_required
def create_drivers(request):
    form = DriverForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('drivers')
    return render(request, 'drivers/create.html',{'form':form})

@login_required
def edit_drivers(request, id):
    driver = Driver.objects.get(id=id)
    form = DriverForm(request.POST or None, request.FILES or None, instance=driver)
    if form.is_valid and request.POST:
        form.save()
        return redirect('drivers')
    return render(request,'drivers/edit.html',{'form':form})

@login_required
def delete_drivers(request, id):
    driver = Driver.objects.get(id=id)
    driver.delete()
    return redirect('drivers')



    
    


