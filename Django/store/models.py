from django.db import models

# Create your models here.
class Product(models.Model): # Base class which is used for making database table (models.Model)
    title = models.CharField(max_length = 255)
    description = models.TextField()

    #9999.99 -> Max price 
    price = models.DecimalField(max_digits = 6, decimal_places = 2) # These two parameters are always required for the decimal field

    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True) # Everytime we update a new product, Django will automatically stores the current datetime in this field (auto_now = True)
    # auto_now_add = True, It only stores when we create the product object first time

class Customer(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 255)
    birth_date = models.DateField(null = True)