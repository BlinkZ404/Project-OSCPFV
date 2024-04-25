from django.contrib import admin
from .models import Item, Order, OrderItem, Merchant,MerchantItem

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = [
        'title',
        'img_tag',
        'price',
        'category',
        'slug',
        'details'
    ]

class MerchantItemAdmin(admin.ModelAdmin):
    list_display = [
        'merchant',
        'item',
        'rating',
        'stock',
        'shipping',
        'warranty',
        'price'
    ]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'item',
        'order',
        'quantity'
    ]

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_date',
        'user',
        'phone',
        'address',
        'payment_info',
        'status'
    ]

class MerchantAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'img_tag'
    ]


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(MerchantItem, MerchantItemAdmin)

