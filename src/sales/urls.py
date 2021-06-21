from django.urls import path
from .views import (
    home_view,
    SaleListView,
    DetailListView,
)

app_name = 'sales'
urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SaleListView.as_view(), name='list'),
    path('sales/<pk>/', DetailListView.as_view(), name='detail'),
]