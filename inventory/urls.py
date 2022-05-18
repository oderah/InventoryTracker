from django.urls import path
from rest_framework import routers
from .api.inventory_api import ItemViewSet, WarehouseViewSet

router = routers.DefaultRouter()

router.register('warehouses', WarehouseViewSet)
router.register('items', ItemViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls