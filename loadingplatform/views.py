from re import L
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LoadingPlatform
from .forms import LoadingPlatformForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def loadingplatforms(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        areas = LoadingPlatform.objects.filter(name__icontains=qtext)
    else: 
        loadingplatforms = LoadingPlatform.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(areas, 5)
        try:
            loadingplatforms = paginator.page(page)
        except EmptyPage:
            loadingplatforms = paginator.page(paginator.num_pages)
    return render(request, 'loadingplatforms/index.html', {'loadingplatforms':loadingplatforms})

@login_required
def create_loadingplatforms(request):
    form = LoadingPlatformForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('loadingplatforms')
    return render(request, 'loadingplatforms/create.html',{'form':form})

@login_required
def edit_loadingplatforms(request, id):
    loadingplatform = LoadingPlatform.objects.get(id=id)
    form = LoadingPlatformForm(request.POST or None, request.FILES or None, instance=loadingplatform)
    if form.is_valid and request.POST:
        form.save()
        return redirect('loadingplatforms')
    return render(request,'loadingplatforms/edit.html',{'form':form})

@login_required
def delete_areas(request, id):
    area = LoadingPlatform.objects.get(id=id)
    area.delete()
    return redirect('loadingplatforms')