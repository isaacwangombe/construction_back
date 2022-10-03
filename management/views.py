from django.shortcuts import render
from .models import Item,Supplier

# Create your views here.

def welcome(request):
    # total = Item.tbs()
    return render(request, 'test.html' )

  

def welcome2(request, item):

    total = Item.total_price()
    total_item =Item.total_price_by_item(item)
    total_quantity_item =Item.total_quantity_by_item(item)
    avg_item =Item.average_by_item(item)

    return render(request, 'test.html', {'total':total, 'item':item,'total_item':total_item,'total_quantity_item':total_quantity_item,'avg_item':avg_item } )


def welcome2(request, item, supplier):

    total = Item.avg_amount_item_by_supplier(item, supplier)
   

    return render(request, 'test2.html', {'total':total, 'item':item,'supplier':supplier} )

