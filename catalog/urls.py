from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, UserQuestionCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', UserQuestionCreateView.as_view(), name='contact'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view'),
    path('create/', ProductCreateView.as_view(), name='create'),
]
