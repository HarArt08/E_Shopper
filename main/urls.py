from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('404/', ErorListView.as_view(), name='eror'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('checkout/', CheckoutListView.as_view(), name='checkout'),
    path('product_detail/', ProductListView.as_view(), name='product'),
    path('product_detail/<int:id>', ProductDetailView.as_view(), name='product_detail'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_single/', BlogSingleListView.as_view(), name='blog_single'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('shops/', ShopListView.as_view(), name='shops'),
    path('shops/<int:id>', ShopDetailView.as_view(), name='shop_detail'),
    path('', FooterListView.as_view(), name='footer'),
]