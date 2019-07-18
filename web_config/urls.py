"""web_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, re_path
from web_assembly.views import *
from app_ecommerce.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_register, name='register'),
    path('login/', LoginView.as_view(template_name='user_login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user_logout.html'), name='logout'),

    path('profile/', user_profile, name='profile'),
    path('profile/edit/', user_profile_edit, name= 'edit-profile'),
    path('profile/edit-password/', user_password_edit, name='edit-password'),

    path('', product_list, name='product'),
    path("product/<slug:slug>/", product_detail, name='product-detail'),
    path('new_post/', product_post, name='product-post'),

    path('inventory/', user_inventory, name='product-post'),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
