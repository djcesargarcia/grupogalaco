from django.shortcuts import render

# Create your views here.

def tmsapp(request):
    return render(request, 'tmsapp/inicio.html', {})
