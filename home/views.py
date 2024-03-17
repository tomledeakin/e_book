from django.shortcuts import render, HttpResponse, redirect
from category.models import CategoryModel
from .forms import PromotionModelForm
from .models import PromotionModel
from home.models import PromotionModel
from django.conf import settings
from author.models import AuthorModel
# Create your views here.
def home(request):
    promotion_list = PromotionModel.objects.all()

    # sort = request.GET.get("sort")
    # if sort not in ["-created_at"]:
    #     sort = settings.DEFAULT_SORT
    
    context = {
        "promotion_list": promotion_list
    }
    return render(request, "home/home.html", context)

def about(request):
    return render(request, "home/about.html")



def promotion_add(request):
    form = PromotionModelForm()

    if request.method == "POST":
        form = PromotionModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home:home")

    context = {
        "form": form
    }
    return render(request, 'home/add.html', context)

# def promotion_list(request):
#     promotion_list = PromotionModel.objects.all()


#     context = {
#         "promotion_list": promotion_list
#     }
#     return render(request, 'home/home.html', context)