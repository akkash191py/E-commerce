
from django.contrib import admin
from .models import *


# CategoryAdmin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','icon','created','modified')
admin.site.register(Category,CategoryAdmin)

# BrandAdmin
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name','image')
admin.site.register(Brand,BrandAdmin)

# Color Admin
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_name','color_bg')
admin.site.register(Color,ColorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','seller', 'product_name','price','quantity','stock','status')
    list_editable = ('status',)
admin.site.register(Product,ProductAdmin)


admin.site.register(Quantity)
admin.site.register(Size)
admin.site.register(ProductAttribute)