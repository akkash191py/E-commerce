from django.db import models
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.


# Product Review
RATING = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField(blank = True)
    review_rating = models.CharField(choices=RATING, max_length=150, blank=True)


    class Meta:
        verbose_name_plural='Product Review'

    def __str__(self):
        return str(self.user)

    def get_review_rating(self):
        return self.review_rating

# WishList
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural= 'Wishlist'

    def __str__(self):
        return self.product.product_name