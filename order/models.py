from django.db import models
from django.contrib.auth.models import User
from products.models import Product
#from cart.models import CartItem
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

# Order

ORDER_STATUS_CHOICES = (
	('created', 'Created'),
	('paid', 'Paid'),
	('shipped', 'Shipped'),
    ('Cancelled', 'Cancelled'),

)

class Order(models.Model):
    buyer = models.ForeignKey(User,related_name="order", on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=120, choices=ORDER_STATUS_CHOICES, default='created')
    ispaid = models.BooleanField(default=False)
    ordered_date = models.DateField(default=True)
    shipping_address = models.ForeignKey('Shipping', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True )

    def __str__(self):
        return str(self.buyer)

    class Meta:
        verbose_name_plural = 'Orders'

    @staticmethod
    def create_order(buyer, order_id, shipping_address, is_paid=False):
        order = Order()
        order.buyer = buyer
        order.order_id = order_id
        order.shipping_address= shipping_address
        order.is_paid = is_paid
        order.save()
        return order


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="product_order", on_delete=models.CASCADE
    )
    #cartitem = models.ForeignKey(CartItem, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    class Meta:
        verbose_name_plural = 'Orderd Items'

    def __str__(self):
        return str(self.order)

    """@staticmethod
    def create_order_item(order, product, quantity, total):
        order_item = OrderItem()
        order_item.order = order
        order_item.product = product
        order_item.quantity = quantity
        order_item.total = total
        #price_of_product = Product.objects.get(id=order_item.product.id)
        #total = order_item.quantity * float(price_of_product.price)
        order_item.save()
        return order_item"""

@receiver(pre_save, sender=OrderItem)
def total_price(sender, **kwargs):
    order_item = kwargs['instance']
    price_of_product = Product.objects.get(id=order_item.product.id)
    #price_of_items = CartItem.objects.get(id=ordered_item.cartitem.id)
    order_item.total = order_item.quantity * float(price_of_product.price)
    #order_item.total = Decimal(price_of_items.price)


# Shipping Model
class Shipping(models.Model):
    user= models.ForeignKey(User,related_name="shipping", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)




    class Meta:
        verbose_name_plural='Shipping'

    def __str__(self):
        return self.name