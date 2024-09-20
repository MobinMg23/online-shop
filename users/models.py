from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import phone_validator
from products.models import Product

class User(AbstractUser):
    phone = models.CharField(max_length=15, validators=[phone_validator], blank=True)


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = 'P', 'Pending'
        DONE = 'D', 'Done'
        CANCELED =  'C', 'Canceled'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)     
    status = models.CharField(
        max_length=1,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=1)

