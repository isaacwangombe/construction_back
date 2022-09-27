from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Item,Supplier, Units, Date
from .serializer import ItemSerializer, SupplierSerializer, DateSerializer, UnitsSerializer



class DateList(APIView):
  def get(self, request, format=None):
    all_dates = Date.get_all()
    serializers = DateSerializer(all_dates, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = DateSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



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

  def post(self, request, format=None):
    serializers = ItemSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class ItemList(APIView):
  def get(self, request, format=None):
    all_item = Item.get_all()
    serializers = ItemSerializer(all_item, many=True)
    return Response(serializers.data)