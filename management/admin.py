from django.contrib import admin
from .models import Item,Supplier, Units, Date
# Register your models here.


admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Units)
admin.site.register(Date)