from django.shortcuts import render
import logging

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from rest_framework import permissions, status
from rest_framework.exceptions import PermissionDenied, NotAcceptable, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import (CategoryListSerializer, ProductSerializer, CreateProductSerializer, ProductAllSerializer,
                          ProductDetailSerializer,ProductAttributeSerializer,ProductMiniSerializer)
from rest_framework import filters
from googletrans import Translator


translator = Translator()
class CategoryListAPIView(ListAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class CategoryAPIView(RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {}
        for k, v in serializer.data.items():
            data[k] = translator.translate(str(v), dest="en").text

        return Response(data)



class RelatedProductAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('id')

    """def get(self, request, id, *args,**kwargs):
        product_id = id  # request.data.get("product_id")
        print(id)
        if not product_id:
            return Response({"error": "Product Id Not Found"}, status=400)
        product = get_object_or_404(Product,id=product_id)
        products_serialized = self.request.query_params.get('product')
        #products_serialized = ProductSerializer(
            #product.get_related_products(), many=true,context={'request':request})
        return Response(products_serialized.data)"""


    """def get_queryset(self):
        user = self.request.user
        queryset = Product.objects.filter(user=user)
        print(user)
        print(queryset)
        return queryset"""

class CreateProductAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateProductSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(seller=user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DestroyProductAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({"detail": "Product deleted"})


class ProductView(APIView):

    """ API for Product """

    def get(self,request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__name = category)
        else:
            queryset = Product.objects.all()
        serializer = ProductAllSerializer(queryset , many = True)
        return Response({'count' : len(serializer.data) , 'data' : serializer.data})


class Product_detail(APIView):
    def get(self,request):
        category = self.request.query_params.get('category')