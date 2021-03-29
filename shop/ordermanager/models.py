from django.db import models
from django.utils.timezone import now, timedelta


class Employee(models.Model):
    
    SELLER = 'SEL'
    CASHIER = 'CAS'
    ACCOUNTANT = 'ACC'
    ROLES = [
        (SELLER, 'Seller'),
        (CASHIER, 'Cashier'),
        (ACCOUNTANT, 'Accountant')
    ]
    
    role = models.CharField(max_length=50, choices=ROLES, verbose_name='Role', default=CASHIER)
    name = models.CharField(max_length=50, verbose_name='Name')

    def __str__(self):
        return f'{self.role}, {self.name}'


class Product(models.Model):
       
    name = models.CharField(max_length=255, verbose_name='Name product')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Price product')
    date_created = models.DateTimeField(verbose_name='Date create', auto_now=True)

    def __str__(self):
        return self.name

    @property
    def discount(self): 
        if (self.date_created + timedelta(days=30)) < now():
            return 0.2
        else:
            return 0


class Order(models.Model):
    
    NEWORDER = 'NEWORD'
    PROCESSED = 'PROC'
    PAID = 'PAID'
    STATUSES = [
        (NEWORDER, 'New order'),
        (PROCESSED, 'Processed'),
        (PAID, 'Paid')
    ]  
  
    cashier = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Cashier') 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ordered product')
    client_name = models.TextField(verbose_name='Name client', null=True)
    status = models.CharField(max_length=20, choices=STATUSES, default=NEWORDER, verbose_name='Order status')
    quantity = models.PositiveIntegerField(default=1)
    date_created = models.DateTimeField(verbose_name='Date create', auto_now=True)    
    
    def __str__(self):
        return f'{self.client_name}, {self.status}'


class Receipt(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    date_created = models.DateTimeField(verbose_name='Date created', auto_now_add=False)    

    @property
    def total_sum(self):
        return self.order.product.price * self.order.quantity

    @property
    def total_sum_discount(self):
        return self.total_sum * (1 - self.order.product.discount)

    def __str__(self):
        return f'{self.date_created}, {self.order}, {self.total_sum}, {self.total_sum_discount}'

