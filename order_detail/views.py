from django.shortcuts import render
from home.models import PromotionModel
from .models import OrderDetailModel
from order.models import OrderModel
# Create your views here.


def order_detail(request):
    order = OrderModel.objects.all()
    order_detail = OrderDetailModel.objects.get(order = order)
    
    
    context = {
        "order_detail": order_detail
    }
    return render(request, 'order/detail.html', context)
