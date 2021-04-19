from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.db import models

from app.core.models import BaseModel
from .managers import UserManager

class Account(AbstractUser):
    """
    Extension of the original authorization account of django admin.
    Will use default OAuth of django admin for ease of use.

    Inherited
    ---------
    AbstactUser : class obj
        OAuth model intended for default permissions needed.

    """
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    profile_picture = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    preferred_name = models.CharField(max_length=128, null=True, blank=True)
    secondary_email = models.EmailField(
    	max_length=64,
    	unique=True,
    	null=True,
    	blank=True,
    )

    region = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
    	return self.preferred_name or self.email

    @property
    def slug(self):
    	return slugify(self.preferred_name)


class AccountAddress(BaseModel):
    """
    AccountAddress model is for the addreses of a certain user to be used
    by our Courier model.

    Inherited
    ---------
        core.Basemodel : class obj
            Contains the basic information of when this object was created etc.
            It also helps deal with deletion records by setting is_active to 
            False.

    """
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    number_bulding = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    area = models.CharField(max_length=128, null=True, blank=True)
    zipcode = models.IntegerField(default=0)
    province = models.CharField(max_length=32, null=True, blank=True)
    country = models.CharField(max_length=56, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.preferred_name, self.country)

