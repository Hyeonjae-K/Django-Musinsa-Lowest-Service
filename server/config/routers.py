from rest_framework import routers
from lowest.viewsets import BrandsViewSet, HistoryViewSet, ProductsViewSet

router = routers.DefaultRouter()

router.register(r'brands', BrandsViewSet)
router.register(r'history', HistoryViewSet)
router.register(r'products', ProductsViewSet)
