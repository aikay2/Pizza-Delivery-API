from .models import Order
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    order_status = serializers.HiddenField(default='PENDING')
    
    class Meta:
        model = Order
        fields = ['id', 'size', 'order_status', 'quantity']
        
        
class OrderDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['id', 'size', 'order_status', 'quantity', 'created_at', 'updated_at']
        
        
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default="PENDING")
    
    class Meta:
        model = Order
        fields = ['order_status']