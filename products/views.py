from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from rest_framework.views import Response, APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Category, Product
from users.forms import OrderForm

class HomeAPIView(APIView):
    permission_classes = [AllowAny, ]
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'home.html' #template page home

    def get(self, request):
        categorys = Category.objects.all()
        products = Product.objects.all()
        return Response({
            'categorys': categorys,
            'products': products
        })


class ProductDetail(APIView):
    permission_classes = [AllowAny, ]
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'detail.html' #template page home

    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = OrderForm()
        return Response({
            'products': product,
            'form': form
        })
    

class ProductsForPerCategorys(APIView):
    permission_classes = [AllowAny,]
    renderer_classes = [TemplateHTMLRenderer,]
    template_name = 'category-products.html'

    def get(self, request, id):
        products = get_list_or_404(Product, category=id)
        return Response({
            'products': products
        })
    



