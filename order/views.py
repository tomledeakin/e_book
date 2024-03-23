from django.shortcuts import render
from .models import OrderModel
from django.views.generic import ListView, DetailView
from home.models import PromotionModel
from customer.models import CustomerModel
from order_detail.models import OrderDetailModel
# Create your views here.
def order_list(request):
    customer = CustomerModel.objects.get(user = request.user)
    order_list = OrderModel.objects.filter(customer=customer)
    
    context = {
        "order_list": order_list,
        "customer": customer
    }
    return render(request, 'order/list.html', context)

def order_detail(request,id):
    order = OrderModel.objects.get(id=id)
    order_detail = OrderDetailModel.objects.filter(order=order)
    
 

    
    context = {
        "order_detail": order_detail
    }
    return render(request, 'order/detail.html', context)











