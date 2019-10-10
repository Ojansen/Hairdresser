from django.db import models
from account.models import Account
from hairdresser.models import Hairdresser


# Create your models here.
class Order(models.Model):
    appointment_date = models.DateTimeField()
    TIME_CHOICES = (
        ('0', '08:00'),
        ('1', '09:00'),
        ('2', '10:00'),
        ('3', '11:00'),
        ('4', '12:00'),
        ('5', '14:00'),
    )
    appointment_time = models.CharField(max_length=1, choices=TIME_CHOICES)
    description = models.TextField()
    user_id = models.ManyToManyField(Account)
    hairdresser_id = models.ManyToManyField(Hairdresser)

    def __int__(self):
        return self.id
