from django.db import models


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