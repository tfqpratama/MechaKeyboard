from __future__ import unicode_literals
from django.db import models

class Customer(models.Model):
    id_customer = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255, default=None)

    class Meta:
        managed = False
        db_table = 'customer'

class Inventori(models.Model):
    id_inventori = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'inventori'

class Manajemen(models.Model):
    id_manajemen = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'manajemen'

class Produk(models.Model):
    id_produk = models.CharField(max_length=20, primary_key=True)
    id_inventori = models.ForeignKey(Inventori, models.DO_NOTHING, db_column='id_inventori')
    nama = models.CharField(max_length=255)
    tanggal_masuk = models.DateTimeField(auto_now_add=True)
    manufacturer = models.CharField(max_length=20)
    led_color = models.CharField(max_length=20)
    switch_type = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    stok = models.IntegerField

    class Meta:
        managed = False
        db_table = 'produk'

class Notifikasi(models.Model):
    id_notif = models.IntegerField(primary_key=True)
    id_produk = models.ForeignKey(Produk, models.DO_NOTHING, db_column='id_produk')
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer')
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'notifikasi'

class Pemesanan(models.Model):
    id_order = models.IntegerField(primary_key=True)
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer')
    id_manajemen = models.ForeignKey(Manajemen, models.DO_NOTHING, db_column='id_manajemen')
    alamat_kirim = models.TextField
    status = models.CharField(max_length=20)
    rek_customer = models.CharField(max_length=60)
    rek_tujuan = models.CharField(max_length=60)
    tgl_pesan = models.DateTimeField(auto_now_add=True)
    tgl_konfirmasi = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'pemesanan'

class Pesan(models.Model):
    id_pesan = models.IntegerField(primary_key=True)
    id_order = models.ForeignKey(Pemesanan, models.DO_NOTHING, db_column='id_order')
    id_produk = models.ForeignKey(Produk, models.DO_NOTHING, db_column='id_produk')
    jumlah = models.IntegerField
