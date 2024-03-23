from django.shortcuts import render
from .models import CategoryModel
from django.views.generic import ListView, DetailView
from home.models import PromotionModel
from django.conf import settings
from django.contrib.auth.decorators import login_required
from product.models import ProductModel


class CategoryListView(ListView):
    queryset = CategoryModel.objects.all()
    template_name = 'category/list.html'
    context_object_name = "category_list"

class CategoryDetailView(DetailView):
    model = CategoryModel
    template_name = 'category/detail.html'   
    context_object_name = "category" 


# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def category_list(request):
    category_list = CategoryModel.objects.all()

    # query = """
    #     SELECT 
    #         * -- sum() as custom_field
    #     FROM 
    #         category_categorymodel
    #     WHERE 
    #         category_name = %(category_name)s
    #         AND delete_flg = %(delete_flg)s
    # """
    # params = {
    #     "category_name": "dien thoai",
    #     "delete_flg": 0
    # }
    # category_list = CategoryModel.objects.raw(query, params)
    promotion_list = PromotionModel.objects.all()
    
    context = {
        "category_list": category_list,
        "promotion_list": promotion_list
    }
    return render(request, 'category/list.html', context)

def category_detail(request, id):
    category = CategoryModel.objects.get(id=id)
    product = ProductModel.objects.filter(category=category)
    context = {
        "category": category,
        "product": product
    }
    return render(request, 'category/detail.html', context)



