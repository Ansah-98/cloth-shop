from .views import ListProduct
from django.urls import path

urlpatterns = [
    path('',ListProduct.as_view())]
