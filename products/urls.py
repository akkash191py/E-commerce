from django.urls import path, include
from . import views

urlpatterns = [

    path("category/", views.CategoryListAPIView.as_view()),
    path("category/<int:pk>/", views.CategoryAPIView.as_view()),
    #path("list/product/", views.ListProductAPIView.as_view()),
    path("product/<id>/", views.RelatedProductAPIView.as_view()),
    path("create/product/", views.CreateProductAPIView.as_view()),
    path("product/<int:pk>/delete/", views.DestroyProductAPIView.as_view()),
    path("product/", views.ProductView.as_view()),

]