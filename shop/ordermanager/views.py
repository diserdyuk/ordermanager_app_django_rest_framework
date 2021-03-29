from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ordermanager.models import Employee, Product, Order, Receipt
from ordermanager.serializers import EmployeeSerializer, ProductSerializer, OrderSerializer


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

