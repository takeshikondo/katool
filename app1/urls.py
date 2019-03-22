from django.urls import path
from . import views

urlpatterns = [
        path('func/', views.func_choice, name='app1_func'),
        path('', views.func_choice, name='app1_func'),         
        path('predict/', views.predict, name='app1_predict'),
        path('predict2/', views.predict2, name='app1_predict2'),      
        path('shop_info/', views.shop_info, name='app1_shop_info'),
        path('sales/', views.sales_choice, name='app1_sales'),
        path('sales_chart/', views.sales_chart, name='app1_sales_chart'),
        path('sales_area/', views.sales_area, name='app1_sales_area'),
        path('sales_order/', views.sales_order, name='app1_sales_order'),
]