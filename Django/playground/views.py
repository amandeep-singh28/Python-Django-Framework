from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F # Q means query(It returns query expression or a piece of code that produce a value)
from django.db.models.aggregates import Count, Min, Max, Sum, Avg
from django.db.models import Value
from django.db.models import Func
from django.db.models.functions import Concat
from django.db.models import ExpressionWrapper, DecimalField
from store.models import Product, OrderItem, Order, Customer

def say_hello(request):
    
    queryset = Product.objects.annotate(
        # discounted_price = ExpressionWrapper(F('unit_price') * 0.82, output_field = DecimalField())
        discounted_price = F('unit_price') * 0.82
    )

    return render(request, 'hello.html', {'name' : 'Amandeep', 'result' : list(queryset)})
    
