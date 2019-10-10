from django.db import models
from account.models import Account


# Create your models here.
class Hairstyle(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    SEX_TYPES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX_TYPES)

    def __str__(self):
        return self.name


class Hairdresser(models.Model):
    photo = models.ImageField(upload_to='static/img/hairdresser')
    user_id = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
    )
    hairstyle_id = models.ManyToManyField(Hairstyle)

    def __str__(self):
        return self.user_id.first_name
