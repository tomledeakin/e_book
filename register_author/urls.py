from django.urls import path
from . import views

app_name = "register_author"

urlpatterns = [
    path('', views.register, name="register"),
]
