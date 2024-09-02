from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorList, VendorDetail, PurchaseOrderViewSet, HistoricalPerformanceViewSet

router = DefaultRouter()
router.register(r'purchase-order', PurchaseOrderViewSet, basename='purchase')
router.register(r'historical-performance', HistoricalPerformanceViewSet, basename='historical')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs here
    path('vendors/', VendorList.as_view(), name='vendor-list'),
    path('vendors/<int:id>/', VendorDetail.as_view(), name='vendor-detail'),
]
