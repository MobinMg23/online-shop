from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    