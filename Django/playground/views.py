from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    # Pull data from db
    # Transfrom data
    # Send emails
    # return HttpResponse("Hello World")
    # return render(request, 'hello.html')
    return render(request, 'hello.html', {'name' : 'Amandeep'})
