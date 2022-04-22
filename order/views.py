from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def orders(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        orders = Order.objects.filter(name__icontains=qtext)
    else: 
        orders = Order.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(orders, 5)
        try:
            orders = paginator.page(page)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)
    return render(request, 'orders/index.html', {'orders':orders})
    

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
