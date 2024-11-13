from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    path('product_create/', views.product_create, name='product_create'),
    path('product_edit/', views.product_edit, name='product_edit'),
    path('product_delete/', views.product_delete, name='product_delete'),
    path('product_list/',views.product_list,name='product_list'),
    path('cart/', views.cart_detail, name='cart_detail'), 
    path('cart/add/<str:product_name>/', views.add_to_cart, name='add_to_cart'),  
    path('cart/remove/<str:product_name>/', views.remove_from_cart, name='remove_from_cart'),  
]
