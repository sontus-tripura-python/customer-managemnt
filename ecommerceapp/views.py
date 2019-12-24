from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import *
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    deliverd = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'total_customers':total_customers,
    'total_orders':total_orders,'deliverd':deliverd, 'pending':pending,

    }
    return render(request, 'product/home.html', context)

def products(request):
    products = product.objects.all()
    context = {'products': products }
    return render(request, 'product/product.html', context)


def UpdateForm(request, pk):
    order = Order.objects.get(id=pk)
    uform = OrderForm(instance=order)
    if request.method =='POST':
        uform = OrderForm(request.POST, instance=order)
        if uform.is_valid():
            uform.save()
            return redirect('/')
    context = { 'uform': uform }
    return render(request, 'product/updateform.html', context)

def deleteForm(request, pk):
    order = Order.objects.get(id=pk)
    if request.method =='POST':
        order.delete()
        return redirect('/')
    context = { 'D_form': order }
    return render(request, 'product/deleteform.html', context)

def customers(request, pk):
    OrderFormSet = inlineformset_factory(customer, Order, fields=('product', 'status'))
    Customers = customer.objects.get(id=pk)
    formset = OrderFormSet(instance=Customers)
    orders = Customers.order_set.all()
    order_count = orders.count()
    #orderform = OrderForm(initial={'customer':Customers })
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=Customers)
        #orderform = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = { 'Customers': Customers, 'orders':orders, 'order_count':order_count, 'formset': formset}
    return render(request, 'product/customer.html', context)
