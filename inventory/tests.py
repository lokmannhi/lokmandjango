from django.test import TestCase
from django.urls import reverse
from .models import Inventory, Supplier

class InventoryTestCase(TestCase):
    def test_inventory_list_view(self):
        response = self.client.get(reverse('inventory-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_inventory_api_view(self):
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, 200)
    
    def test_inventory_detail_view(self):
        supplier = Supplier.objects.create(name="Test Supplier")
        inventory = Inventory.objects.create(
        name="Test Item",
        description="Test Description",
        note="Test Note",
        stock=10,
        availability=True,
        supplier=supplier
        )
        response = self.client.get(reverse('inventory-detail', args=[inventory.id]))
        self.assertEqual(response.status_code, 200)