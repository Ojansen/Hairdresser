from django.db import models
from account.models import Account
from hairdresser.models import Hairdresser


# Create your models here.
class Order(models.Model):
    appointment_date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    user_id = models.ManyToManyField(Account)
    hairdresser_id = models.OneToOneField(Hairdresser, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
