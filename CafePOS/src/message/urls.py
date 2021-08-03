from django.urls import path
from . import views

app_name = 'message'
urlpatterns = [
    path('send_message_api/', views.ListSendMessageApiView.as_view(), name='send_message_api'),
    path('update_message_api/', views.update_message_api, name='update_message_api'),
]
