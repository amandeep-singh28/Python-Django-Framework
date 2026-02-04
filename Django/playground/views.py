from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F # Q means query(It returns query expression or a piece of code that produce a value)
from store.models import Product, OrderItem

def say_hello(request):
    queryset = Product.objects.select_related('collection').all()


    return render(request, 'hello.html', {'name' : 'Amandeep', 'products' : list(queryset)})
    
