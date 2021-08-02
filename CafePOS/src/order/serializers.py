from rest_framework import serializers
from .models import TempOrderItem


class TempOrderItemListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    menu = serializers.CharField(source='menu.name')
    size = serializers.CharField(source='size.size')

    class Meta:
        model = TempOrderItem
        fields = '__all__'


# class OrderItemListSerializer(serializers.ModelSerializer):
#     category = serializers.CharField(source='category.name')
#     menu = serializers.CharField(source='menu.name')
#
#     class Meta:
#         model = OrderItem
#         fields = '__all__'