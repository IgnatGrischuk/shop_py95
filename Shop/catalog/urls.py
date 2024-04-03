from django.urls import path
from .views import (CategoryListView, CategoryProductsView, SellerListView,
                    SellerProductView, CartView)

urlpatterns = [
    path('categories', CategoryListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', CategoryProductsView.as_view(),
         name='category-products'),
    path('sellers/', SellerListView.as_view(),
         name='seller'),
    path('sellers/<int:seller_id>/', SellerProductView.as_view(),
         name='seller-product'),
    path('cart/', CartView.as_view(), name='cart')
]