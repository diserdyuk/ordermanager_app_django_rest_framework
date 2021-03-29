from rest_framework.serializers import ModelSerializer

from ordermanager.models import Employee, Product, Order


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'role']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product 
        fields = ['name', 'price', 'date_created']


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'cashier', 'product', 'client_name', 'status', 'quantity', 'date_created']
