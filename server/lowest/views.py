from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Brands, History, Products
from .serializers import BrandsSerializer, HistorySerializer, ProductsSerializer


@api_view(['GET'])
def testBrands(request):
    total_brands = Brands.objects.all()
    serializer = BrandsSerializer(total_brands, many=True)
    Response(serializer.data)


@api_view(['GET'])
def testHistory(request):
    total_History = History.objects.all()
    serializer = HistorySerializer(total_History, many=True)
    Response(serializer.data)


@api_view(['GET'])
def testProducts(request):
    total_Products = Products.objects.all()
    serializer = ProductsSerializer(total_Products, many=True)
    Response(serializer.data)
