from django.urls import path, include
from . import views, api_views

urlpatterns = [
  path('', views.welcome,name = 'test'),
  path('items/<supplier>/<item>', views.welcome2,name = 'test2'),


  path('api/all_suppliers', api_views.SupplierList.as_view()),
  path('api/all_items', api_views.ItemList.as_view()),
  path('api/item_by_dates/<date>', api_views.ByDateList.as_view()),
  path('api/item_by_supplier/<supplier>', api_views.BySupplierList.as_view()),
  path('api/item_by_id/<id>', api_views.ById.as_view()),

  ## Calculation apis

  path('api/total_price', api_views.TotalPrice.as_view()),
  path('api/price_by_item', api_views.PriceByItem.as_view()),
  path('api/price_by_item_supplier', api_views.PriceByItemSupplier.as_view()),
  path('api/total_price_by_item/<item>', api_views.TotalPriceByItem.as_view()),
  path('api/average_price_by_item/<item>', api_views.AvgPriceByItem.as_view()),
  path('api/total_amount_by_supplier/<supplier>', api_views.TotalPriceBySupplier.as_view()),
  path('api/total_amount_by_date/<date>', api_views.TotalPriceByDate.as_view()),
  path('api/total_amount_by_date_range/<date>/<date2>', api_views.TotalPriceByDateRange.as_view()),


]
