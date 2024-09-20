from django.urls import path
from .views import SignupAPIViews, LoginAPIView, LogoutAPIView, Cart, OrderCreateAPIView, OrderDeleteAPIView

urlpatterns = [
    path('signup/', SignupAPIViews.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('cart/', Cart.as_view(), name='cart'),
    path('order/', OrderCreateAPIView.as_view(), name='order'),
    path('order-delete/<int:id>/', OrderDeleteAPIView.as_view(), name='delete-order'),
]