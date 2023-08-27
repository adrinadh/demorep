from django.db import models
from ecommerceapp.models import Product
# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date', ]

    def __str__(self) -> str:
        return '{}'.format(self.cart_id)


class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItems'

    def subTotal(self):
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return '{}'.format(self.product)
