from django.shortcuts import render
from .models import AuthorModel
from home.models import PromotionModel
from django.conf import settings
from django.contrib.auth.decorators import login_required
from product.models import ProductModel


# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def author_list(request):
    author_list = AuthorModel.objects.all()
    promotion_list = PromotionModel.objects.all()
    context = {
        "author_list": author_list,
        "promotion_list": promotion_list
    }
    return render(request, 'author/list.html', context)

def author_detail(request, id):
    author = AuthorModel.objects.get(id=id)
    product = ProductModel.objects.filter(author=author)
    context = {
        "author": author,
        "product": product
    }
    return render(request, 'author/detail.html', context)