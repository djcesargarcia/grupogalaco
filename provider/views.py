from django.shortcuts import render, redirect
from .models import Provider
from .forms import ProviderForm 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def providers(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        providers = Provider.objects.filter(name__icontains=qtext)
    else: 
        providers = Provider.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(providers, 5)
        try:
            providers = paginator.page(page)
        except EmptyPage:
            providers = paginator.page(paginator.num_pages)
    return render(request, 'provider/index.html', {'providers':providers})

@login_required
def create_providers(request):
    form = ProviderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('provider')
    return render(request, 'provider/create.html',{'form':form})

@login_required
def edit_providers(request, id):
    providers = Provider.objects.get(id=id)
    form = ProviderForm(request.POST or None, request.FILES or None, instance=providers)
    if form.is_valid and request.POST:
        form.save()
        return redirect('provider')
    return render(request,'provider/edit.html',{'form':form})

@login_required
def delete_providers(request, id):
    provider = Provider.objects.get(id=id)
    provider.delete()
    return redirect('provider')
