from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from trading.models import Product
from .serializers import ProductSerializer

class ListProduct(generics.ListAPIView):
    print(Product.objects.all())
    queryset = Product.objects.all()
    serializer_class = ProductSerializer