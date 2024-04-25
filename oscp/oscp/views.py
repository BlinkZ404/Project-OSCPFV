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
    if not request.user.is_authenticated:
        if request.method== 'POST':
            username = request.POST.get('nameInput')
            email = request.POST.get('emailInput')
            password = request.POST.get('passwordInput')
            pass2 = request.POST.get('passwordInput1')
            if password != pass2:
                return render(request, 'signup.html', {'error': "Mismatched Passwords"})
            else:
                my_user = User.objects.create_user(username, email, password)
                my_user.save()
                return redirect('login-page')

        return render(request, 'signup.html')
    else:
        return redirect('/')

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('nameInput')
            password = request.POST.get('passwordInput')
            print(username,password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home-page')
            else:
                return render(request, 'login.html', {'error': 'Invalid Email or Password'})

        return render(request, 'login.html')
    else:
        return redirect('/')


def logOut(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login-page')

@login_required
def profile(request):
    pass