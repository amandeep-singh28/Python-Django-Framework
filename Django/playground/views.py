from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.

# def calculate():
#     x = 1
#     y = 2
#     return x

def say_hello(request):
    # x = calculate()
    # x = 1
    # y = 2
    # Pull data from db
    # Transfrom data
    # Send emails
    # return HttpResponse("Hello World")
    # return render(request, 'hello.html')
    query_set = Product.objects.all() # For pulling out all the objects in the products table
    # for data in query_set:
    #     print(data)

    # list(query_set)

    # query_set[0:5]
    return render(request, 'hello.html', {'name' : 'Amandeep'})
