from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer

class InventoryListAPI(generics.ListAPIView):
    queryset = Inventory.objects.all().select_related('supplier')
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
def inventory_list(request):
        inventories = Inventory.objects.all().select_related('supplier')
        return render(request, 'inventory/inventory_list.html', {'inventories': inventories})

def inventory_detail(request, id):
    item = None
    not_found = False
    try:
        item = Inventory.objects.get(pk=id)
    except Inventory.DoesNotExist:
        not_found = True

    return render(request, 'inventory/inventory_detail.html', {
        'item': item,
        'not_found': not_found
    })