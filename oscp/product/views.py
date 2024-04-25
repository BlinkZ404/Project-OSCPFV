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
    if request.POST:
        bkash=request.POST['bkash']
        nagad=request.POST['nagad']
        order=Order.objects.get(id=order)
        if bkash==None and nagad==None:
            order.payment_info= 'Cash on Delivery'
        elif bkash ==None:
            order.payment_info= f'Nagad:{nagad}'
        else:
            order.payment_info= f'Bkash:{bkash}'
        order.save()
        return redirect('/')

    order=Order.objects.get(id=order)
    orderitem=OrderItem.objects.filter(order=order)
    item=[]
    total=0
    for i in orderitem:
        # print(i.item.price)
        price=int(i.item.price) * int(i.quantity)
        dic={
            'item':i.item.item,
            'price': price,
        }
        total+=price
        item.append(dic)
    response = render(request, 'checkout.html', {'order':order,'items':item,'total':total})
    response.delete_cookie('products')
    return response




@login_required(login_url='login-page')
def CartView(request):
    pass


