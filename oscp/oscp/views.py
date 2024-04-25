from django.shortcuts import render,HttpResponse, redirect, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from product.models import Item, Order, OrderItem

class HomeView(ListView):
    model = Item
    template_name = 'index.html'

def signup(request):
     pass

def login(request):
     pass

def logOut(request):
    pass

@login_required
def profile(request):
    pass