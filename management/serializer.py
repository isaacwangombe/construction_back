from rest_framework import serializers
from .models import Item,Supplier, Units


class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Supplier
    fields = ('id', 'supplier', 'phone')


class UnitsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Units
    fields = ('id', 'units')


class ItemSerializer(serializers.ModelSerializer):
  units = UnitsSerializer()
  supplier = SupplierSerializer()

  class Meta:
    model = Item
    fields = ('id', 'item','quantity', 'price', 'units','supplier', 'date' )