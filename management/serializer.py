from rest_framework import serializers
from .models import Item,Supplier


class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Supplier
    fields = ('id', 'supplier', 'phone')


class ItemSerializer(serializers.ModelSerializer):


  class Meta:
    model = Item
    fields = ('id', 'item','quantity', 'price', 'units','supplier', 'date' )