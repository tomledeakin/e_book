import json
from django.shortcuts import render
from django.http import JsonResponse
from customer.models import CustomerModel
from order.models import OrderModel
from order_detail.models import OrderDetailModel
from product.models import ProductModel
import uuid
from django.db.models import Sum
from home.models import PromotionModel
from customer.models import CustomerModel

# Create your views here.
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["itemId"]
    print(f"data: {data}")

    # customer
    customer = CustomerModel.objects.get(user=request.user)

    # order
    order, created = OrderModel.objects.get_or_create(
        status = 0,
        customer = customer
    )

    product = ProductModel.objects.get(id=product_id)

    # order detail
    try:
        order_detail = OrderDetailModel.objects.get(
            order = order,
            product = product
        )
    except OrderDetailModel.DoesNotExist:
        order_detail = OrderDetailModel(
            order = order,
            product = product,
            price = product.price,
            quantity = 0
        )
    order_detail.quantity = order_detail.quantity + 1 if order_detail.quantity else 1
    order_detail.price = product.price
    order_detail.save()

    return JsonResponse({"total": get_total_number_item_in_cart(customer)})


def cart(request):
    customer = CustomerModel.objects.get(user=request.user)
    order = OrderModel.objects.filter(
        status = 0,
        customer = customer
    ).first()

    order_detail = OrderDetailModel.objects.filter(order=order)
    promotion_list = PromotionModel.objects.all()

    try:
        customer1 = CustomerModel.objects.get(user=request.user)
    except CustomerModel.DoesNotExist:
        customer1 = None
    
    context = {
        'order': order,
        'order_detail': order_detail,    
        'cart': get_total_number_item_in_cart(customer),
        "promotion_list": promotion_list,
        'customer': customer1
    }
    return render(request, 'cart/cart.html', context)

def order(request, id):
    order = OrderModel.objects.get(id=id, status = 0)
    order.status = 1
    order.description = request.POST.get("description")
    order.order_number = str(uuid.uuid4())

    order_detail = OrderDetailModel.objects.filter(order=order)
    for item in order_detail:
        item.price = item.product.price
        item.save()

    order.save()

    context = {
        'order': order
    }
    return render(request, 'cart/order.html', context)

def get_total_number_item_in_cart(customer):
    order = OrderModel.objects.filter(
        status = 0,
        customer = customer
    ).first()
    total_items = OrderDetailModel.objects.filter(order=order).aggregate(Sum('quantity'))
    total_items = list(total_items.values())[0]
    return total_items
