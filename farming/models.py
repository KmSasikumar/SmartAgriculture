from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class calculate_yeild(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    weigth = models.FloatField()
    area = models.FloatField()
    result = models.FloatField()

class crop_productions(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    crop_name = models.CharField(max_length=200)
    land_acer = models.FloatField()
    crop_yeild = models.FloatField()
    user_cost = models.FloatField()
    market_price = models.FloatField()
    totalProduction = models.FloatField(null = True)
    totalRevenue = models.FloatField(null = True)
    totalCost = models.FloatField(null = True)
    profit = models.FloatField(null = True)