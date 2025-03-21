from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class calculate_yeild(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    weigth = models.IntegerField()
    area = models.IntegerField()
    result = models.IntegerField()

class crop_productions(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    crop_name = models.CharField(max_length=200)
    land_acer = models.IntegerField()
    crop_yeild = models.IntegerField()
    user_cost = models.IntegerField()
    market_price = models.IntegerField()
    totalProduction = models.IntegerField(null = True)
    totalRevenue = models.IntegerField(null = True)
    totalCost = models.IntegerField(null = True)
    profit = models.IntegerField(null = True)