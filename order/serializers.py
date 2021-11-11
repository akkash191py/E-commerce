from rest_framework import serializers
from .models import Order, OrderItem,Shipping
from products.serializers import ProductDetailSerializer
from django.contrib.auth.models import User


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = "__all__"
        #exclude = ("modified",)


class CreateShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        exclude = ["user"]




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ("modified",)

class OrderListSerializer(serializers.ModelSerializer):
    shipping_address = ShippingSerializer(required=False)


    class Meta:
        model = Order
        fields = [
            "id",
            "buyer",
            "order_id",
            "status",
            "shipping_address",
            "ordered_date",

        ]


class OrderMiniSerializer(serializers.ModelSerializer):
    shipping_address = ShippingSerializer(required=False)


    class Meta:
        model = Order
        exclude = ("modified",)




class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ("modified",)


class OrderItemMiniSerializer(serializers.ModelSerializer):
    order = OrderMiniSerializer(required=False, read_only=True)
    product = ProductDetailSerializer(required=False, read_only=True)

    class Meta:
        model = OrderItem
        exclude = ("modified",)