
from django.db import models

# Create your models here.
from django.utils import timezone


class Stock(models.Model):
    share = models.CharField(max_length=200, unique=True)
    jse_code = models.CharField(max_length=200, unique=True)
    price = models.CharField(max_length=200)
    move = models.CharField(max_length=200)
    move_change = models.CharField(max_length=200)
    market_cap = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
        ordering = ['id']

    def __str__(self):
        return self.jse_code
