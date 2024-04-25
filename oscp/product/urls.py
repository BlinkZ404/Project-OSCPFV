from django.urls import path
from .views import ItemDetailView, checkout, CartView

app_name = 'product'

urlpatterns = [
    path('product/<slug>/', ItemDetailView.as_view(), name='product-page'),
    path('checkout/<order>', checkout, name='checkout-page'),
    path('cart/', CartView, name='cart-page')
    ]