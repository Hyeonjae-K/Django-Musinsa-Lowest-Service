from rest_framework import serializers
from models import Brands, History, Products


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ('ko_name', 'en_name', 'url', 'image', 'created_date')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('product', 'price', 'created_date')


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'brand', 'current', 'lowest',
                  'highest', 'url', 'image', 'created_date')
