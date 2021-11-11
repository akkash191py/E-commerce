from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status, exceptions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    GenericAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)
from .serializers import (
    OrderItemSerializer,
    OrderItemMiniSerializer,
    OrderSerializer,
    OrderListSerializer,
    OrderMiniSerializer,
    ShippingSerializer,
    CreateShippingSerializer,
)
from .models import Order, OrderItem, Shipping
from .models import Product

# OrderAPI
class OrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #user = request.user
        #buyer = request.data.get("buyer")
        #print(buyer)
        #return Response({"sucess"})
        #queryset = Order.objects.filter(buyer = buyer)
        queryset = Order.objects.all()
        serializer = OrderListSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request, pk, *args, **kwargs):
        user = request.user
        user_address = Shipping.objects.filter(user=user).first()
        product = get_object_or_404(Product, pk=pk)
        if product.quantity == 0:
            raise exceptions.NotAcceptable("quantity of this product is out.")
        try:
            order_id = request.data.get("order_id", "")
            quantity = request.data.get("quantity", 1)
        except:
            pass

        total = quantity * product.price
        order = Order().create_order(user, order_id, user_address)
        order_item = OrderItem().create_order_item(order, product, quantity, total)
        serializer = OrderItemMiniSerializer(order_item)


        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ListShippingAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShippingSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Shipping.objects.filter(user=user)
        return queryset


class ShippingDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShippingSerializer
    queryset = Shipping.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        shipping_address = self.get_object()
        if shipping_address.user != user:
            raise NotAcceptable("this addrss don't belong to you")
        serializer = self.get_serializer(shipping_address)
        return Response(serializer.data, status=status.HTTP_200_OK)


class createShippingAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateShippingSerializer
    queryset = ""

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
