from django.db import models
from django.db.models import Avg, Sum, Count, Max
from django.db.models import FloatField, F



class Supplier(models.Model):
	supplier = models.CharField(max_length =300)
	phone = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.supplier)	

	
	@classmethod
	def get_all(cls):
			table = Supplier.objects.all()
			return table	

class Item(models.Model):
	item = models.CharField(max_length =300)
	quantity = models.IntegerField()
	price = models.IntegerField()
	units = models.CharField(max_length =300, blank=True, null=True)
	supplier = models.CharField(max_length =300, blank=True, null=True)
	date = models.DateField(auto_now_add=False, blank=True, null=True)

	
	def __str__(self):
		return str(f"item - {self.item}, date - {self.date}")


	
	@classmethod
	def get_all(cls):
			table = Item.objects.all()
			return table	


	@classmethod
	def get_by_id(cls, id):
			retrieved = Item.objects.get(id = id)
			return retrieved	


	@classmethod
	def filter_by_date(cls, date):
			retrieved = Item.objects.filter(date = date)
			return retrieved	


	@classmethod
	def filter_by_supplier(cls, supplier):
			retrieved = Item.objects.filter(supplier = supplier)
			return retrieved	


	@classmethod
	def total_price(cls):
			table = Item.objects.aggregate(Sum('price')).get('price__sum')
			return 0 if (table) == None else table


## Total amounts by filter on one page

	@classmethod
	def total_price_by_items(cls):
			sum_b = Item.objects.values('item').annotate(Sum('price'))
			return sum_b

	@classmethod
	def avg_price_by_items(cls):
			sum_b = Item.objects.values('item', 'units').annotate(average_price =Sum( F('price')/F('quantity')))
			return sum_b

	@classmethod
	def total_quantity_by_item(cls):
			sum_b = Item.objects.values('item', 'units').annotate(Sum('quantity'))
			return sum_b

	@classmethod
	def total_price_by_supplier(cls):
			sum_b = Item.objects.values('supplier').annotate(Sum('price'))
			return sum_b

	@classmethod
	def total_price_by_items_supplier(cls):
			sum_b = Item.objects.values('supplier','item').annotate(Sum('price'))
			return sum_b

	@classmethod
	def average_price_by_items_supplier(cls):
			sum_b = Item.objects.values('supplier','item').annotate(average_price =Sum( F('price')/F('quantity')))
			return sum_b

	@classmethod
	def total_price_by_date(cls):
			sum_b = Item.objects.values('date').annotate(Sum('price'))
			return sum_b


	@classmethod
	def total_amount_by_date_range(cls,date, date2):
			table = list(Item.objects.filter(date__range = [date, date2]).aggregate(Sum('price')).values())
			test = all( i == None for i in table)
			return 1 if (test) == True else float("".join(map(str,table)))



	# @classmethod
	# def total_price_by_item(cls,item):
	# 		table = list(Item.objects.filter(item__iexact = item).aggregate(Sum('price')).values())
	# 		test = all( i == None for i in table)
	# 		return 1 if (test) == True else float("".join(map(str,table)))



	# @classmethod
	# def total_quantity_by_item(cls,item):
	# 		table = list(Item.objects.filter(item__iexact = item).aggregate(Sum('quantity')).values())
	# 		test = all( i == None for i in table)
	# 		return 1 if (test) == True else float("".join(map(str,table)))


	
	# @classmethod
	# def average_by_item(cls,item):
	# 		price = list(Item.objects.filter(item__iexact = item).aggregate(Sum('price')).values())
	# 		test = all( i == None for i in price)
	# 		price = 1 if (test) == True else float("".join(map(str,price)))
	
	# 		quantity = list(Item.objects.filter(item__iexact = item).aggregate(Sum('quantity')).values())
	# 		test = all( i == None for i in quantity)
	# 		quantity = 1 if (test) == True else float("".join(map(str,quantity)))


	# 		return '%.2f'%(price/quantity)
		

	# @classmethod
	# def total_amount_by_supplier(cls,supplier):
	# 		table = list(Item.objects.filter(supplier__iexact = supplier).aggregate(Sum('price')).values())
	# 		test = all( i == None for i in table)
	# 		return 1 if (test) == True else float("".join(map(str,table)))


	# @classmethod
	# def total_amount_by_date(cls,date):
	# 		table = list(Item.objects.filter(date__iexact = date).aggregate(Sum('price')).values())
	# 		test = all( i == None for i in table)
	# 		return 1 if (test) == True else float("".join(map(str,table)))

