from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"

class ProductDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
