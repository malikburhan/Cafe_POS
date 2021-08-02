from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('', views.order_list, name='list'),
    path('service/table/', views.order_service_table, name='service_table'),
    path('service/<str:id_table>', views.order_service_customer, name='service_customer'),
    path('<str:id>/service/', views.order_service, name='service'),

    path('takeaway', views.order_takeaway_customer, name='takeaway_customer'),
    path('<str:id>/takeaway', views.order_takeaway, name='takeaway'),

    path('delivery', views.order_delivery_customer, name='delivery_customer'),
    path('<str:id>/delivery', views.order_delivery, name='delivery'),

    # for order 1.
    path('get_temp_order_items', views.TableOrderItemListSerializerView.as_view(), name='get_temp_order_items'),
    path('add_temp_order_item', views.add_temp_order_item, name='add_temp_order_item'),
    path('remove_temp_order_item', views.remove_temp_order_item, name='remove_temp_order_item'),
    path('commit_temp_order_items', views.commit_temp_order_items, name='commit_temp_order_items'),
    path('<str:id>/complete', views.order_complete, name='order_complete'),
    path('<str:id>/invoice', views.order_invoice, name='invoice'),

    path('table', views.order_list, name='table'),

]