from django.shortcuts import render
from models import Routes

# Create your views here.

def routes(request):
    return render(request, 'routes/index.html', {})

