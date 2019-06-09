from product.models import Product, Company, Kind
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = '__all__'