from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    deliverd = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders': orders, 'customers': customers, 'total_customers':total_customers,
    'total_orders':total_orders,'deliverd':deliverd, 'pending':pending

    }
    return render(request, 'product/home.html', context)

def products(request):
    products = product.objects.all()
    context = {'products': products }
    return render(request, 'product/product.html', context)
def customers(request, pk):
    Customers = customer.objects.get(id=pk)
    orders = Customers.order_set.all()
    order_count = orders.count()

    context = { 'Customers': Customers, 'orders':orders, 'order_count':order_count }
    return render(request, 'product/customer.html', context)
