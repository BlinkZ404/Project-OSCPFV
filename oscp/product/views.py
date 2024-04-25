from django.shortcuts import render, redirect
from django.views.generic import DetailView
from product.models import Item, Order, OrderItem, Merchant, MerchantItem
from django.contrib.auth.decorators import login_required
import json

class ItemDetailView(DetailView):
    pass


@login_required(login_url='login-page')
def checkout(request,order):
    pass




@login_required(login_url='login-page')
def CartView(request):
    pass


