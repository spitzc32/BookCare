from django.db import models

from app.core.models import BaseModel
from app.accounts.models import Account

class Bookmark(BaseModel):
    title = models.CharField(max_length=512, null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=512, null=True)

    THEME_CHOICES = (
        ('PLANT', 'PLANT'),
        ('PEACE','PEACE'),
        ('VERSE','VERSE'),
        ('ADVENTURE', 'ADVENTURE'),
        ('ANIMAL', 'ANIMAL'),
        ('PLANET','PLANET'),
    )
    theme = models.CharField(
        max_length=15,
        choices=THEME_CHOICES,
        default='removed',
    )

    def __str__(self):
        return '{}'.format(self.title)

class AccountBookmark(BaseModel):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    bookmark = models.ForeignKey(to=Bookmark, on_delete=models.CASCADE)
