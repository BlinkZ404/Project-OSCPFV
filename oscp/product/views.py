from django.shortcuts import render, redirect
from django.views.generic import DetailView
from product.models import Item, Order, OrderItem, Merchant, MerchantItem
from django.contrib.auth.decorators import login_required
import json

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Item.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['merchant_list'] = MerchantItem.objects.filter(item=self.object)
        return context


@login_required(login_url='login-page')
def checkout(request,order):
    pass




@login_required(login_url='login-page')
def CartView(request):
    pass


