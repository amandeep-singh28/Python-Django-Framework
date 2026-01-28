from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length = 255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length = 255)
    featured_product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True, related_name = '+')

class Product(models.Model): # Base class which is used for making database table (models.Model)
    title = models.CharField(max_length = 255)
    description = models.TextField()

    #9999.99 -> Max price 
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2) # These two parameters are always required for the decimal field

    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True) # Everytime we update a new product, Django will automatically stores the current datetime in this field (auto_now = True)
    # auto_now_add = True, It only stores when we create the product object first time
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT) # Because if by mistake collection is deleted, so we might not end up deleting PRODUCTS too
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 255)
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length = 1, choices = PAYMENT_STATUS_CHOICES, default = PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete = models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.PROTECT)
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField() # To prevent negative values
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)

class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    # customer = models.OneToOneField(Customer, on_delete = models.CASCADE, primary_key = True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
