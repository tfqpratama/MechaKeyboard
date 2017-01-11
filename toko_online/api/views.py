from rest_framework import generics
from .models import *
from .serializers import *

class CustomerDetail(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    def get_queryset(self):
        idc = self.request.query_params.get('id_customer', None)
        queryset = Customer.objects.filter(id_customer=idc)
        return queryset

class ProdukList(generics.ListCreateAPIView):
    serializer_class = ProdukSerializer
    def get_queryset(self):
        queryset = Produk.objects.all()
        nm = self.request.query_params.get('nama', None)
        manuf = self.request.query_params.get('manufacturer', None)
        led = self.request.query_params.get('led_color', None)
        switch = self.request.query_params.get('switch_type', None)
        sz = self.request.query_params.get('size', None)
        if nm is not None:
            queryset = Produk.objects.filter(nama__icontains=nm)
        if manuf is not None:
            queryset = Produk.objects.filter(manufacturer=manuf)
        if led is not None:
            queryset = Produk.objects.filter(led_color=led)
        if switch is not None:
            queryset = Produk.objects.filter(switch_type__icontains=switch)
        if sz is not None:
            queryset = Produk.objects.filter(size=sz)
        return queryset

class ProdukDetail(generics.ListCreateAPIView):
    serializer_class = ProdukSerializer
    def get_queryset(self):
        idp = self.request.query_params.get('id_produk', None)
        queryset = Produk.objects.filter(id_produk=idp)
        return queryset

class NotifikasiList(generics.ListCreateAPIView):
    queryset = Notifikasi.objects.all()
    serializer_class = NotifikasiSerializer

class CartList(generics.ListCreateAPIView):
    serializer_class = PemesananSerializer
    def get_queryset(self):
        idc = self.request.query_params.get('id_customer', None)
        queryset = Pemesanan.objects.filter(id_customer=idc, status='Cart')
        return queryset

class PemesananList(generics.ListCreateAPIView):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananSerializer

class RegisterCustomer(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    def get_queryset(self):
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if self.request.method == 'POST':
            queryset = Customer.objects.all()
            return queryset

        # if self.request.method == 'GET':
        #     queryset = Customer.objects.all()
        #     return queryset
