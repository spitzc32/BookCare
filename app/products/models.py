from app.core.models import BaseModel
from app.accounts.models import Account

from django.db import models
from django.utils.text import slugify


class Product(BaseModel):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=2000)
	price = models.FloatField(default=0)
	quantity_stock = models.IntegerField(default=0)

	def __str__(self):
		return self.title


class ProductFeedback(BaseModel):
	product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
	account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
	feedback = models.CharField(max_length=2000)

	def __str__(self):
		return '{} - {}'.format(self.product.title, self.account.preferred_name)
