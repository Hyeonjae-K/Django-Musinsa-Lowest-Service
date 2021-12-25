from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Brands, History, Products
from .serializers import BrandsSerializer, HistorySerializer, ProductsSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all().order_by('-created_date')
    serializer_class = HistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class ProductsSetPagination(PageNumberPagination):
    page_size = 30


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = ProductsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
