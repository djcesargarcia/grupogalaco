from django.shortcuts import render


# Create your views here.

def tmsapp(request):
    return render(request, 'tmsapp/inicio.html', {})

def home(request):
    return render(request, 'tmsapp/home.html', {})

def routes(request):
    return render(request, 'routes/index.html',{})

