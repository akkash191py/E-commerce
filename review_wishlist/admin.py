from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Wishlist)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user','product','review_text','review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)