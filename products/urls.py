from django.urls import path
from .views import HomeAPIView, ProductDetail, ProductsForPerCategorys


urlpatterns = [
    path('', HomeAPIView.as_view(), name='home'),
    path('product/<int:id>/', ProductDetail.as_view(), name='detail'),
    path('category/<int:id>/', ProductsForPerCategorys.as_view(), name='category-products'),
]