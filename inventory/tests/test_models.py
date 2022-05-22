from django.test import TestCase

from inventory.models import Item, Warehouse

warehouse_one = {
    'name': 'Warehouse1',
    'capacity': 100,
    'address': '1234 Adrress A, Ottawa ON, Canada'
}

warehouse_one__str__ = f'{ warehouse_one["name"] }, { warehouse_one["address"] }, Capacity [ { warehouse_one["capacity"] } ]'

item_one = {
    'name': 'Item 1',
    'amount': 20,
    'unit_price': 34.25,
    'storage_space': 2
}

item_one__str__ = f'{ item_one["name"] }, ${ item_one["unit_price"] }, In stock [ { item_one["amount"] } ], Stored at => [ { warehouse_one__str__ } ]'


# Warehouses

class InventoryTest(TestCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.create_warehouse(self)

    def create_warehouse(self,
                        name=warehouse_one['name'],
                        capacity=warehouse_one['capacity'],
                        address=warehouse_one['address']):
        self.warehouse = Warehouse.objects.create(name=name,
                                        capacity=capacity,
                                        address=address)
                                        
    def test_warehouse_creation(self):
        self.assertTrue(isinstance(self.warehouse, Warehouse))
        self.assertEquals(self.warehouse.__str__(), warehouse_one__str__)


# Items

    @classmethod
    def create_item(self,
                name=item_one['name'],
                amount=item_one['amount'],
                unit_price=item_one['unit_price'],
                storage_space=item_one['storage_space'],
                warehouse=None):
        if warehouse is None: warehouse = self.warehouse
        return Item.objects.create(name=name,
                                    amount=amount,
                                    unit_price=unit_price,
                                    storage_space=storage_space,
                                    warehouse=warehouse)

    def test_item_creation(self):
        item = self.create_item()
        self.assertTrue(isinstance(item, Item))
        self.assertEquals(item.__str__(), item_one__str__)
        self.assertEquals(item.warehouse, self.warehouse)

