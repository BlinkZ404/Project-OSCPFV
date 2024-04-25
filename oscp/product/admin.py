from django.contrib import admin
from .models import Item, Order, OrderItem, Merchant,MerchantItem

class ItemAdmin(admin.ModelAdmin):
    pass

class MerchantItemAdmin(admin.ModelAdmin):
    pass

class OrderItemAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    pass

class MerchantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(MerchantItem, MerchantItemAdmin)

