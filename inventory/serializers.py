from rest_framework import serializers
from .models import Inventory, Supplier

class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)

    class Meta:
        model: Inventory
        fields: ['id', 'name', 'availability', 'supplier_name']