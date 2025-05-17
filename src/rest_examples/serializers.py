from rest_framework import serializers

from .models import Product

class TestSerializer(serializers.Serializer):
    """Serializa un campo de nombre para nuestra APIView"""
    name = serializers.CharField(max_length=15)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'