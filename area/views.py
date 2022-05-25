from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Area
from .forms import AreaForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def areas(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        areas = Area.objects.filter(name__icontains=qtext)
    else: 
        areas = Area.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(areas, 5)
        try:
            areas = paginator.page(page)
        except EmptyPage:
            areas = paginator.page(paginator.num_pages)
    return render(request, 'areas/index.html', {'areas':areas})

@login_required
def create_areas(request):
    form = AreaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('areas')
    return render(request, 'areas/create.html',{'form':form})

@login_required
def edit_areas(request, id):
    area = Area.objects.get(id=id)
    form = AreaForm(request.POST or None, request.FILES or None, instance=area)
    if form.is_valid and request.POST:
        form.save()
        return redirect('areas')
    return render(request,'areas/edit.html',{'form':form})

@login_required
def delete_areas(request, id):
    area = Area.objects.get(id=id)
    area.delete()
    return redirect('areas')