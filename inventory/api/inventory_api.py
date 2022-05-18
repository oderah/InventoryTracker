from inventory.serializers import ItemSerializer, WarehouseSerializer
from rest_framework import viewsets
from inventory.models import *

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer