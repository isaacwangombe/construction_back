from django.urls import path, include
from . import views, api_views

urlpatterns = [
  path('', views.welcome,name = 'test'),


  path('api/date', api_views.DateList.as_view()),
  path('api/units', api_views.UnitsList.as_view()),
  path('api/supplier', api_views.SupplierList.as_view()),
  path('api/item', api_views.ItemList.as_view()),
]
