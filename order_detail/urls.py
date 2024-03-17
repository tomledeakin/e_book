from django.urls import path
from . import views

app_name = "order_detail"

urlpatterns = [
    path('<int:id>/', views.order_detail, name="order_detail"),

]
