from django.shortcuts import render

# Create your views here.

def distance(request):
     return render(request, 'distance/index.html', {})
