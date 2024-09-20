from django.contrib import admin
from .models import Category, Product
from users.models import Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)