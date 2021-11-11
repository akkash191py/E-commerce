from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ("modified",)


class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(slug_field="username", queryset=User.objects)
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Product
        fields = ('id','seller','category','product_name','image','price','description','brand_type','quantity_type')

class ProductMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data = serializers.ModelSerializer.to_representation(self, instance)
        return data


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("modified",)
        # read_only_fields = ('id', 'seller', 'category', 'product_name', 'price', 'image', 'description', 'quantity',)


class ProductDetailSerializer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(slug_field="username", queryset=User.objects)
    category = serializers.SerializerMethodField()
    image = Base64ImageField()

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Product
        fields = '__all__'
        #exclude = ("modified",)


# Brand Serializer
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


# Quantity Serializer
class QuantitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Quantity
        fields = '__all__'


# Color Serializer
class ColorSerializer(serializers.ModelSerializer):

    """ Serializer for ColorVarient Models """

    class Meta:
        model = Color
        fields = '__all__'


# Size Serializer
class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'


# Product Serializer
class ProductAllSerializer(serializers.ModelSerializer):

    category  = CategoryListSerializer()              # serialize the category fields of Product Model
    quantity_type = QuantitySerializer()               # serialize the quantity_type fields of Product Model


    class Meta:
        model = Product
        fields = '__all__'

class ProductAttributeSerializer(serializers.ModelSerializer):

    #product = ProductAllSerializer()
    color = ColorSerializer()  # serialize the color_type fields of Product Model
    size = SizeSerializer()

    class Meta:
        model = ProductAttribute
        fields = '__all__'