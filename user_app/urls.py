"""
URL configuration for E_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('products/', views.products, name='products'),
    path('product/<int:id>/',views.product_details,name='product_details'),
    path('dashboard_user/',views.user_dashboard,name='dashboard_user'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('increase/<int:item_id>/',views.increase_quantity,name='increase_quantity'),
    path('decrease/<int:item_id>/',views.decrease_quantity,name='decrease_quantity'),
    path('remove/<int:item_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('checkout/',views.checkout,name='checkout'),
    
]
