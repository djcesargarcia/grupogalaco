from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def vehicles(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        vehicles = Vehicle.objects.filter(brand__icontains=qtext)
    else: 
        vehicles = Vehicle.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(vehicles, 5)
        try:
            vehicles = paginator.page(page)
        except EmptyPage:
            vehicles = paginator.page(paginator.num_pages)
    return render(request, 'vehicles/index.html', {'vehicles':vehicles})

@login_required
def create_vehicles(request):
    form = VehicleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('vehicles')
    return render(request, 'vehicles/create.html',{'form':form})

@login_required
def edit_vehicles(request, id):
    vehicle = Vehicle.objects.get(id=id)
    form = VehicleForm(request.POST or None, request.FILES or None, instance=vehicle)
    if form.is_valid and request.POST:
        form.save()
        return redirect('vehicles')
    return render(request,'vehicles/edit.html',{'form':form})

@login_required
def delete_vehicles(request, id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle.delete()
    return redirect('vehicles')