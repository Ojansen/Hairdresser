from django.db import models
from account.models import Account


# Create your models here.
class Order(models.Model):
    appointment_date = models.DateTimeField()
    description = models.TextField()
    user_id = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=False
    )
