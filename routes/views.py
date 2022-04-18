from django.shortcuts import render
from models import Routes
from .models import Driver
from .forms import DriverForm

# Create your views here.

def routes(request):
    routes = Routes.objects.all()
    return render(request, 'routes/index.html', {'routes':routes})
