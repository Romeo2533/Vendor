from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .utils import StandardResultsSetPagination


def get_vendor(self, request, id):
        try:
            return Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            raise Http404
class VendorList(generics.ListAPIView):
    queryset=Vendor.objects.all().order_by('id')
    search_fields = ['name', '^gst_number']
    serializer_class = VendorSerializer
    pagination_class = StandardResultsSetPagination
    
    def paginate_queryset(self, queryset):
        if self.request.query_params.get(self.paginator.page_query_param) == 'all':
            return None
        return super().paginate_queryset(queryset)
    
    def post(self, request, format=None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'Vendor has been created successfully','vendor_id':serializer.data['id']}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorDetail(APIView):
    queryset=Vendor.objects.all()

    
    def get_vendor(self, request, id):
        try:
            return Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        vendor = self.get_vendor(request, id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)


    def patch(self, request, id, format=None):
        vendor = self.get_vendor(request, id)
        serializer = VendorSerializer(instance = vendor, data = request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'Vendor has been updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

