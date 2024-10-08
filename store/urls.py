from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import product_detail

urlpatterns = [
     path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    

]