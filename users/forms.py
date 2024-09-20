from django import forms
from .models import User, Order
from django.utils import timezone

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('quantity',)  # فقط شامل quantity
    
    def save(self, commit=True):
        order = super().save(commit=False)
        order.status = Order.OrderStatus.PENDING
        order.created_at = timezone.now()
        if commit:
            order.save()
        return order