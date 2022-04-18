from django.shortcuts import render, redirect
from .models import Routes
from .forms import RoutesForm

# Create your views here.

def routes(request):
    routes = Routes.objects.all()
    return render(request, 'routes/index.html', {'routes':routes})

def create_routes(request):
    form = RoutesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('routes')
    return render(request, 'routes/create.html',{'form':form})

def edit_routes(request, id):
    route = Routes.objects.get(id=id)
    form = RoutesForm(request.POST or None, request.FILES or None, instance=route)
    if form.is_valid and request.POST:
        form.save()
        return redirect('routes')
    return render(request,'routes/edit.html',{'form':form})

def delete_routes(request, id):
    route = Routes.objects.get(id=id)
    route.delete()
    return redirect('routes')