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
    pass
    
class MerchantItem(models.Model):
    pass

class Order(models.Model):
    pass

class OrderItem(models.Model):
    pass

