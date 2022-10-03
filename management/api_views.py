from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Item,Supplier
from .serializer import ItemSerializer, SupplierSerializer


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

  def delete(self, request,id, format=None):
    item = Item.get_by_id(id)
    item.delete()    
    return Response({'message': 'item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

  def patch(self, request,id, format=None):
    item = Item.get_by_id(id)
    serializers = ItemSerializer(item, data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


### Calculation results


class TotalPrice(APIView):
		def get(self, request):
			total_price = Item.total_price()
			return Response({"total_price":total_price})



class PriceByItem(APIView):
		def get(self, request):
			price_by_item = Item.total_price_by_items()
			return Response(price_by_item)

class AvgByItem(APIView):
		def get(self, request):
			price_by_item = Item.avg_price_by_items()
			return Response({"price_by_item":price_by_item})

class QtyByItem(APIView):
		def get(self, request):
			qty_by_item = Item.total_quantity_by_item()
			return Response({"qty_by_item":qty_by_item})

class PriceByItemSupplier(APIView):
		def get(self, request):
			price_by_item = Item.total_price_by_items_supplier()
			return Response({"price_by_item":price_by_item})

class AvgPriceByItemSupplier(APIView):
		def get(self, request):
			price_by_item = Item.average_price_by_items_supplier()
			return Response({"price_by_item":price_by_item})

class PriceBySupplier(APIView):
		def get(self, request):
			price_by_supplier = Item.total_price_by_supplier()
			return Response({"price_by_supplier": price_by_supplier})

class PriceByDate(APIView):
		def get(self, request):
			price_by_date = Item.total_price_by_date()
			return Response({"price_by_date":price_by_date})



class TotalPriceByDateRange(APIView):
		def get(self, request,date, date2):
			total_amount_by_date_range = Item.total_amount_by_date_range(date, date2)
			return Response({"total_amount_by_date_range":total_amount_by_date_range})



# class TotalPriceByItem(APIView):
# 		def get(self, request,item):
# 			total_price_by_item = Item.total_price_by_item(item)
# 			return Response({"total_price_by_item":total_price_by_item})


# class AvgPriceByItem(APIView):
# 		def get(self, request,item):
# 			average_price_by_item = Item.average_by_item(item)
# 			return Response({"average_price_by_item":average_price_by_item})

# class TotalPriceBySupplier(APIView):
# 		def get(self, request,supplier):
# 			total_amount_by_supplier = Item.total_amount_by_supplier(supplier)
# 			return Response({"total_amount_by_supplier":total_amount_by_supplier})

# class TotalPriceByDate(APIView):
# 		def get(self, request,date):
# 			total_amount_by_date = Item.total_amount_by_date(date)
# 			return Response({"total_amount_by_date":total_amount_by_date})