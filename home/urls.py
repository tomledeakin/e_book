from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('add/', views.promotion_add, name="promotion_add"),
    # path('promotion_list/', views.promotion_list, name="promotion_list"),
]




