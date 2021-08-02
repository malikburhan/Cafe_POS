from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'accounts'
urlpatterns = [
    path('', views.accounts_list, name='list'),
    path('<str:id>/profile', views.accounts_profile, name='profile'),

    path('register/', views.register, name='register'),
    path('<str:id>/profile/add', views.accounts_add_profile, name='add_profile'),
    path('<str:id>/edit', views.accounts_edit, name='edit'),
    path('<str:id>/delete', views.accounts_delete, name='delete'),

    path('login', auth_view.LoginView.as_view(), name='login'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

]

