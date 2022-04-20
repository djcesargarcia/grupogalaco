from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html',{'customers': customers})

@login_required
def create_customers(request):
    form = CustomerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('customers')
    return render(request, 'customers/create.html',{'form':form})

@login_required
def edit_customers(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST or None, request.FILES or None, instance=customer)
    if form.is_valid and request.POST:
        form.save()
        return redirect('customers')
    return render(request,'customers/edit.html',{'form':form})

@login_required
def delete_customers(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('drivers')