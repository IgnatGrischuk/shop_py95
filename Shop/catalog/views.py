from .models import Category, Product, Seller, Discount
from rest_framework.generics import ListAPIView
from .serializers import (CategorySerializer, ProductSerializer,
                          SellerSerializer, DiscountSerializer)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )


class CategoryProductsView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, category_id):
        queryset = Product.objects.filter(category__id=category_id)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class SellerListView(APIView):
        queryset = Seller.objects.all()
        serializer_class = SellerSerializer
        permission_classes = (AllowAny, )


class SellerProductView(APIView):
    permission_classes = (AllowAny, )

    def get(self, seller_id):
        queryset = Product.objects.filter(seller_id=seller_id)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
