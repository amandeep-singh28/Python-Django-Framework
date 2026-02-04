from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F # Q means query(It returns query expression or a piece of code that produce a value)
from store.models import Product, OrderItem, Order

def say_hello(request):
    queryset = Order.objects.select_related('customer').order_by('placed_at')[:5]


    return render(request, 'hello.html', {'name' : 'Amandeep', 'orders' : list(queryset)})
    
