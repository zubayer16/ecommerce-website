from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import product_detail

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

    # New routes for additional pages
    path('profile/', views.profile, name="profile"),
    path('categories/', views.categories, name="categories"),
    path('trends/', views.trends, name="trends"),
    path('social/', views.social, name="social"),
    path('about/', views.about, name="about"),
]
