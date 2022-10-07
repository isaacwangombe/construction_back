from django.contrib import admin
from .models import Item,Supplier, Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    exclude = ["id"]


admin.site.register(Item)
admin.site.register(Supplier)
admin.site.register(Project, ProjectAdmin)
