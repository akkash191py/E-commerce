from django.urls import path, include
from . import views

urlpatterns = [

    path('save-review/<int:pid>',views.save_review, name='save-review'),
    path('add-wishlist',views.add_wishlist, name='add_wishlist'),
    path('my-wishlist',views.my_wishlist, name='my_wishlist'),
    path('my-reviews',views.my_reviews, name='my-reviews'),

]



