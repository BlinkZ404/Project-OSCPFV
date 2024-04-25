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
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    variant = models.CharField(max_length=20, null=True)
    details = models.TextField(max_length=500, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    image = models.ImageField(default='default.jpg', upload_to='static/images')
    slug = models.SlugField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product:product-page", kwargs={
                       'slug': self.slug
                       })

    def get_add_to_cart_url(self):
        return reverse("product:cart-page", kwargs={
            'slug': self.slug
        })

    def img_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="100" height="100" />')
    img_tag.short_description = 'Image'

class Merchant(models.Model):
    name = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='static/images')
    def __str__(self):
        return self.name

    def img_tag(self):
        return mark_safe(f'<img src="{self.logo.url}" width="60" height="50" />')
    img_tag.short_description = 'Image'
    
class MerchantItem(models.Model):
    merchant = models.ForeignKey(Merchant,on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rating = models.IntegerField()
    stock = models.CharField(choices=STOCK_CHOICES, max_length=15, default=STOCK_CHOICES)
    shipping = models.CharField(max_length=100, null=True)
    warranty = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.item.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(null=True, default=timezone.now)
    address = models.CharField(max_length=500,null=True)
    phone = models.CharField(max_length=20,null=True)
    payment_info = models.CharField(max_length=20, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default='Pending')
    note = models.CharField(max_length=250,null=True)


    def __str__(self):
        return self.status

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(MerchantItem, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=1)

