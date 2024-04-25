from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.shortcuts import reverse
from django.utils import timezone

CATEGORY_CHOICES = (
    ('S', 'Smartphone'),
    ('C', 'Computer'),
    ('SW', 'SmartWatch'),
    ('CA', 'Camera'),
    ('H', 'Headphone')
)

STOCK_CHOICES = (
    ('In-Stock', 'In-Stock'),
    ('Pre-Order', 'Pre-Order'),
    ('Out-of-Stock', 'Out-of-Stock')
)

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Ready to Ship', 'Ready to Ship'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled')
)
class Item(models.Model):
    pass

class Merchant(models.Model):
    pass
    
class MerchantItem(models.Model):
    pass

class Order(models.Model):
    pass

class OrderItem(models.Model):
    pass

