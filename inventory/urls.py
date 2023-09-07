from django.urls import path
from . import views

urlpatterns = [
    path('api/inventory/', views.InventoryListAPI.as_view(), name='inventory-list-api'),
    path('inventory/', views.inventory_list, name='inventory-list'),
    path('inventory/<int:id>', views.inventory_detail, name='inventory-detail')
]