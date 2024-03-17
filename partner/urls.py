from django.urls import path
from . import views

app_name = "partner"

urlpatterns = [
    path('', views.partner_list, name="partner_list"),
    
    path('api/', views.partner_list_api, name="partner_list_api"),
    # path('api/add/', views.partner_add_api, name="partner_add_api"),

    path('api/<int:id>/', views.partner_detail_api, name="partner_detail_api"),
]
