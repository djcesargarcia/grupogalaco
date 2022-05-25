from django.shortcuts import render, redirect
from .models import Zone
from .forms import ZoneForm 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def zones(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        zones = Zone.objects.filter(name__icontains=qtext)
    else: 
        zones = Zone.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(zones, 5)
        try:
            zones = paginator.page(page)
        except EmptyPage:
            zones = paginator.page(paginator.num_pages)
    return render(request, 'zones/index.html', {'zones':zones})
    

@login_required
def create_zones(request):
    form = ZoneForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('zones')
    return render(request, 'zones/create.html',{'form':form})

@login_required
def edit_zones(request, id):
    zone = Zone.objects.get(id=id)
    form = ZoneForm(request.POST or None, request.FILES or None, instance=zone)
    if form.is_valid and request.POST:
        form.save()
        return redirect('zones')
    return render(request,'zones/edit.html',{'form':form})

@login_required
def delete_zones(request, id):
    order = Zone.objects.get(id=id)
    order.delete()
    return redirect('zones')
