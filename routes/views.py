from django.shortcuts import render, redirect
from .models import Routes
from .forms import RoutesForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def routes(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        routes = Routes.objects.filter(name__icontains=qtext)
    else: 
        routes = Routes.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(routes, 5)
        try:
            routes = paginator.page(page)
        except EmptyPage:
            routes = paginator.page(paginator.num_pages)
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