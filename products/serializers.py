from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ['id','name','description','price','quantity','product_image']

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ['id','name','description','price','quantity']
