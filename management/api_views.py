from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Item,Supplier, Units
from .serializer import ItemSerializer, SupplierSerializer, UnitsSerializer



class UnitsList(APIView):
  def get(self, request, format=None):
    all_units = Units.get_all()
    serializers = UnitsSerializer(all_units, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = UnitsSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class SupplierList(APIView):
  def get(self, request, format=None):
    all_supplier = Supplier.get_all()
    serializers = SupplierSerializer(all_supplier, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = SupplierSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class ItemList(APIView):
  def get(self, request, format=None):
    all_item = Item.get_all()
    serializers = ItemSerializer(all_item, many=True)
    return Response(serializers.data)

  def put(self, request, format=None):
    serializers = ItemSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class BySupplierList(APIView):
  def get(self, request,supplier, format=None):
    items = Item.filter_by_supplier(supplier)
    serializers = ItemSerializer(items, many=True)
    return Response(serializers.data)

class ByDateList(APIView):
  def get(self, request, date, format=None):
    items = Item.filter_by_date(date)
    serializers = ItemSerializer(items, many=True)
    return Response(serializers.data)

class ById(APIView):
  def get(self, request,id, format=None):
    item = Item.get_by_id(id)
    serializers = ItemSerializer(item, many=False)
    return Response(serializers.data)
