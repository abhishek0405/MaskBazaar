from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')#GET ALL THE CATEGORIES
    serializer_class = CategorySerializer #This will be serialising the data.
