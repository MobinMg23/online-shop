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
    

class ProfieleEditeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', "last_name", 'password')

    def save(self, commit=True):
        user = super(ProfieleEditeForm, self).save(commit=False)
        if 'password' in self.cleaned_data:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user