from django.shortcuts import render
from django import views


from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Customer, Category, Add, AddPic
from .serializers import CustomerSerializer, CategorySerializer, AddSerializer, AddPicSerializer


class Pagination(PageNumberPagination):
    page_size = 10


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class AddViewSet(viewsets.ModelViewSet):
    serializer_class = AddSerializer
    queryset = Add.objects.all()
    filterset_fields = ['cus', 'category']


class AddPicViewSet(viewsets.ModelViewSet):
    serializer_class = AddPicSerializer
    queryset = AddPic.objects.all()
    filterset_fields = ['add']
