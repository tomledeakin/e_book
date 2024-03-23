from django.shortcuts import render, HttpResponse, redirect
from .models import ProductModel
from .forms import ProductForm, ProductModelForm
from django.db.models import Q
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.conf import settings
from author.models import AuthorModel
from home.models import PromotionModel
from home.models import PromotionModel
from customer.models import CustomerModel
# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def product_list(request):

    # limit
    limit = request.GET.get("limit")
    if limit and limit.isnumeric():
        limit = int(limit)
    else:
        limit = settings.DEFAULT_LIMIT
    
    page = request.GET.get("page", 1)

    product_list = []
    sort = request.GET.get("sort")
    if sort not in ["-created_at", "created_at", "product_name"]:
        sort = settings.DEFAULT_SORT

    keyword = request.GET.get("keyword")

    if keyword:
        product_list = ProductModel.objects.filter(
            Q(product_name__contains=keyword) 
            | Q(summary__contains=keyword)
            | Q(description__contains=keyword)
        )
    else:
        product_list = ProductModel.objects.all()
    
    product_list = product_list.order_by(sort)

    # product_list = product_list[:limit]
    # paginator
    product_list_paging = Paginator(product_list, limit)
    range_pages = range(1, product_list_paging.num_pages + 1)
    try:
        product_list_paging = product_list_paging.get_page(page)
    except PageNotAnInteger:
        product_list_paging = product_list_paging.get_page(1)
    except EmptyPage:
        product_list_paging = product_list_paging.get_page(product_list_paging.num_pages)


    promotion_list = PromotionModel.objects.all()


    # check if it is author
    try:
        author = AuthorModel.objects.get(user=request.user)
    except AuthorModel.DoesNotExist:
        author = None
        

    context = {
        "product_list": product_list_paging,
        "keyword": keyword if keyword else "",
        "range_pages": range_pages,
        "promotion_list": promotion_list,
        "author": author,
    }
    return render(request, 'product/list.html', context)

def product_detail(request, id):
    product = ProductModel.objects.get(id=id)
    # check if it is author
    try:
        author = AuthorModel.objects.get(user=request.user)
    except AuthorModel.DoesNotExist:
        author = None
    
 
    
    context = {
        "product": product,
        "author": author,
    }
    return render(request, 'product/detail.html', context)

def product_add(request):
    form = ProductModelForm()

    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product:product_list")

    context = {
        "form": form
    }
    return render(request, 'product/add.html', context)

def product_edit(request, id):
    model = ProductModel.objects.get(id=id)
    form = ProductModelForm(instance=model)

    if request.method == "POST":
        form = ProductModelForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
            return redirect("product:product_detail", id)

    context = {
        "form": form
    }
    return render(request, 'product/edit.html', context)

def product_delete(request, id):
    model = ProductModel.objects.get(id=id)
    model.delete()
    return redirect("product:product_list")