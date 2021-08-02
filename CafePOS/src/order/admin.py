from django.contrib import admin
from .models import Order, TempOrderItem, OrderItem, Table


# Register your models here.
admin.site.register(Order)
admin.site.register(TempOrderItem)
admin.site.register(OrderItem)
admin.site.register(Table)
