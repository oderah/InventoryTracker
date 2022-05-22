from inventory.serializers import ItemSerializer, WarehouseSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from inventory.models import *

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    @action(detail=True, methods=[ 'get' ])
    def items(self, request, pk=None):
        try:
            warehouse = self.queryset.get(id=pk)
            items = warehouse.items.all()
            page = self.paginate_queryset(items)
            
            if page is None:
                return Response(
                    ItemSerializer(
                        warehouse.items.all(),
                        many=True
                    ).data,
                    status=status.HTTP_200_OK
                )

            return self.get_paginated_response(
                ItemSerializer(
                    items,
                    many=True
                ).data
            )
        except Warehouse.DoesNotExist:
            return Response(
                {
                    'detail': f'warehouse with pk { pk } does not exist'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer