from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q # Q means query(It returns query expression or a piece of code that produce a value)
from store.models import Product

def say_hello(request):
    queryset = Product.objects.filter(Q(inventory__lt = 100) & ~Q(unit_price__lt = 700.00))

    return render(request, 'hello.html', {'name' : 'Amandeep', 'products' : list(queryset)})
