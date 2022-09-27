from django.urls import path, include
from . import views, api_views

urlpatterns = [
  path('', views.welcome,name = 'test'),


  path('api/all_units', api_views.UnitsList.as_view()),
  path('api/all_suppliers', api_views.SupplierList.as_view()),
  path('api/all_items', api_views.ItemList.as_view()),
  path('api/item_by_date/<date>', api_views.ByDateList.as_view()),
  path('api/item_by_supplier/<supplier>', api_views.BySupplierList.as_view()),
  path('api/item_by_id/<id>', api_views.ById.as_view()),
]
