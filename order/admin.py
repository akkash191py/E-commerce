from django.contrib import admin
from .models import *


# OrderAdmin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyer','order_id','status','ordered_date','shipping_address')
admin.site.register(Order,OrderAdmin)


# OrderItemAdmin
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','product','quantity','total')
admin.site.register(OrderItem,OrderItemAdmin)


# OrderItemAdmin
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('name','street','city','state','pincode','contact_number')
admin.site.register(Shipping,ShippingAdmin)