from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def tmsapp(request):
    return render(request, 'tmsapp/inicio.html', {})

@login_required
def home(request):
    return render(request, 'tmsapp/home.html', {})

@login_required
def routes(request):
    return render(request, 'routes/index.html',{})

