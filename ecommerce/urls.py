"""ecommerce URL Configuration"""


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('ecomm_auth.urls')),
    path("", include("products.urls")),
    path("", include("cart.urls")),
    path("", include("order.urls")),
    path("", include("checkout.urls")),
    path("", include("review_wishlist.urls")),


]