from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dock
from .forms import DockForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

@login_required
def docks(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        docks = Dock.objects.filter(name__icontains=qtext)
    else: 
        docks = Dock.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(docks, 5)
        try:
            docks = paginator.page(page)
        except EmptyPage:
            docks = paginator.page(paginator.num_pages)
    return render(request, 'docks/index.html', {'docks':docks})

@login_required
def create_docks(request):
    form = DockForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('docks')
    return render(request, 'docks/create.html',{'form':form})

@login_required
def edit_docks(request, id):
    dock = Dock.objects.get(id=id)
    form = DockForm(request.POST or None, request.FILES or None, instance=dock)
    if form.is_valid and request.POST:
        form.save()
        return redirect('docks')
    return render(request,'docks/edit.html',{'form':form})

@login_required
def delete_docks(request, id):
    dock = Dock.objects.get(id=id)
    dock.delete()
    return redirect('docks')