from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import LoadLorry
from .forms import LoadLorryForm
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
def loadlorries(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        loadlorries = LoadLorry.objects.filter(name__icontains=qtext)
    else: 
        loadlorries = LoadLorry.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(loadlorries, 5)
        try:
            loadlorries = paginator.page(page)
        except EmptyPage:
            loadlorries = paginator.page(paginator.num_pages)
    return render(request, 'loadlorries/index.html', {'loadlorries':loadlorries})

@login_required
def create_loadlorries(request):
    form = LoadLorryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('loadlorries')
    return render(request, 'loadlorries/create.html',{'form':form})

@login_required
def edit_loadlorries(request, id):
    loadlorry = LoadLorry.objects.get(id=id)
    form = LoadLorryForm(request.POST or None, request.FILES or None, instance=loadlorry)
    if form.is_valid and request.POST:
        form.save()
        return redirect('loadlorries')
    return render(request,'loadlorries/edit.html',{'form':form})

@login_required
def delete_loadlorries(request, id):
    loadlorry = LoadLorry.objects.get(id=id)
    loadlorry.delete()
    return redirect('loadlorries')