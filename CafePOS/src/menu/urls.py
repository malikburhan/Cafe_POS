from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('category', views.menu_category_list, name='menu_category_list'),
    path('category/add', views.menu_category_add, name='menu_category_add'),
    path('category/<str:id>/edit', views.menu_category_edit, name='menu_category_edit'),
    path('category/<str:id>/delete', views.menu_category_delete, name='menu_category_delete'),

    path('', views.menu_list, name='menu_list'),
    path('add', views.menu_add, name='menu_add'),
    path('<str:id>/edit', views.menu_edit, name='menu_edit'),
    path('<str:id>/delete', views.menu_delete, name='menu_delete'),

    # api
    path('get_menu_dd', views.get_menu_dd, name='get_menu_dd'),
    path('get_size_dd', views.get_size_dd, name='get_size_dd'),
]