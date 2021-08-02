from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.customer_list, name='list'),
    path('add', views.customer_add, name='add'),
    path('<str:id>/profile', views.customer_profile, name='profile'),
    path('<str:id>/edit', views.customer_edit, name='edit'),
    path('<str:id>/delete', views.customer_delete, name='delete'),

]