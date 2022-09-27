from django.db import models

# Create your models here.

class Date(models.Model):
	date = models.DateField(auto_now_add=False)
	
	def __str__(self):
		return str(self.date)

	
	@classmethod
	def get_all(cls):
			table = Date.objects.all()
			return table	
	


class Units(models.Model):
	units = models.CharField(max_length =300)

	def __str__(self):
		return str(self.units)	

	class Meta:
		verbose_name_plural  =  "Units" 

	
	@classmethod
	def get_all(cls):
			table = Units.objects.all()
			return table	


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
	units = models.ForeignKey(Units, on_delete=models.CASCADE, blank=True, null=True)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
	date = models.ForeignKey(Date, on_delete=models.CASCADE, blank=True, null=True)
	
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