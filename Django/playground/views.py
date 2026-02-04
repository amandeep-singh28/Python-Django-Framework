from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F # Q means query(It returns query expression or a piece of code that produce a value)
from django.db.models.aggregates import Count, Min, Max, Sum, Avg
from store.models import Product, OrderItem, Order

def say_hello(request):
    # result = Product.objects.aggregate(Count('id'))
    result = Product.objects.aggregate(count = Count('id'), min_price = (Min('unit_price')))


    return render(request, 'hello.html', {'name' : 'Amandeep', 'result' : result})
    
