"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('san-pham/', include('product.urls')),
    path('danh-muc/', include('category.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('dang-ky/', include('register.urls')),
    path('dang-ky-author/', include('register_author.urls')),
    path('dang-nhap/', include('login2.urls')),
    path('dang-xuat/', include('logout2.urls')),
    path('doi-tac/', include('partner.urls')),
    path('xac-thuc/', include('auth2.urls')),
    path('author/', include('author.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
