from django.shortcuts import render, redirect
from .models import Routes
from .forms import RoutesForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def routes(request):
    routes = Routes.objects.all()
    return render(request, 'routes/index.html', {'routes':routes})

@login_required
def create_routes(request):
    form = RoutesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('routes')
    return render(request, 'routes/create.html',{'form':form})

@login_required
def edit_routes(request, id):
    route = Routes.objects.get(id=id)
    form = RoutesForm(request.POST or None, request.FILES or None, instance=route)
    if form.is_valid and request.POST:
        form.save()
        return redirect('routes')
    return render(request,'routes/edit.html',{'form':form})

@login_required
def delete_routes(request, id):
    route = Routes.objects.get(id=id)
    route.delete()
    return redirect('routes')