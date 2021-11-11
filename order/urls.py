from django.urls import path
from . import views


urlpatterns = [
    path("order/", views.OrderListView.as_view()),
    path("order/<int:pk>/", views.OrderView.as_view()),
    path("shipping/", views.ListShippingAPIView.as_view()),
    path("shipping/<int:pk>", views.ShippingDetailView.as_view()),
    path("create/shipping/", views.createShippingAPIView.as_view()),

]