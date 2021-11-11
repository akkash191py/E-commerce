
from django.contrib import admin
from .models import *


# CartAdmin
class CartAdmin(admin.ModelAdmin):
    list_display = ('user','total')
admin.site.register(Cart,CartAdmin)


# CartAdmin
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','product','quantity','price')
admin.site.register(CartItem,CartItemAdmin)
