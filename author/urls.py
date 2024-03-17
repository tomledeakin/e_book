from django.urls import path
from . import views

app_name = "author"

urlpatterns = [
    path('', views.author_list, name="author_list"),
    path('<int:id>/', views.author_detail, name="author_detail"),
]