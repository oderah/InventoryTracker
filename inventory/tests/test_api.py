from http import HTTPStatus
from typing import OrderedDict
from inventory.serializers import ItemSerializer
from rest_framework.test import APITestCase, APIClient
from inventory.models import *

control = Item(
    id=1,
    name='Item 1',
    amount=20,
    unit_price=34.25,
    storage_space=2,
    warehouse=Warehouse(
        id=1,
        name='Warehouse1',
        capacity=100,
        address='1234 Adrress A, Ottawa ON, Canada'
    )
)

class InventoryAPITest(APITestCase):

    @classmethod
    def setUpTestData(self):
        self.api_client = APIClient()
        warehouse = Warehouse.objects.create(
            name=control.warehouse.name,
            capacity=control.warehouse.capacity,
            address=control.warehouse.address
        )
        warehouse.save()
        Item.objects.create(
            name=control.name,
            amount=control.amount,
            unit_price=control.unit_price,
            storage_space=control.storage_space,
            warehouse=warehouse
        ).save()

    def test_retrieve_warehouse_items(self):
        response = self.client.get('/api/warehouses/1/items/')
        self.assertEqual(response.status_code, HTTPStatus.OK.value, response)
        self.assertEqual(response.data['results'], ItemSerializer(
            [ control ],
            many=True
        ).data)