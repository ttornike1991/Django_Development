from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='Home'),
    path('products',views.products,name='products'),
    path('customers',views.customers,name='customers'),
    path('justProduct',views.justproduct,name='justProduct')
]