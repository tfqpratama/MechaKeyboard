from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class InventoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventori
        fields = '__all__'

class ManajemenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manajemen
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class NotifikasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifikasi
        fields = '__all__'

class PemesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemesanan
        fields = '__all__'

class PesanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesan
        fields = '__all__'
