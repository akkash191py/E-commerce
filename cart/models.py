from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


# Cart Model
class Cart(models.Model):
    user = models.OneToOneField(
        User, related_name="user_cart", on_delete=models.CASCADE
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    class Meta:
        verbose_name_plural = 'Cart'

    def __str__(self):
        return str(self.user) + " " + str(self.total)

"""@receiver(post_save, sender=User)
def create_user_cart(sender, created, instance, *args, **kwargs):
    if created:
        Cart.objects.create(user=instance)"""


# CartItem Model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_item", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="cart_product", on_delete=models.CASCADE
    )
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return str(self.product.product_name)


# Signals for CartItem
@receiver(pre_save, sender=CartItem)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)