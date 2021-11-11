
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User


# Category Model
class Category(models.Model):
    name= models.CharField(max_length=100)
    icon = models.ImageField(upload_to='static/category', null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='1. Categories'

    def icon_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.icon.url))


    def __str__(self):
        return self.name


# Brand Model
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/brands')

    class Meta:
        verbose_name_plural='3. Brands'

    def __str__(self):
        return self.brand_name


# Quantity Model
class Quantity(models.Model):
    varient_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='6. Quantities'

    def __str__(self):
        return self.varient_name

class Color(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s" ></div>' % (self.color_code))

    class Meta:
        verbose_name_plural='4. Colors'

    def __str__(self):
        return self.color_name

class Size(models.Model):
    size_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='5. Sizes'

    def __str__(self):
        return self.size_name



# Product Model
class Product(models.Model):
    seller = models.ForeignKey(User, related_name="user_product", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/products')
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    description = models.TextField()
    stock = models.IntegerField(default=100)
    status = models.BooleanField(default=True)

    brand_type = models.ForeignKey(Brand, null=True, on_delete=models.CASCADE)
    quantity_type = models.ForeignKey(Quantity, blank=True, null=True, on_delete=models.PROTECT)



    class Meta:
        verbose_name_plural = '2. Products'

    def __str__(self):
        return self.product_name


# Product Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)



    class Meta:
        verbose_name_plural='7. ProductAttributes'

    def __str__(self):
        return self.product.product_name



