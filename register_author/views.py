from django.shortcuts import render, redirect
from .forms import RegisterForm
from home.models import PromotionModel
# Create your views here.
def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:home")

    context = {
        "form": form    
    }
    return render(request, "register_author/register_author.html", context)
