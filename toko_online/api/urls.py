from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^customer_detail/$', views.CustomerDetail.as_view()),
    url(r'^produk_list/$', views.ProdukList.as_view()),
    url(r'^produk_detail/$', views.ProdukDetail.as_view()),
    url(r'^notifikasi/$', views.NotifikasiList.as_view()),
    url(r'^cart_list/$', views.CartList.as_view()),
    url(r'^pemesanan/$', views.PemesananList.as_view()),
    url(r'^register_customer/$', views.RegisterCustomer.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
