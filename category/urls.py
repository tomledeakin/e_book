from django.urls import path
from . import views

app_name = "category"

urlpatterns = [
    path('', views.category_list, name="category_list"),
    path('<int:id>/', views.category_detail, name="category_detail"),

    path('view/', views.CategoryListView.as_view(), name="category_list_view"),
    path('view/<int:pk>/', views.CategoryDetailView.as_view(), name="category_detail_view"),
]
