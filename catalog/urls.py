from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, product, new_product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='index'),
    path('contact/', contact, name='contact'),
    path('product/<int:product_id>', product, name='product'),
    path('new_product/', new_product, name='new_product'),
]
