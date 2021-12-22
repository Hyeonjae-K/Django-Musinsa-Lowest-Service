from django.urls import path
from .views import testBrands, testHistory, testProducts

urlpatterns = [
    path('test/brands/', testBrands),
    path('test/history/', testHistory),
    path('test/products/', testProducts),
]
