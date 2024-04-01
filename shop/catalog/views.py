from catalog.models import Category, Product, Seller, Discount
from rest_framework.generics import ListAPIView
from catalog.serializers import CategorySerializer, ProductSerializer, DiscountSerializer, SellerSerializer
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

class DiscountsListView(ListAPIView):
    queryset = Discount.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = DiscountSerializer


class DiscountProductsView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, discount_id):
        if discount_id == 0:
            queryset = Product.objects.filter(discount=None)
        else:
            queryset = Product.objects.filter(discount__id=discount_id)
        serializer = ProductSerializer(queryset, many=True)
        print('test')
        return Response(serializer.data)


class SellersListView(ListAPIView):
    queryset = Seller.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = SellerSerializer


class SellerProductsView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, seller_id):
        queryset = Product.objects.filter(seller__id=seller_id)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


