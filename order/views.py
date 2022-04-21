from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders/index.html', {'orders': orders})

@login_required
def create_orders(request):
    form = OrderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('orders')
    return render(request, 'orders/create.html',{'form':form})

@login_required
def edit_orders(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(request.POST or None, request.FILES or None, instance=order)
    if form.is_valid and request.POST:
        form.save()
        return redirect('orders')
    return render(request,'orders/edit.html',{'form':form})

@login_required
def delete_orders(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('orders')
