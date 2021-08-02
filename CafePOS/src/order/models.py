from django.contrib.auth.models import User
from django.db import models
from menu.models import Category, Menu, Size
from customer.models import Customer


# Create your models here.


class Order(models.Model):
    TYPE_CHOICES = [
        ('service', 'Service'),
        ('takeaway', 'Take Away'),
        ('delivery', 'Delivery')
    ]
    ordertype = models.CharField(max_length=10, null=True, blank=True, choices=TYPE_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table_number = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
    deliver_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Order.deliver_by+', null=True, blank=True)
    deliver_at = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Order.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Order.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Order.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.ordertype } - {self.customer.name} - {self.table_number} - {self.complete} "


class TempOrderItem(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('cooked', 'Cooked'),
        ('sarved', 'Sarved'),
        ('waste', 'Waste')
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default=1, null=True, blank=True, choices=STATUS_CHOICES)
    commit = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='TempOrderItem.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='TempOrderItem.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='TempOrderItem.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category.name} - {self.menu.name} - {self.quantity} - {self.total}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='OrderItem.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='OrderItem.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='OrderItem.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category.name} - {self.menu.name} - {self.quantity} - {self.total}"


class Table(models.Model):
    number = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    is_reserved = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Table.creator+', null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Table.updater+', null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    deleter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Table.deleter+', null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Table No.{self.number}"
