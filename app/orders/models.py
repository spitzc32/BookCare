from app.core.models import BaseModel
from app.accounts.models import Account
from app.products.models import Product

from django.db import models
from django.utils.text import slugify


class Order(BaseModel):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    ORDER_STATE_CHOICES = (
        ('removed', 'removed'),
        ('cart','cart'),
        ('checkout','checkout'),
        ('payment', 'payment'),
        ('courier', 'courier'),
        ('received','received'),
        ('failed','failed'),
    )
    order_status = models.CharField(
        max_length=15,
        choices=ORDER_STATE_CHOICES,
        default='removed',
    )
    PAYMENT_METHOD_CHOICES = (
        ('COD', 'COD'),
        ('visa','visa'),
        ('paypal','paypal'),
    )
    payment_method = models.CharField(
        max_length=15,
        choices=ORDER_STATE_CHOICES,
        default='COD',
    )
    order_price = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)



class OrderProducts(BaseModel):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    additional_comment = models.CharField(max_length=512, null=True)
    total = models.FloatField(default=0)

    @property
    def total(self):
        return self.product.price * quantity


	

	
