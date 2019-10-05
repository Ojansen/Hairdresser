from django.db import models
from account.models import Account


# Create your models here.
class Hairstyle(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sex = models.IntegerField()

    def __str__(self):
        return self.name


class Hairdresser(models.Model):
    user_id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
    )
    hairstyle_id = models.ManyToManyField(Hairstyle)
