from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import Response, APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics, status
from .serializers import *
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import User, Order
from products.models import Product, Category
from .forms import LoginForm, OrderForm, ProfieleEditeForm


class SignupAPIViews(APIView):
    permission_classes = [AllowAny,]
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'signup.html'
    
    def get(self, request):
        serializer = SignupSerializer()
        return Response({
            'serializer': serializer
        })
    
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'serializer': serializer
            })
        serializer.save()
        return redirect("home")


class LoginAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = "login.html"
    
    def get(self, request):
        form = LoginForm()
        return Response({'form': form})
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('login')
        dj_login(request, user)       
        return redirect('home')
        

class LogoutAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            dj_logout(request)
            return redirect('home')


class OrderCreateAPIView(APIView):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        order_form = OrderForm(request.POST)
        
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.product = product
            order.user = request.user
            quantity = order.quantity

            try:
                if quantity and product.price:
                    order.total = product.price * quantity
                else:
                    raise ValueError("Invalid quantity or product price.")
            except Exception as e:
                return Response({'error': str(e)}, status=400)

            order.status = 'pending'
            order.save()
            return redirect('home')
        else:
            return Response({'form': order_form.errors}, status=400)
        

class OrderDeleteAPIView(APIView):
    def delete(self, request, id):
        order = get_object_or_404(Order, id=id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
    
    

class Cart(APIView):
    renderer_classes = [TemplateHTMLRenderer,]
    template_name = 'cart.html'

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        return Response({'orders': orders})
    

class ProfileEditeAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    renderer_classes = [TemplateHTMLRenderer,]
    template_name = 'profile-edite.html'

    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        form = ProfieleEditeForm(instance=user)
        return Response({'form': form})
    
    def post(self, request):
        user = get_object_or_404(User, id=request.user.id)
        form = ProfieleEditeForm(request.POST, instance=user)  
        if form.is_valid():
            form.save()
            return redirect('/')
        return Response({'form': form}, template_name=self.template_name)






