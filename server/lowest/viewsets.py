from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Brands, History, Products
from .serializers import BrandsSerializer, HistorySerializer, ProductsSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
