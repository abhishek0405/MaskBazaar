from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    #queryset = Product.objects.get(price=500)
    queryset = Product.objects.all()#GET ALL THE CATEGORIES
    serializer_class = ProductSerializer #This will be serialising the data.

    def filter_bycateg(self,request,id):
      return Product.objects.filter(category__id=1)
      #return 1