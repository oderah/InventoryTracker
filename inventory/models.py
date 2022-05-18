from pydoc import describe
from django.db import models

class Warehouse(models.Model):
    name = models.TextField()
    capacity = models.IntegerField(default=500)
    address = models.TextField()

    def __str__(self):
        return f'{ self.name }, { self.address }, Capacity [ { self.capacity } ]'

class Item(models.Model):
    name = models.TextField()
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    storage_space = models.IntegerField(default=1)
    warehouse = models.ForeignKey(Warehouse, related_name="items", on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.name }, ${ self.price }, In stock [ { self.amount } ], Stored at => [ { self.warehouse } ]'
