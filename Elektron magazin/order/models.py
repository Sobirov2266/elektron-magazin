from django.db import models
from account.models import Customer
from product.models import Product


class Order(models.Model):
    STATUES = [
        ('PENDING', 'pending'),
        ('INPROGRESS', 'inprogress'),
        ('COMPLATED', 'complated'),
        ('CANCELED', 'canceled')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='orders', null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    required_date = models.DateTimeField(null=True)
    shipped_date = models.DateTimeField(null=True)
    canceled_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, choices=STATUES, default='PENDING')


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='orders')
    quantity=models.IntegerField(default=1)

