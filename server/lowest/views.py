from rest_framework.response import Response
from rest_framework.decorators import api_view
from apscheduler.schedulers.background import BackgroundScheduler

from .models import Brands, History, Products
from .serializers import BrandsSerializer, HistorySerializer, ProductsSerializer
from .crawler import brandsCrawler

sched = BackgroundScheduler()
sched.add_job(brandsCrawler, 'cron', minute='0')
sched.start()


@api_view(['GET'])
def testBrands(request):
    total_brands = Brands.objects.all()
    serializer = BrandsSerializer(total_brands, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def testHistory(request):
    total_History = History.objects.all()
    serializer = HistorySerializer(total_History, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def testProducts(request):
    total_Products = Products.objects.all()
    serializer = ProductsSerializer(total_Products, many=True)
    return Response(serializer.data)
